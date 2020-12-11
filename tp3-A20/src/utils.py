import math
import numpy as np


def convert_index_to_position(idx, shape):
    return (idx // shape[0], idx % shape[0])


def distance(idx_1, idx_2, shape):
    point_1 = np.array(convert_index_to_position(idx_1, shape))
    point_2 = np.array(convert_index_to_position(idx_2, shape))

    return np.sum(np.abs(point_1 - point_2))


def is_district_full(district_idx, districts, bounds):
    is_lower_bound = district_idx < bounds[0][1]
    if is_lower_bound:
        return len(districts[district_idx]) == bounds[0][0]

    return len(districts[district_idx]) == bounds[1][0]


def check_inner_district_distances(solution, n, m):
    """Extracted from check_sol.py"""
    for (district, district_index) in zip(solution, range(len(solution))):
        for precinct1_index in range(len(district) - 1):
            for precinct2_index in range(precinct1_index + 1, len(district)):
                if (abs(district[precinct1_index][0] - district[precinct2_index][0]) + abs(district[precinct1_index][1] - district[precinct2_index][1])) > math.ceil(n/2/m):
                    return (district_index, precinct1_index, precinct2_index)

    return 0
