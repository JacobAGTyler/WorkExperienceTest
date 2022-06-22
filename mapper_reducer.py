from collections import OrderedDict


class MapReduce:
    def __init__(self):
      self.initial = {}
      self.intermediate = OrderedDict()
      self.result = []

    def set_initial(self, data: dict):
      self.initial = data

    def store_intermediate(self, key, value):
      self.intermediate.setdefault(key, [])
      self.intermediate[key].append(value)

    def store_result(self, value):
      self.result.append(value)

    def execute(self, mapper: callable, reducer: callable):
      for record in data:
        mapper(record)

      for key in self.intermediate:
        reducer(key, self.intermediate[key])

      self.result.sort()
        


