"""Greedy algorithm for the following problem:
Finds sequence of blocs in order to get the biggest tower height, while respecting the following condition:
width_newbloc < width_receivingbloc and depth_newbloc < depth_receivingbloc
Where a bloc is defined by its (height, width, depth) (which corresponds to (hauteur, longueur, profondeur))
"""
import time
import numpy as np
from utils import is_stricly_smaller


def execute_greedy(blocs):
    s = time.time()

    path = _execute_greedy(blocs)

    total_time = time.time() - s

    return path, total_time


def _execute_greedy(blocs):
    """finds sequence of blocs in order to get the biggest tower height"""
    path = []

    # order blocs by their decreasing surface to height ratio
    surface_height_blocs = blocs[:, 0] * blocs[:, 1] * blocs[:, 2]
    blocs = blocs[np.argsort(surface_height_blocs)[::-1]]

    path.append(blocs[0])

    for bloc in blocs[1:]:
        receiving_bloc = path[-1]
        if is_stricly_smaller(bloc, receiving_bloc):
            path.append(bloc)

    return path


def _get_height_surface_ratio(bloc):
    return bloc[0] * bloc[1] * bloc[2]
    # return bloc[1] * bloc[2]
