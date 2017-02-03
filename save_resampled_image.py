import os
import dicom
import scipy.ndimage
import numpy as np
import matplotlib.pyplot as plt
import pandas
import csv

# Load the scans in given folder path
def load_scan(path):
    slices = [dicom.read_file(path + '/' + s) for s in os.listdir(path)]
    slices.sort(key = lambda x: int(x.InstanceNumber))
    try:
        slice_thickness = np.abs(slices[0].ImagePositionPatient[2] - slices[1].ImagePositionPatient[2])
    except:
        slice_thickness = np.abs(slices[0].SliceLocation - slices[1].SliceLocation)

    for s in slices:
        s.SliceThickness = slice_thickness

    return slices

# scale and translate pixel value to HU unit
def get_pixels_hu(scans):
    image = np.stack([s.pixel_array for s in scans])
    # Convert to int16 (from sometimes int16),
    # should be possible as values should always be low enough (<32k)
    image = image.astype(np.int16)

    # Set outside-of-scan pixels to 0
    # The intercept is usually -1024, so air is approximately 0
    # image[image == -2000] = 0

    # Convert to Hounsfield units (HU)
    intercept = scans[0].RescaleIntercept
    slope = scans[0].RescaleSlope

    if slope != 1:
        image = slope * image.astype(np.float64)
        image = image.astype(np.int16)

    image += np.int16(intercept)

    return np.array(image, dtype=np.int16)

def resample(image, scan, new_spacing=[1,1,1]):
    # Determine current pixel spacing
    spacing = map(float, ([scan[0].SliceThickness] + scan[0].PixelSpacing))
    spacing = np.array(list(spacing))

    resize_factor = spacing / new_spacing
    new_real_shape = image.shape * resize_factor
    new_shape = np.round(new_real_shape)
    real_resize_factor = new_shape / image.shape
    new_spacing = spacing / real_resize_factor

    image = scipy.ndimage.interpolation.zoom(image, real_resize_factor, mode='nearest')

    return image, new_spacing

DATASET_DIR = "E:/stage1/stage1"
OUTPUT_DIR = "D:/stage1/resampled/"
INFO_FILE = "D:/stage1/patient_info.csv"
all_patient_ids = os.listdir(DATASET_DIR)
all_patient_ids.sort()
df_info = pandas.read_csv(INFO_FILE)
i = 0

for patient_id in all_patient_ids:
    # record already resampled
    if patient_id in df_info.id.values:
        continue

    # load patient
    DCM_PATH = DATASET_DIR + "/" + patient_id
    OUTPUT_PATH = OUTPUT_DIR + patient_id
    dcm = load_scan(DCM_PATH)
    mat = get_pixels_hu(dcm)

    # resample
    mat_resampled, spacing = resample(mat, dcm)

    # persist resampled matrix
    np.save(OUTPUT_PATH, mat_resampled)

    # update record info
    with open(INFO_FILE, 'a') as file_info:
        writer = csv.writer(file_info, lineterminator = '\n')
        depth = mat_resampled.shape[0]
        width = mat_resampled.shape[1]
        height = mat_resampled.shape[2]
        writer.writerow([patient_id, width, height, depth])

    print(patient_id, mat.shape, mat_resampled.shape)

    # loop control
    i = i + 1
    if i >= 100:
        break
