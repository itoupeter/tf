import pandas
import numpy

a = numpy.random.rand(6, 3)
df = pandas.DataFrame(a, columns = ['a', 'b', 'c'])
df.to_csv('tmp.csv', columns = ['b', 'a'])
