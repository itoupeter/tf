import os
import dicom
import scipy.ndimage
import numpy as np
import matplotlib.pyplot as plt

MIN_BOUND = -1000.0
MAX_BOUND = 400.0

def normalize(image):
    image = (image - MIN_BOUND) / (MAX_BOUND - MIN_BOUND)
    image[image>1] = 1.
    image[image<0] = 0.
    return image

INPUT_DIR = "D:/stage1/mat_resampled"
filenames = os.listdir(INPUT_DIR)
filenames.sort()
i = 0

for filename in filenames:
    if i >= 3:
        break
    i += 1
    FULL_PATH = INPUT_DIR + "/" + filename
    mat = np.load(FULL_PATH)

    plt.subplot(2, 2, 1)
    plt.imshow(mat[150], cmap = plt.cm.gray)

    plt.subplot(2, 2, 3)
    plt.hist(mat.flatten())

    plt.subplot(2, 2, 2)
    mat = normalize(mat)
    plt.imshow(mat[150], cmap = plt.cm.gray)

    plt.subplot(2, 2, 4)
    plt.hist(mat.flatten())

    plt.show()
