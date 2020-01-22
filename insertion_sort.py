import random
import time
import datetime
import sys

count = 100;

print('Hi, its insertion sort!')
print('Count: ' + str(count))

#generate random list
numbers = []
for x in range(count):
  numbers.append(random.randint(1,1000))
print('Source list:')
print(numbers)

# start time
start_time = int(round(time.time() * 1000))

# create new sorted list
sorted = []
# first insertion
sorted.insert(0, numbers.pop())

def insert_order(list, ins):
  for z in list:
    if z > ins:
      list.insert(list.index(z), ins)
      return
  list.append(ins)

for x in numbers:
  insert_order(sorted, x)

print('Sorted list:')
print(sorted)

# end time
end_time = int(round(time.time() * 1000))

print('Time:')
print(end_time - start_time)

# results:
# 1000 ~ 60ms
# 10000 ~ 1700ms
# 20000 ~ 6500ms
# 100000 ~ too long :)
