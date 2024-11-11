"""
@version:   1.0
@author:    Виноградов Э.Н.
@copyright: 2024
"""
from argparse import ArgumentTypeError
from typing import Callable


def validate_params(type: Callable, constrain: Callable):
    def wrapper(value):
        value = type(value)
        if not constrain(value):
            raise ArgumentTypeError
        return value

    return wrapper


positive_int = validate_params(int, constrain=lambda x: x > 0)
