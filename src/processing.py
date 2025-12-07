from typing import List, Dict, Optional
from datetime import datetime

def filter_by_state(list_dictionary: List[Dict], state: Optional[str]='EXECUTED') -> List[Dict]:
    """Функция, которая принимает список словарей и опционально значение
     для ключа и возвращает новый список словарей, содержащий только те словари,
      у которых ключ соответствует указанному значению."""
    list_dictionary_executed = []
    for dictionary in list_dictionary:
        if dictionary.get("state") == state:
            list_dictionary_executed.append(dictionary)
    return list_dictionary_executed


def sort_by_date(list_dictionary: List[Dict], parameter: bool=True) -> List[Dict]:
    """Функция, которая принимает список словарей и необязательный параметр,
     задающий порядок сортировки и возвращает новый список, отсортированный по дате."""
    sort_list_dictionary = sorted(list_dictionary, key=lambda i: i.get("date"), reverse=parameter)
    return sort_list_dictionary
