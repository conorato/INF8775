from tabou import _get_height_to_remove

import numpy as np

current_solution = np.array([[1, 9, 9], [1, 8, 8], [10, 7, 7], [
                            1, 6, 6], [1, 5, 5], [10, 4, 4], [2, 3, 3]])
candidate = np.array([4, 2, 8])

print(_get_height_to_remove(current_solution, candidate))
