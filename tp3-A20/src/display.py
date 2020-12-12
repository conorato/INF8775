import numpy as np


def display(districts, municipalities_map, display_solution):
    if display_solution:
        _display_districts(districts)
    else:
        _print_green_victories(districts, municipalities_map)


def _display_districts(districts):
    for district in districts:
        print(*[f'{municipality[1]} {municipality[0]}' for municipality in district])


def _print_green_victories(districts, municipalities_map):
    district_won_by_green = 0
    for district in districts:
        x_municipalities = [municipality_idx[0]
                            for municipality_idx in district]
        y_municipalities = [municipality_idx[1]
                            for municipality_idx in district]
        votes_per_municipalities = municipalities_map[y_municipalities,
                                                      x_municipalities]
        total_votes_for_green = np.sum(votes_per_municipalities)
        total_votes = 100 * len(district)
        if (total_votes_for_green / total_votes > 0.5):
            district_won_by_green += 1

    print(district_won_by_green)
