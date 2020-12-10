import argparse
import random
import sys

import numpy as np


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


def main(nb_district, municipalities_map_path, display_solution=False):
    municipalities_map = read_municipalities_map_from_file(
        municipalities_map_path)
    print(municipalities_map)


if __name__ == '__main__':
    args = get_options()

    main(args.circonscriptions, args.exemplaires, args.solution)
