import numpy as np
from random import sample

from utils import convert_index_to_position, distance, is_district_full


def initialize_solution(municipalities_map, bounds, nb_district):
    return _init_solution_k_means(municipalities_map, bounds, nb_district)


def _init_solution_k_means(municipalities_map, bounds, nb_district):
    # transform to 1D
    new_centers = None
    municipalities_map = municipalities_map.copy()
    municipalities_map_shape = municipalities_map.shape
    municipalities_map = municipalities_map.reshape(-1)
    unassigned_municipalities = set(range(municipalities_map.shape[0]))

    # choose k centers from the dataset at random
    centers = _choose_random_centers(unassigned_municipalities, nb_district)
    unassigned_municipalities -= set(centers)

    # for each point, compute the distance to its nearest cluster center
    while new_centers == None or old_centers != centers:
        districts = _assign_municipalities_according_centers(
            unassigned_municipalities, centers, nb_district, bounds, municipalities_map_shape)
        old_centers = centers
        centers = _update_centers(districts, municipalities_map_shape)
        print('updated centers to: ', centers)
    return [
        [convert_index_to_position(idx, municipalities_map_shape)
         for idx in district]
        for district in districts
    ]


def _choose_random_centers(unassigned_municipalities, nb_district):
    centers = sample(unassigned_municipalities, nb_district)
    return centers


def _assign_municipalities_according_centers(unassigned_municipalities, centers, nb_district, bounds, shape):
    districts = [[] for _ in range(nb_district)]

    for district, center in zip(districts, centers):
        district.append(center)

    for municipality in unassigned_municipalities:
        district_indexes_ordered_by_dist = np.argsort([
            distance(municipality, center, shape) for center in centers
        ])
        district_indexes_ordered_by_dist = [
            district_idx for district_idx in district_indexes_ordered_by_dist
            if not is_district_full(district_idx, districts, bounds)
        ]
        districts[district_indexes_ordered_by_dist[0]].append(municipality)

    return districts


def _update_centers(districts, shape):
    return [_get_center(district, shape) for district in districts]


def _get_center(district, shape):
    """list of ints"""
    positions = [convert_index_to_position(
        municipality, shape) for municipality in district]
    center_2d = np.round(np.mean(positions, axis=0))
    return int(center_2d[0] * shape[0] + center_2d[1])
