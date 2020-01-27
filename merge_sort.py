from sort import Sort

count = 100000;

class MergeSort(Sort):
  def __init__(self, count):
    self.type = 'merge'
    Sort.__init__(self, count)

  def sort(self):
    
    while len(self.numbers) > 1:
      a1 = self.numbers.pop(0)
      a2 = self.numbers.pop(0)
      if isinstance(a1, int):
        a1 = [a1]
      if isinstance(a2, int):
        a2 = [a2]
      self.numbers.append(self.merge(a1,a2))

  def merge(self, a1, a2):
    result = []
    while (not len(a1) == 0 or not len(a2) == 0):
      if len(a1) == 0:
        result.append(a2.pop(0))
      elif (len(a2) == 0):
        result.append(a1.pop(0))
      elif (a1[0] > a2[0]):
        result.append(a2.pop(0))
      else:
        result.append(a1.pop(0))
    return result

s = MergeSort(count)
s.execute()

# results:
# 1000 ~ 10ms
# 10000 ~ 130ms
# 20000 ~ 475ms
# 50000 ~ 2150ms
# 100000 ~ 7800ms

# O(nlgn) 
