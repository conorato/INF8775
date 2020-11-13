import time
import numpy as np

from utils import is_stricly_smaller, get_surface, arg_max


def execute_dyn_prog(blocs):
    s = time.time()

    path = _execute_dyn_prog(blocs)

    total_time = time.time() - s
    height = sum([bloc[0] for bloc in path])

    return path, height, total_time


def _execute_dyn_prog(blocs):
    """finds sequence of blocs in order to get the biggest tower height"""

    blocs = _order_blocs_by_decreasing_surface(blocs)

    tower_height = blocs[:, 0].copy()
    tower_sequence = [[bloc] for bloc in blocs]

    for index, bloc in enumerate(blocs):
        receiving_bloc_index = _find_bigger_bloc(
            blocs,
            bloc,
            index,
            tower_height
        )

        if receiving_bloc_index is not None:
            abs_bloc_idx = index
            abs_receiving_bloc_idx = receiving_bloc_index

            tower_height[abs_bloc_idx] = tower_height[abs_receiving_bloc_idx] + bloc[0]
            tower_sequence[abs_bloc_idx] = tower_sequence[abs_receiving_bloc_idx] + [bloc]

    tallest_tower_base_index = arg_max(tower_height)

    return tower_sequence[tallest_tower_base_index]


def _order_blocs_by_decreasing_surface(blocs):
    surface_blocs = blocs[:, 1] * blocs[:, 2]
    return blocs[np.argsort(surface_blocs)[::-1]]


def _find_bigger_bloc(blocs, bloc, index, tower_heights):
    bigger_or_equal_surface_blocs = blocs[:index]

    bigger_surface_bloc_indexes = np.argwhere(
        (bloc[1] < bigger_or_equal_surface_blocs[:, 1])
        & (bloc[2] < bigger_or_equal_surface_blocs[:, 2])
    ).flatten()

    if bigger_surface_bloc_indexes.shape[0] == 0:
        return None

    return max(
        bigger_surface_bloc_indexes,
        key=lambda i: tower_heights[i]
    )

    # return np.argmax(tower_heights[bigger_surface_bloc_indexes])
