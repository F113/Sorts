import random
import time
import datetime
import sys
from sort import Sort

count = 1000

class BubbleSort(Sort):
  def __init__(self, count):
    self.type = 'bubble'
    Sort.__init__(self, count)

  def sort(self):
    n = len(self.numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if self.numbers[j] > self.numbers[j+1]:
                self.numbers[j], self.numbers[j+1] = self.numbers[j+1], self.numbers[j]

s = BubbleSort(count)
s.execute()

# results:
# 1000 ~ 120ms
# 10000 ~ 12000ms
# O(n^2)