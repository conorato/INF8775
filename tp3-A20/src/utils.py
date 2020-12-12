import math
import numpy as np


def convert_index_to_position(idx, shape):
    return (idx // shape[0], idx % shape[0])


def distance(idx_1, idx_2, shape):
    point_1 = convert_index_to_position(idx_1, shape)
    point_2 = convert_index_to_position(idx_2, shape)

    return abs(point_1[0] - point_2[0]) + abs(point_1[1] - point_2[1])


def is_district_full(district_idx, districts, bounds):
    is_lower_bound = district_idx < bounds[0][1]
    if is_lower_bound:
        return len(districts[district_idx]) == bounds[0][0]

    return len(districts[district_idx]) == bounds[1][0]


def get_green_victories(districts, municipalities_map):
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

    return district_won_by_green


def check_inner_district_distances(solution, n, m):
    """Extracted from check_sol.py"""
    for (district, district_index) in zip(solution, range(len(solution))):
        for precinct1_index in range(len(district) - 1):
            for precinct2_index in range(precinct1_index + 1, len(district)):
                if (abs(district[precinct1_index][0] - district[precinct2_index][0]) + abs(district[precinct1_index][1] - district[precinct2_index][1])) > math.ceil(n/2/m):
                    return (district_index, precinct1_index, precinct2_index)

    return 0
