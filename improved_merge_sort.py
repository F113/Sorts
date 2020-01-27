from sort import Sort

count = 100000;

class ImprovedMergeSort(Sort):
  def __init__(self, count):
    self.type = 'merge'
    Sort.__init__(self, count)

  def sort(self):    
    cnt = range(len(self.numbers))
    leng = len(self.numbers)
    start_end = []
    end_start = []
    tstart = []
    tend = []
    for x in cnt:
      tstart.append(self.numbers[x])

      if (x+1 < leng):
        if (self.numbers[x+1] < self.numbers[x]):
          start_end.append(tstart)
          tstart = []      
      
      tend.append(self.numbers[leng-x-1])
      if (self.numbers[leng-x-1] > self.numbers[leng-x-2]):
        end_start.append(tend)
        tend = []

    start_end.append(tstart)
    end_start.append(tend)
    
    if (len(start_end) < len(end_start)):
      working = start_end
    else:
      working = end_start
    
    while len(working) > 1:
      a1 = working.pop(0)
      a2 = working.pop(0)      
      working.append(self.merge(a1,a2))
    self.numbers = working
    return

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

s = ImprovedMergeSort(count)
s.execute()

# results:
# 1000 ~ 10ms
# 10000 ~ 170ms
# 20000 ~ 330ms
# 50000 ~ 1380ms
# 100000 ~ 4550ms

# cool improvement toward merge sort
