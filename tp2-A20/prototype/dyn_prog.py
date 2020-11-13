import numpy as np
from numba import jit


@jit(nopython=True)
def execute_dyn_prog(blocs):
    path = _execute_dyn_prog(blocs)

    return path


@jit(nopython=True)
def _execute_dyn_prog(blocs):
    """finds sequence of blocs in order to get the biggest tower height"""

    blocs = _order_blocs_by_decreasing_surface(blocs)

    tower_height = blocs[:, 0].copy()
    tower_sequence = [[bloc] for bloc in blocs]

    for index, bloc in enumerate(blocs):
        receiving_bloc_index = _find_tallest_possible_tower(
            blocs,
            bloc,
            index,
            tower_height
        )

        if receiving_bloc_index != -1:
            tower_height[index] = tower_height[receiving_bloc_index] + bloc[0]
            tower_sequence[index] = tower_sequence[receiving_bloc_index] + [bloc]

    tallest_tower_base_index = np.argmax(tower_height)

    return tower_sequence[tallest_tower_base_index]


@jit(nopython=True)
def _order_blocs_by_decreasing_surface(blocs):
    surface_blocs = blocs[:, 1] * blocs[:, 2]
    return blocs[np.argsort(surface_blocs)[::-1]]


@jit(nopython=True)
def _find_tallest_possible_tower(blocs, bloc, index, tower_heights):
    bigger_or_equal_surface_blocs = blocs[:index]

    bigger_surface_bloc_indexes = np.argwhere(
        (bloc[1] < bigger_or_equal_surface_blocs[:, 1])
        & (bloc[2] < bigger_or_equal_surface_blocs[:, 2])
    ).flatten()

    if bigger_surface_bloc_indexes.shape[0] == 0:
        return -1

    # we find the index of the bigger_surface_bloc_indexes which has the tallest tower
    # and we return the corresponding element of bigger_surface_bloc_indexes
    return bigger_surface_bloc_indexes[
        np.argmax(tower_heights[bigger_surface_bloc_indexes])
    ]
