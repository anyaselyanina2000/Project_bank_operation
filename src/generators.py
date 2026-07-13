from typing import List, Dict, Generator


def filter_by_currency(transactions: List[Dict], currency: str) -> Generator[Dict, None, None]:
    """Функция, которая принимает на вход список словарей, представляющих транзакции."""
    for transaction in transactions:
        if transaction['operationAmount']['currency']['name'] == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict]) -> Generator[str, None, None]:
    """Генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    for transaction in transactions:
        yield transaction['description']


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты."""
    for number in range(start, end + 1):
        yield f"{number:016}"
