import pytest

from dataclasses import dataclass
from data import save_obj, list_objects
from replit.database import Database
from unittest import mock


@pytest.fixture
def fake_db() -> Database:
    MockDB = mock.Mock(Database)
    fake_db = MockDB()
    fake_db.__setitem__ = mock.MagicMock()
    fake_db.prefix = mock.MagicMock(return_value=[{'id': 'dc_FixtureClass_1', 'name': 'Jacob', 'number': 42}])
    return fake_db


@dataclass
class FixtureClass:
    id: int
    name: str
    number: int


@pytest.fixture
def fixture_instance() -> FixtureClass:
    return FixtureClass(id=1, name='Jacob', number=42)


def test_save_obj(monkeypatch: pytest.MonkeyPatch, fake_db, fixture_instance):
    monkeypatch.setattr('data.db', fake_db)
    result = save_obj(fixture_instance)

    assert result is True


@dataclass
class IdFreeFixtureClass:
    name: str
    number: int


def test_save_id_free_save_obj(monkeypatch: pytest.MonkeyPatch, fake_db):
    monkeypatch.setattr('data.db', fake_db)
    id_free = IdFreeFixtureClass(number=43, name='Jacob')

    with pytest.raises(AttributeError):
        result = save_obj(id_free)
        assert result is False


def test_list_objects(monkeypatch: pytest.MonkeyPatch, fake_db):
    monkeypatch.setattr('data.db', fake_db)
    lst = list_objects(FixtureClass)

    assert type(lst) == list
    assert lst == [FixtureClass(id=1, name='Jacob', number=42)]
