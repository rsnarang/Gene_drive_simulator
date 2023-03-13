import numpy.random as npr


def ranged_characteristics(range_tuple: tuple) -> int:
    characteristic = npr.normal(loc=range_tuple[0], scale=range_tuple[3])
    if characteristic <= range_tuple[1]:
        return range_tuple[1]
    elif characteristic >= range_tuple[2]:
        return range_tuple[2]
    else:
        return characteristic


def binary_characteristic(rate) -> bool:
    return npr.binomial(1, rate) == 1


trait_function = {**dict.fromkeys(['weight', 'age', 'life_span'], ranged_characteristics),
                  **dict.fromkeys(['sex', 'gene_edit'], binary_characteristic)}
