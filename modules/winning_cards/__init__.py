import re


def nb_winning_cards(card: str) -> int:
    list_numbers = card.split(':')[1].split('|')
    winning_num = set(re.findall(r"(\d+)", list_numbers[0]))
    my_num = set(re.findall(r"(\d+)", list_numbers[1]))
    return len(winning_num & my_num)
