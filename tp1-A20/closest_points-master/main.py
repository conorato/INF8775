import argparse
import random
import math
import sys
import time
import csv

from brute_force import execute_brute_force
from DpR import execute_DpR
from utils import GRID_SIZE


def get_options():
    parser = argparse.ArgumentParser()
    parser.add_argument('--algo', help='either BF, DPR_ELEM and DPR_EXP')
    parser.add_argument('--nb_points')
    parser.add_argument('--file')

    args = parser.parse_args()
    print("Chosen arguments are: ", args.algo, args.nb_points, args.file)

    return args

def read_points_from_file(filename):
    with open(filename, 'r') as f:
        nb_points = f.readline()
        points = [[int(n) for n in line.split()] for line in f]

    return nb_points, points

'''
Un point est représenté par un tuple (position_x, position_y)
La fonction generate_points génère une liste de N points.
'''
def generate_points(N):
    points = [(random.randint(0, GRID_SIZE), random.randint(0, GRID_SIZE)) for i in range(N)]
    return points

'''
--------------------------------------------------------------------
ATTENTION : Dans votre code vous devez utiliser le générateur gen.py
pour générer des points. Vous devez donc modifier ce code pour importer
les points depuis les fichiers générés.
De plus, vous devez faire en sorte que l'interface du tp.sh soit
compatible avec ce code (par exemple l'utilisation de flag -e, -a, (p et -t)).
--------------------------------------------------------------------
 '''

def main(algo=None, nb_points=0, file=None):

    if file != None:
        nb_points, POINTS = read_points_from_file(file)
    else:
        nb_points = int(nb_points)
        POINTS = generate_points(nb_points)

    sorted_points_x = sorted(POINTS, key=lambda x: x[0])
    sorted_points_y = sorted(POINTS, key=lambda x: x[1])

    if algo == "BF":
        time_BF = execute_brute_force(sorted_points_x)
        print("Temps : ", time_BF)

    elif algo == "DPR_ELEM":
        SEUIL_DPR = 3
        time_DPR = execute_DpR(sorted_points_x, sorted_points_y, SEUIL_DPR)
        print("Temps : ", time_DPR)

    elif algo == "DPR_EXP":
        SEUIL_DPR = 10
        time_DPR = execute_DpR(sorted_points_x, sorted_points_y, SEUIL_DPR)
        print("Temps : ", time_DPR)

    else:
        time_BF = execute_brute_force(sorted_points_x)
        print("Temps : ", time_BF)
        time_DPR = execute_DpR(sorted_points_x, sorted_points_y, 3)
        print("Temps : ", time_DPR)
        time_DPR = execute_DpR(sorted_points_x, sorted_points_y, 10)
        print("Temps : ", time_DPR)



if __name__ == '__main__':
    args = get_options()

    main(args.algo, args.nb_points, args.file)
