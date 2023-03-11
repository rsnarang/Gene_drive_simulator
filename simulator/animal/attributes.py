import numpy.random as npr
from simulator.animal import constants
from timeit import default_timer as timer
import itertools
from dataclasses import dataclass


@dataclass
class StartingAttr:
    id_iter = itertools.count()

    def __post_init__(self):
        self.id = next(self.id_iter)
        self.alive = True

    @staticmethod
    def weight() -> int:
        return int(npr.uniform(*constants.weight_range))

    @staticmethod
    def sex_male() -> bool:
        if npr.binomial(1, 0.5) == 0:
            return True
        else:
            return False

# These functions are only for initializing our
# simulation based on yaml config
class InitialPopulation(StartingAttr):
    @staticmethod
    def starting_age() -> int:
        return int(npr.uniform(*constants.age_range))

    @staticmethod
    def starting_gene_edit() -> bool:
        if npr.binomial(1, 0.1) == 0:
            return True
        else:
            return False

# These functions are for all newborns
class NewBorn(StartingAttr):

    def __post_init__(self):
        self.age = 0

    @staticmethod
    def gene_edit():
        if npr.binomial(1, constants.gene_edite_rate) == 1:
            return True
        else:
            return False


if __name__ == "__main__":
    start = timer()
    print(StartingAttr)
    end = timer()
    print(end - start)
