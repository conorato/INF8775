import numpy as np

from utils import get_green_victories


def display(districts, municipalities_map, display_solution):
    if display_solution:
        _display_districts(districts)
    else:
        _print_green_victories(districts, municipalities_map)


def _display_districts(districts):
    for district in districts:
        print(*[f'{municipality[1]} {municipality[0]}' for municipality in district])


def _print_green_victories(districts, municipalities_map):
    print(get_green_victories(districts, municipalities_map))
