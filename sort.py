import random
import time
import datetime
import sys

class Sort:
  def __init__(self, count):
    self.count = count
    print('Hi, its ' + self.type + ' sort!')

  def generate(self):
    self.numbers = []
    for x in range(self.count):
      self.numbers.append(random.randint(1,1000))
    print('Generate list. Len:' + str(self.count))
    print(self.numbers)
    
  
  def sort(self):
    pass
  
  def result(self):
    print('Sorted list:')
    print(self.numbers)

  def execute(self):
    self.generate()
    self.start_time = int(round(time.time() * 1000))
    self.sort()
    self.end_time = int(round(time.time() * 1000))
    self.result()
    print('Time:')
    print(self.end_time - self.start_time)



