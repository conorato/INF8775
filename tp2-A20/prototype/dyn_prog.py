import time

from utils import is_stricly_smaller, get_surface, arg_max


def execute_dyn_prog(blocs):
    s = time.time()

    path = _execute_dyn_prog(blocs)

    total_time = time.time() - s
    height = sum([bloc[0] for bloc in path])

    return path, height, total_time


def _execute_dyn_prog(blocs):
    """finds sequence of blocs in order to get the biggest tower height"""
    blocs.sort(key=get_surface, reverse=True)

    tower_height = [bloc[0] for bloc in blocs]
    tower_sequence = [[bloc] for bloc in blocs]

    current_threshold_index = 0
    while current_threshold_index != len(blocs):
        current_blocs = blocs[current_threshold_index:]

        for index, bloc in enumerate(current_blocs):
            receiving_bloc_index = _find_bigger_bloc(
                current_blocs, bloc, index)

            if receiving_bloc_index is not None:
                abs_bloc_idx = current_threshold_index + index
                abs_receiving_bloc_idx = current_threshold_index + receiving_bloc_index

                tower_height[abs_bloc_idx] = tower_height[abs_receiving_bloc_idx] + bloc[0]
                tower_sequence[abs_bloc_idx] = tower_sequence[abs_receiving_bloc_idx] + [bloc]
            else:
                next_threshold_index = current_threshold_index + index

        current_threshold_index = next_threshold_index + 1

    tallest_tower_base_index = arg_max(tower_height)

    return tower_sequence[tallest_tower_base_index]


def _find_bigger_bloc(blocs, bloc, index):
    bigger_surface_bloc_indexes = [
        idx
        for idx, receiving_bloc in enumerate(blocs[:index])
        if is_stricly_smaller(bloc, receiving_bloc)
    ]

    if len(bigger_surface_bloc_indexes) == 0:
        return None

    highest_tower_idx = max(
        bigger_surface_bloc_indexes, key=lambda i: blocs[i])

    return highest_tower_idx
