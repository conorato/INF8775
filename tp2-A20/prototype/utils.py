def is_stricly_smaller(bloc, receiving_bloc):
    return bloc[1] < receiving_bloc[1] and bloc[2] < receiving_bloc[2]


def get_surface(bloc):
    return bloc[1] * bloc[2]


def arg_max(l):
    def f(i): return l[i]
    return max(range(len(l)), key=f)
