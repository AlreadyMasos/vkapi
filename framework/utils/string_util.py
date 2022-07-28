from random import choice
from string import ascii_letters


def set_random_string():
    random_string = (''.join(choice(ascii_letters) for i in range(15)))
    return random_string


def validate_timer_string(string, current_string):
    return string == current_string


def validate_card(card_num, real_card_num):
    return card_num in real_card_num
