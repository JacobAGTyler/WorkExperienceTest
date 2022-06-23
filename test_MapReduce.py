import pytest

from mapper_reducer import MapReduce
from collections import OrderedDict


@pytest.fixture
def data() -> [tuple]:
    return [
        ('AB389', 'AB290'),
        ('AB3882', 'AB290'),
        ('AB3882', 'AB399'),
        ('AB500', 'AB399'),
        ('AB8339', 'AB399'),
        ('AB400', 'AB3882'),
        ('AB399', 'AB3882'),
        ('AB290', 'AB3882'),
        ('AB190', 'AB3882'),
        ('AB3882', 'AB190')
    ]


@pytest.fixture
def mr(data) -> MapReduce:
    mr = MapReduce()
    mr.set_initial(data=data)
    return mr


def test_init():
    mr = MapReduce()
    assert isinstance(mr, MapReduce)


def test_set_initial(data):
    mr = MapReduce()
    mr.set_initial(data=data)

    assert mr.initial == data


def test_store_intermediate(mr):
    mr.store_intermediate('TEST', 'VALUE')

    assert mr.intermediate == OrderedDict({'TEST': ['VALUE']})


def test_store_result(mr: MapReduce):
    mr.store_result()


