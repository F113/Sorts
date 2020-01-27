from sort import Sort

count = 1000;

class InsertionSort(Sort):
  def __init__(self, count):
    self.type = 'insertion'
    Sort.__init__(self, count)

  def sort(self):
    sorted = []
    sorted.insert(0, self.numbers.pop())
    for x in self.numbers:
      self.insert_order(sorted, x)
    self.numbers = sorted

  def insert_order(self, list, ins):
    for z in list:
      if z > ins:
        list.insert(list.index(z), ins)
        return
    list.append(ins)

s = InsertionSort(count)
s.execute()

# results:
# 1000 ~ 10ms
# 10000 ~ 950ms
# 20000 ~ 4000ms

# O(n^2)

