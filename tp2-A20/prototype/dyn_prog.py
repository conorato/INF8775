import time

from utils import is_stricly_smaller


def execute_dyn_prog(blocs):
    s = time.time()

    path = _execute_dyn_prog(blocs)

    total_time = time.time() - s
    height = sum([bloc[0] for bloc in path])

    return path, height, total_time


def _execute_dyn_prog(blocs):
    """finds sequence of blocs in order to get the biggest tower height"""
    path = []
    blocs.sort(key=_get_surface, reverse=True)

    # computation array (each tower starts with its own height)
    tower_height = [bloc[0] for bloc in blocs]
    # side array to keep sequence (each tower starts with its own index)
    tower_sequence = [[bloc] for bloc in blocs]

    def _find_bigger_bloc(bloc, index):
        bigger_or_equal_surface_blocs = blocs[:index]
        bigger_surface_bloc_indexes = [
            idx
            for idx, receiving_bloc in enumerate(bigger_or_equal_surface_blocs)
            if is_stricly_smaller(bloc, receiving_bloc)
        ]

        if len(bigger_surface_bloc_indexes) == 0:
            return None

        highest_tower_idx = max(
            bigger_surface_bloc_indexes, key=lambda i: blocs[i])

        return highest_tower_idx

    current_threshold_index = 0
    # while len(blocs[current_threshold_index:]) > 0:
    for index, bloc in enumerate(blocs[current_threshold_index:]):

        # index += current_threshold_index
        receiving_bloc_index = _find_bigger_bloc(bloc, index)
        print(f'index {index} has receiving: {receiving_bloc_index}')
        if receiving_bloc_index is not None:
            tower_height[index] = tower_height[receiving_bloc_index] + bloc[0]
            tower_sequence[index].append(blocs[receiving_bloc_index])
        else:
            threshold_index = index

        # current_threshold_index = threshold_index + 2
    # tmp += 1

    tallest_tower_base_index = _arg_max(tower_height)

    return tower_sequence[tallest_tower_base_index]


def _get_surface(bloc):
    return bloc[1] * bloc[2]


def _arg_max(l):
    def f(i): return l[i]
    return max(range(len(l)), key=f)
