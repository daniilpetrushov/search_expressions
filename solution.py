from itertools import product
from typing import List

EVAL_RESULT = 200
SEARCH_DIGITS = "9876543210"

def search_expressions() -> List[str]:
    """
        Ищет всевозможные варианты выражений, результат которых равняется 200,
        которые можно получить подставляя '+', '-', '' в промежутки между цифр от 9 до 0.
    """
    result_list: List[str] = []
    # Т.к. имеем 9 промежутков между цифрами, воспользуемся декартовым произведением,
    # чтобы получить всевозможные варианты знаков.
    for combination in product(["+", "-", ""], repeat=len(SEARCH_DIGITS) - 1):
        # Расположим очередной вариант знаков в наше выражение.
        expression = "".join(digit + sign for digit, sign in zip(SEARCH_DIGITS, combination)) + SEARCH_DIGITS[-1]
        # Если результат выражения удовлетворяет условию, запомним его.
        if eval(expression) == EVAL_RESULT:
            result_list.append(expression)
    return result_list

print(search_expressions())
