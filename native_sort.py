from sort import Sort

count = 50000;

class NativeSort(Sort):
  def __init__(self, count):
    self.type = 'native'
    Sort.__init__(self, count)

  def sort(self):
    self.numbers.sort()

s = NativeSort(count)
s.execute()

# very fast