"""
Slightly modified to take the required command line arguments
[Source]: https://github.com/AliceB08/closest_points
"""
import argparse
import random
import math
import sys
import time
import csv

from brute_force import execute_brute_force
from DpR import execute_DpR


def get_options():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-a', '--algo', choices=['brute', 'recursif', 'seuil'], required=True)
    parser.add_argument('-e', '--exemplaires',
                        help='path to points file', required=True)
    parser.add_argument('-p', '--petite-dist',
                        help='affiche la plus petite distance entre deux points', default=False, action='store_true')
    parser.add_argument('-t', '--temps', help='affiche le temps d’exécution en ms',
                        default=False, action='store_true')

    args = parser.parse_args()

    return args


def read_points_from_file(filename):
    with open(filename, 'r') as f:
        nb_points = f.readline()
        points = [[int(n) for n in line.split()] for line in f]

    return nb_points, points


'''
--------------------------------------------------------------------
ATTENTION : Dans votre code vous devez utiliser le générateur gen.py
pour générer des points. Vous devez donc modifier ce code pour importer
les points depuis les fichiers générés.
De plus, vous devez faire en sorte que l'interface du tp.sh soit
compatible avec ce code (par exemple l'utilisation de flag -e, -a, (p et -t)).
--------------------------------------------------------------------
 '''


def main(algo, file, print_distance=False, print_time=False):
    nb_points, POINTS = read_points_from_file(file)
    sorted_points_x = sorted(POINTS, key=lambda x: x[0])
    sorted_points_y = sorted(POINTS, key=lambda x: x[1])

    if algo == "brute":
        distance, time = execute_brute_force(sorted_points_x)

    elif algo == "recursif":
        SEUIL_DPR = 3   # choisi arbitrairement
        distance, time = execute_DpR(
            sorted_points_x, sorted_points_y, SEUIL_DPR)

    elif algo == "seuil":
        SEUIL_DPR = 8   # choisi par essai-erreur
        distance, time = execute_DpR(
            sorted_points_x, sorted_points_y, SEUIL_DPR)

    if print_time:
        print(time * 1000)  # display in ms

    if print_distance:
        print(distance)

    return time


if __name__ == '__main__':
    args = get_options()

    main(args.algo, args.exemplaires, args.petite_dist, args.temps)
