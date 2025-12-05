from src.masks import get_mask_account, get_mask_card_number

def mask_account_card(account: str) -> str:
    """Функция, которая умеет обрабатывать информацию как о картах, так и о счетах."""
    if account.startswith("Счет"):
        account_number = account[5:]
        return f"Счет {get_mask_account(account_number)}"
    else:
        name_card_number = account[:-17]
        account_card_number = account[-16:]
        return f"{name_card_number} {get_mask_card_number(account_card_number)}"


def get_date(date: str) -> str:
    """Функция, которая принимает на вход строку с датой в одном формате и возвращает в другом"""
    part_date = date[0:10]
    correct_date = part_date[-2:] + "." + part_date[-5:-3] + "." + part_date[0:4]
    return correct_date
