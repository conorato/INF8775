import numpy as np
from random import sample

from utils import convert_index_to_position, distance


def initialize_solution(municipalities_map, bounds, nb_district):
    districts = [[] for _ in range(nb_district)]

    return _init_solution_k_means(districts, municipalities_map, bounds, nb_district)


def is_district_full(district_idx, districts, bounds):
    is_lower_bound = district_idx < bounds[0][1]
    if is_lower_bound:
        return len(districts[district_idx]) == bounds[0][0]

    return len(districts[district_idx]) == bounds[1][0]


def _init_solution_k_means(districts, municipalities_map, bounds, nb_district):
    # transform to 1D
    municipalities_map = municipalities_map.copy()
    municipalities_map_shape = municipalities_map.shape
    municipalities_map = municipalities_map.reshape(-1)
    unassigned_municipalities = set(range(municipalities_map.shape[0]))

    # choose k centers from the dataset at random
    centers = sample(unassigned_municipalities, nb_district)
    for district, center in zip(districts, centers):
        district.append(center)
    unassigned_municipalities -= set(centers)

    # for each point, compute the distance to its nearest cluster center
    for municipality in unassigned_municipalities:
        district_indexes_ordered_by_dist = np.argsort([
            distance(municipality, center, municipalities_map_shape) for center in centers
        ])
        district_indexes_ordered_by_dist = [
            district_idx for district_idx in district_indexes_ordered_by_dist
            if not is_district_full(district_idx, districts, bounds)
        ]
        districts[district_indexes_ordered_by_dist[0]].append(municipality)

    return [
        [convert_index_to_position(idx, municipalities_map_shape)
         for idx in district]
        for district in districts
    ]
