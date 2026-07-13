import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize('account_card, expected', [
    ('Счет 64686473678894779589', 'Счет **9589'),
    ('Visa Platinum 7000792289606361', 'Visa Platinum 7000 79** **** 6361')])
def test_mask_account_card(account_card: str, expected: str) -> None:
    """Тесты для проверки, что функция корректно распознает и
    применяет нужный тип маскировки в зависимости от типа входных данных
    (карта или счет)."""
    assert mask_account_card(account_card) == expected


@pytest.mark.parametrize('date, expected', [
    ('2024-03-11T02:26:18.671407', '11.03.2024'),
    ('2023-10-01T12:34:56.789', '01.10.2023')
])
def test_get_date(date, expected) -> None:
    """Тестирование правильности преобразования даты."""
    assert get_date(date) == expected
