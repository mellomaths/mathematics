from ast import Call
import math
from collections.abc import Callable


def lim(func: Callable[[float], float], x: float) -> float:
    test_value = 0.00001
    limits_minus = math.ceil(func(x-test_value)) 
    limits_plus = math.floor(func(x+test_value))
    if (limits_minus != limits_plus):
        return None

    return limits_minus
