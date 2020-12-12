import argparse
import random
import sys
import math

import numpy as np


from invalid_naive_algo import invalid_naive_algo
from initialize_solution import initialize_solution
from simulated_annealing import optimize_solution


def get_options():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-c', '--circonscriptions', help='Nombre de circonscriptions à former', type=int, required=True)
    parser.add_argument(
        '-e', '--exemplaires', help="Chemin absolu vers le fichier d'exemplaire", required=True)
    parser.add_argument(
        '-p', '--solution', help='Affiche les municipalités qui composent circonscription',
        default=False, action='store_true')

    args = parser.parse_args()

    return args


def read_municipalities_map_from_file(municipalities_map_path):
    with open(municipalities_map_path, 'r') as f:
        f.readline()
        municipalities = [[int(n) for n in line.split()] for line in f]

    return np.array(municipalities)


def get_upper_lower_distrinct_bounds(municipalities_map, nb_district):
    nb_municipalities_per_district = municipalities_map.size / nb_district
    lower_bound = math.floor(nb_municipalities_per_district)
    upper_bound = math.ceil(nb_municipalities_per_district)
    upper_bound_districts = 0
    lower_bound_districts = 0

    if (nb_municipalities_per_district - lower_bound > 0.5):
        upper_bound_districts = (
            nb_municipalities_per_district - lower_bound)
        lower_bound_districts = (
            1 - upper_bound_districts)
    else:
        lower_bound_districts = (
            upper_bound - nb_municipalities_per_district)
        upper_bound_districts = (
            1 - lower_bound_districts)

    lower_bound_districts *= nb_district
    lower_bound_districts = round(lower_bound_districts)
    upper_bound_districts *= nb_district
    upper_bound_districts = round(upper_bound_districts)

    # print(
    #     f'lower_bound_districts: {lower_bound_districts}, of district size: {lower_bound}')
    # print(
    #     f'upper_bound_districts: {upper_bound_districts}, of district size: {upper_bound}')

    return [(lower_bound, lower_bound_districts), (upper_bound, upper_bound_districts)]


def main(nb_district, municipalities_map_path, display_solution=False):
    municipalities_map = read_municipalities_map_from_file(
        municipalities_map_path)
    bounds = get_upper_lower_distrinct_bounds(municipalities_map, nb_district)

    districts = initialize_solution(municipalities_map, bounds, nb_district)
    optimize_solution(districts, municipalities_map, display_solution)


if __name__ == '__main__':
    args = get_options()

    main(args.circonscriptions, args.exemplaires, args.solution)
