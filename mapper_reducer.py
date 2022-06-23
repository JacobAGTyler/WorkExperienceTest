from collections import OrderedDict
from collections.abc import Callable
from typing import Union

DataKey = Union[str, int]
DataValue = Union[str, int]

MapperFunction = Callable[[object, DataValue], None]
ReducerFunction = Callable[[object, DataKey, DataValue], None]


class MapReduce:
    def __init__(self):
        self.initial = {}
        self.intermediate = OrderedDict()
        self.result = []

    def set_initial(self, data: dict):
        self.initial = data

    def store_intermediate(self, key: DataKey, value: DataValue):
        self.intermediate.setdefault(key, [])
        self.intermediate[key].append(value)

    def store_result(self, value: DataValue):
        self.result.append(value)

    def execute(self, mapper: MapperFunction, reducer: ReducerFunction):
        for record in self.initial:
            mapper(self, record)

        for key in self.intermediate:
            reducer(self, key, self.intermediate[key])

        self.result.sort()
