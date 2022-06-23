import pytest

from dataclasses import dataclass
from data import save_obj


@dataclass
class FixtureClass:
    id: int
    name: str
    number: int


def test_save_obj():
    fc = FixtureClass(id=1, name='Jacob', number=42)
    result = save_obj(fc)

    assert result is True


@dataclass
class IdFreeFixtureClass:
    name: str
    number: int


def test_save_id_free_save_obj():
    id_free = IdFreeFixtureClass(number=43, name='Jacob')

    with pytest.raises(AttributeError):
        result = save_obj(id_free)
        assert result is False
