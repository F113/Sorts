import random
import time
import datetime
import sys

count = 1000;

print('Hi, its merge sort!')
print('Count: ' + str(count))

#generate random list
numbers = []
for x in range(count):
  numbers.append([random.randint(1,1000)])
print('Source list:')
print(numbers)

# start time
start_time = int(round(time.time() * 1000))

# create new sorted list
#sorted = []
# first insertion
#sorted.insert(0, numbers.pop())

def merge(arr1, arr2):
  result = []
  while (not len(arr1) == 0 or not len(arr2) == 0):
    if len(arr1) == 0:
      result.append(arr2.pop(0))
    elif (len(arr2) == 0):
      result.append(arr1.pop(0))
    elif (arr1[0] > arr2[0]):
      result.append(arr2.pop(0))
    else:
      result.append(arr1.pop(0))
  return result

while len(numbers) > 1:
  a1 = numbers.pop(0)
  a2 = numbers.pop(0)
  numbers.append(merge(a1,a2))

print('Sorted list:')
print(numbers)

# end time
end_time = int(round(time.time() * 1000))

print('Time:')
print(end_time - start_time)

# results:
# 1000 ~ 10ms
# 10000 ~ 170ms
# 20000 ~ 475ms
# 50000 ~ 2154ms
# good!
