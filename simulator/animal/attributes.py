import numpy.random as npr
import scipy.stats as sp
import yaml
from timeit import default_timer as timer
import itertools
from dataclasses import dataclass


@dataclass
class StartingAttr:
    stream = open("../config.yaml", "r")
    data = yaml.safe_load(stream)
    id_iter = itertools.count()
    alive = True

    def __post_init__(self):
        self.id = next(self.id_iter)

    @classmethod
    def weight(cls) -> int:
        starting_weight = cls.data["weight"][0]
        ending_weight = cls.data["weight"][1]
        return int(npr.uniform(starting_weight, ending_weight))

    @classmethod
    def sex_male(cls) -> bool:
        if npr.binomial(1, 0.5) == 0:
            return True
        else:
            return False

    # These functions are only for initializing our
    # simulation based on yaml config


class InitialPopulation(StartingAttr):
    @classmethod
    def starting_age(cls) -> int:
        starting_age = cls.data["age"][0]
        ending_age = cls.data["age"][1]
        return int(npr.uniform(starting_age, ending_age))

    @classmethod
    def starting_gene_edit(cls) -> bool:
        if npr.binomial(1, 0.1) == 0:
            return True
        else:
            return False

    # These functions are for all newborns
    # based on yaml configs


class NewBorn(StartingAttr):

    age = 0

    @classmethod
    def gene_edit(cls):
        if npr.binomial(1, cls.data["gene_edit_rate"]) == 1:
            return True
        else:
            return False


if __name__ == "__main__":
    start = timer()
    for i in range(10):
        print(NewBorn.gene_edit())
    end = timer()
    print(end - start)
