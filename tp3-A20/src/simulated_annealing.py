import sys
import math

from display import display


def optimize_solution(districts, municipalities_map, display_solution):
    MAX_DISTANCE_IN_DISTRICT = math.ceil(
        municipalities_map.size/(2*len(districts)))
    # display initial solution
    display(districts, municipalities_map, display_solution)

    while True:
        neighbour = get_random_valid_neighbour(
            districts, MAX_DISTANCE_IN_DISTRICT)
        print('\n')
        display(districts, municipalities_map, display_solution)
        if neighbour == -1:
            return


# def get_random_valid_neighbour(districts, max_distance):
#     districts = districts.copy()
#     district_idxs = set(range(len(districts)))
#     respects_manhattan_dist = False

#     while not respects_manhattan_dist and len(district_idxs) > 0:
#         selected_district_idxs = sample(district_idxs, 2)
#         selected_districts = districts[selected_district_idxs]

#         while not respects_manhattan_dist:
#             district1_coordinate_idx = sample(
#                 range(len(selected_districts[0])))
#             district2_coordinate_idx = sample(
#                 range(len(selected_districts[1])))

#             district1_coordinate = selected_districts[0][district1_coordinate_idx]
#             selected_districts[0][district1_coordinate_idx] = selected_districts[1][district2_coordinate_idx]
#             selected_districts[1][district2_coordinate_idx] = district1_coordinate
#

#         district_idxs -= set(selected_district_idxs)

def get_random_valid_neighbour(districts, max_distance):
    for district1_index in range(len(districts) - 1):
        for district2_index in range(1, len(districts)):
            for municipality1_idx in range(len(districts[district1_index])):
                for municipality2_idx in range(len(districts[district2_index])):
                    new_districts = swap_municipalities(
                        districts, district1_index, district2_index, municipality1_idx, municipality2_idx)
                    respects_manhattan_dist = (
                        maximum_manhattan_distance(
                            new_districts[district1_index]) <= max_distance
                        and maximum_manhattan_distance(
                            new_districts[district2_index]) <= max_distance)
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
