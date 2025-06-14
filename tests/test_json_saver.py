import os

import pytest

from src.models.vacancy import Vacancy
from src.storage.json_saver import JSONSaver


@pytest.fixture
def saver():
    filename = "test.json"
    saver = JSONSaver(filename=filename)
    yield saver
    if os.path.exists(filename):
        os.remove(filename)

@pytest.fixture
def vacancy():
    return Vacancy(vacancy_id="1", title="js", url="url", salary={"from":50000}, description="descr")


def test_add_and_get(saver, vacancy):
    saver.add_vacancy(vacancy)
    data = saver.get_all()
    assert len(data) == 1
    assert data[0]["title"] == "js"


def test_delete_vacancy(saver, vacancy):
    saver.add_vacancy(vacancy)
    saver.delete_vacancy(vacancy)
    data = saver.get_all()
    assert data == []

