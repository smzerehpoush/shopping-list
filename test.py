import random
import numpy

arr = [0, 0, 0, 0, 0, 0, 0]
counter = 0
while counter < 100000000:
    arr[random.randint(1, 6)] += 1
    counter += 1
np_arr = numpy.array(arr)
print(np_arr / 10000, '%')
