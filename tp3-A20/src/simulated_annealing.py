import sys
import math
import random

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

            print('\n')
            display(districts, municipalities_map, display_solution)

        temperature *= TEMPERATURE_DECREASE


def get_random_valid_neighbour(districts, max_distance):
    # instead, generate all combination tuples of districts, then do same for municipality
    # sample([(district1_index, district2_index) for district2_index in range(1, len(districts)) for district1_index in range(len(districts) - 1)], n*(n-1))
    # sherwood

    for district1_index in range(len(districts) - 1):
        for district2_index in range(1, len(districts)):
            for municipality1_idx in range(len(districts[district1_index])):
                for municipality2_idx in range(len(districts[district2_index])):
                    new_districts = swap_municipalities(
                        districts, district1_index, district2_index, municipality1_idx, municipality2_idx)
                    respects_manhattan_dist = all(
                        maximum_manhattan_distance(
                            new_district) <= max_distance
                        for new_district in new_districts
                    )
                    if respects_manhattan_dist:
                        return new_districts
    return -1


def swap_municipalities(districts, district1_index, district2_index, municipality1_idx, municipality2_idx):
    districts = districts.copy()
    district1_coordinate = districts[district1_index][municipality1_idx]

    districts[district1_index][municipality1_idx] = districts[district2_index][municipality2_idx]
    districts[district2_index][municipality2_idx] = district1_coordinate

    return districts


def maximum_manhattan_distance(district):
    # inspired from: https://www.geeksforgeeks.org/maximum-manhattan-distance-between-a-distinct-pair-from-n-coordinates/
    N = len(district)
    sums = [0 for i in range(N)]
    differences = [0 for i in range(N)]

    for i in range(N):
        sums[i] = district[i][0] + district[i][1]
        differences[i] = district[i][0] - district[i][1]

    # Sorting both the vectors
    sums.sort()
    differences.sort()

    maximum = max(sums[-1] - sums[0], differences[-1] - differences[0])

    return maximum


def get_simulated_annealing_probability(new_green_victories, current_green_victories, temperature):
    return np.exp(-abs(new_green_victories - current_green_victories)/temperature)
