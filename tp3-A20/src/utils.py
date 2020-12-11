import numpy as np


def convert_index_to_position(idx, shape):
    return (idx // shape[0], idx % shape[0])


def distance(idx_1, idx_2, shape):
    point_1 = np.array(convert_index_to_position(idx_1, shape))
    point_2 = np.array(convert_index_to_position(idx_2, shape))

    return np.sum(np.abs(point_1 - point_2))
