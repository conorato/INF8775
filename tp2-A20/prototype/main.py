"""
Finds sequence of blocs in order to get the biggest tower height, while respecting the following condition:
width_newbloc < width_receivingbloc and depth_newbloc < depth_receivingbloc
Where a bloc is defined by its (height, width, depth) (which corresponds to (hauteur, longueur, profondeur))
"""
import argparse
import random
import math
import sys
import time
import csv

from greedy import execute_greedy
from dyn_prog import execute_dyn_prog
from tabou import execute_tabou


def get_options():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-a', '--algo', choices=['vorace', 'progdyn', 'tabou'], required=True)
    parser.add_argument('-e', '--exemplaires',
                        help='path to points file', required=True)
    parser.add_argument('-p', '--path', help='affiche les blocs utilisés dans la construction de la tour chacun sur une ligne (hauteur, largeur, profondeur) en commençant par le bas.',
                        default=False, action='store_true')
    parser.add_argument('-r', '--resultats',
                        help='affiche la hauteur de la tour', default=False, action='store_true')
    parser.add_argument('-t', '--temps', help='affiche le temps d’exécution en ms',
                        default=False, action='store_true')

    args = parser.parse_args()

    return args


def read_blocs_from_file(filename):
    with open(filename, 'r') as f:
        nb_points = f.readline()
        points = [[int(n) for n in line.split()] for line in f]

    return nb_points, points


def main(algo, file, print_path=False, print_height=False, print_time=False):
    nb_blocs, blocs = read_blocs_from_file(file)

    if algo == "vorace":
        path, height, time = execute_greedy(blocs)

    elif algo == "progdyn":
        path, height, time = execute_dyn_prog(blocs)

    elif algo == "tabou":
        path, height, time = execute_tabou(blocs)

    if print_time:
        print(time * 1000)  # display in ms

    if print_path:
        print(path)

    if print_height:
        print(height)

    return time


if __name__ == '__main__':
    args = get_options()

    main(args.algo, args.exemplaires, args.path, args.resultats, args.temps)
