from mapper_reducer import MapReduce





def mapper(executor: MapReduce) -> None:
    executor.store_intermediate('A')


def reducer(exector: MapReduce) -> None:
