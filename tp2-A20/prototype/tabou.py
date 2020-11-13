from collections import deque
import numpy as np

STOP_CRITERIA = 100


def execute_tabou(blocs):
    path = _execute_tabou(blocs)

    return path


def _execute_tabou(candidates):
    current_solution = deque()
    current_solution_height = 0
    best_solution = None
    tabous = []

    nb_iter_without_improvement = 0

    while nb_iter_without_improvement < STOP_CRITERIA:
        current_candidate, current_solution_height = _get_candidate(
            candidates,
            current_solution,
            current_solution_height
        )
        current_solution, imcompatible_blocs = _update_solution(
            current_candidate,
            current_solution
        )
        tabous, candidates = _update_tabous(
            imcompatible_blocs,
            tabous,
            candidates
        )

        if is_current_solution_better(current_solution, best_solution):
            best_solution = current_solution
            nb_iter_without_improvement = 0
        else:
            nb_iter_without_improvement += 1

    return best_solution


def _get_candidate(candidates, current_solution, current_solution_height):
    """step 1: determine the candidate which maximises current solution's height"""
    best_candidate = None
    best_candidate_tower_height = 0

    for candidate in candidates:
        height_to_remove = _get_height_to_remove(current_solution, candidate)
        candidate_tower_height = (
            current_solution_height + candidate[0] - height_to_remove
        )

        if candidate_tower_height > best_candidate_tower_height:
            best_candidate = candidate
            best_candidate_tower_height = candidate_tower_height

    return best_candidate, best_candidate_tower_height


def _get_height_to_remove(current_solution, candidate):
    """step 1: needs to be linear time"""
    bigger_width_indexes = current_solution[:, 1] >= candidate[1]
    bigger_depth_indexes = current_solution[:, 2] > candidate[2]

    return ((bigger_width_indexes ^ bigger_depth_indexes)*current_solution[:, 0]).sum()


def _update_solution(candidate, current_solution):
    """step 2: updates current solution and finds which blocs are incompatible with new candidate"""
    updated_solution = current_solution.copy()
    imcompatible_blocs = []

    return updated_solution, imcompatible_blocs


def _update_tabous(new_tabous, tabous):
    """
    step 3: we transfer these incompatible blocs into the tabou list while associating a time to live
    step 4: we update the time to live of blocs in the tabou list and transfer the elements with 0 TTL to C
    """
    updated_tabous = tabous.copy()

    updated_candidates = _update_time_to_live()
    updated_tabous = _add_new_tabous()

    return updated_tabous, updated_candidates


def _update_time_to_live():
    return []


def _add_new_tabous():
    return []


def is_current_solution_better(current_solution, best_solution):
    return False
