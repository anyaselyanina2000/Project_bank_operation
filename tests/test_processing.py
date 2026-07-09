from typing import Dict, List

import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def operations() -> List[Dict[str, str]]:
    return [
        {'id': '41428829', 'state': 'EXECUTED',
         'date': '2019-07-03T18:35:29.512364'},
        {'id': '594226727', 'state': 'CANCELED',
         'date': '2018-09-12T21:27:25.241689'},
        {'id': '939719570', 'state': 'EXECUTED',
         'date': '2018-06-30T02:08:58.425572'}
    ]


def test_filter_by_state(operations: List[Dict[str, str]]) -> None:
    """Тестирование фильтрации списка словарей
    по заданному статусу state."""
    assert filter_by_state(operations, 'EXECUTED') == [
        {'id': '41428829', 'state': 'EXECUTED',
         'date': '2019-07-03T18:35:29.512364'},
        {'id': '939719570', 'state': 'EXECUTED',
         'date': '2018-06-30T02:08:58.425572'}
    ]
    assert filter_by_state(operations, 'CANCELED') == [
        {'id': '594226727', 'state': 'CANCELED',
         'date': '2018-09-12T21:27:25.241689'}
    ]


def test_sort_by_date(operations: List[Dict[str, str]]) -> None:
    """Тестирование сортировки списка словарей по
    датам в порядке убывания и возрастания."""
    assert sort_by_date(operations) == [
        {'id': '41428829', 'state': 'EXECUTED',
         'date': '2019-07-03T18:35:29.512364'},
        {'id': '594226727', 'state': 'CANCELED',
         'date': '2018-09-12T21:27:25.241689'},
        {'id': '939719570', 'state': 'EXECUTED',
         'date': '2018-06-30T02:08:58.425572'}
    ]
