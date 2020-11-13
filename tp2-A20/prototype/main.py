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
import numpy as np
import time


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
        blocs = [[int(n) for n in line.split()] for line in f]

    return np.array(blocs)


def main(algo, file, print_path=False, print_height=False, print_time=False):
    blocs = read_blocs_from_file(file)

    if algo == "vorace":
        path, total_time = execute_greedy(blocs)

    elif algo == "progdyn":
        s = time.time()
        path = execute_dyn_prog(blocs)
        total_time = time.time() - s

    elif algo == "tabou":
        path, height, total_time = execute_tabou(blocs)

    if print_time:
        print(total_time * 1000)  # display in ms

    if print_path:
        print(*path, sep='\n')

    if print_height:
        print(np.array(path)[:, 0].sum())

    return time


if __name__ == '__main__':
    args = get_options()

    main(args.algo, args.exemplaires, args.path, args.resultats, args.temps)
