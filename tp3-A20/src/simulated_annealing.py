import sys
import math
import random
import copy
from itertools import combinations, product

import numpy as np

from display import display
from utils import get_green_victories


def optimize_solution(districts, municipalities_map, display_solution):
    MAX_DISTANCE_IN_DISTRICT = math.ceil(
        municipalities_map.size/(2*len(districts)))
    TEMPERATURE_DECREASE = 0.95
    # display initial solution
    display(districts, municipalities_map, display_solution)
    current_green_victories = get_green_victories(
        districts, municipalities_map)
    temperature = 2
    best_green_victories = current_green_victories

    while True:
        neighbour_districts = get_random_valid_neighbour(
            districts, MAX_DISTANCE_IN_DISTRICT)

        if neighbour_districts == -1:
            return

        new_green_victories = get_green_victories(
            neighbour_districts, municipalities_map)

        if new_green_victories >= current_green_victories or random.random() < get_simulated_annealing_probability(new_green_victories, current_green_victories, temperature):
            districts = neighbour_districts
            current_green_victories = new_green_victories

        if current_green_victories > best_green_victories:
            best_green_victories = current_green_victories
            print('', flush=True)
            display(districts, municipalities_map, display_solution)

        temperature *= TEMPERATURE_DECREASE


def get_random_valid_neighbour(districts, max_distance):
    district_combinations_idxs = list(combinations(range(len(districts)), 2))
    random.shuffle(district_combinations_idxs)

    for district1_index, district2_index in district_combinations_idxs:
        municipalities_combinations_idxs = list(
            product(
                range(len(districts[district1_index])),
                range(len(districts[district2_index]))
            )
        )
        random.shuffle(municipalities_combinations_idxs)

        for municipality1_idx, municipality2_idx in municipalities_combinations_idxs:
            new_districts = swap_municipalities(
                districts, district1_index, district2_index, municipality1_idx, municipality2_idx)
            respects_manhattan_dist = all([
                maximum_manhattan_distance(
                    new_district) <= max_distance
                for new_district in new_districts
            ])
            if respects_manhattan_dist:
                return new_districts

    return -1


def swap_municipalities(districts, district1_index, district2_index, municipality1_idx, municipality2_idx):
    swapped_districts = copy.deepcopy(districts)
    district1_coordinate = swapped_districts[district1_index][municipality1_idx]

    swapped_districts[district1_index][municipality1_idx] = swapped_districts[district2_index][municipality2_idx]
    swapped_districts[district2_index][municipality2_idx] = district1_coordinate

    return swapped_districts


def maximum_manhattan_distance(district):
    # inspired from: https://www.geeksforgeeks.org/maximum-manhattan-distance-between-a-distinct-pair-from-n-coordinates/
    N = len(district)
    sums = [0 for i in range(N)]
    differences = [0 for i in range(N)]

    for i in range(N):
        sums[i] = district[i][0] + district[i][1]
        differences[i] = district[i][0] - district[i][1]

    # # Sorting both the vectors
    sums = sorted(sums)
    differences = sorted(differences)

    maximum = max(sums[-1] - sums[0], differences[-1] - differences[0])

    return maximum


def get_simulated_annealing_probability(new_green_victories, current_green_victories, temperature):
    return np.exp(-abs(new_green_victories - current_green_victories)/temperature)
