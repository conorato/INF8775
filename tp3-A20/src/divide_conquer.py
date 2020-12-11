def initialize_solution(municipalities_map, bounds, nb_district):
    """
    municipalities_map: list of list of int of size n
    bounds: list of tuple (size of district, number of district of that size)
    nb_district: int representing the number of district
    """

    return divide_conquer(
        list(range(municipalities_map.shape[0])),
        list(range(municipalities_map.shape[1])),
        bounds, nb_district)


def divide_conquer(x_range, y_range, bounds, nb_district):
    if len(x_range) <= 1 or len(y_range) <= 1:
        print('nb_district: ', nb_district, 'x_range: ',
              x_range, 'y_range: ', y_range)
    else:
        divide_conquer(
            x_range[0:len(x_range)//2], y_range[0:len(y_range)//2], bounds, nb_district // 4)
        divide_conquer(
            x_range[0:len(x_range)//2], y_range[len(y_range)//2:], bounds, nb_district // 4)
        divide_conquer(
            x_range[len(x_range)//2:], y_range[0:len(y_range)//2], bounds, nb_district // 4)
        divide_conquer(
            x_range[len(x_range)//2:], y_range[len(y_range)//2:], bounds, nb_district // 4)
