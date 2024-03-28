#!/usr/bin/env python3

from typing import Union, Tuple

def compute_square(item: str, number:Union[int, float]) -> Tuple[str, float]:
    number = float(number)
    return ((item, number*number))