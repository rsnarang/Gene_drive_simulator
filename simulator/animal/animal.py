import numpy.random as npr
from simulator.animal import constants
from timeit import default_timer as timer
import itertools
from dataclasses import dataclass


@dataclass
class StartingAttr:
    id_iter = itertools.count()
    id = next(id_iter)
    alive = True

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

    @classmethod
    def create_starting_animal(cls) -> dict:
        starting_animal = {
            "id": cls.id,
            "alive": cls.alive,
            "weight": cls.weight(),
            "sex_male": cls.sex_male(),
            "gene_edit": cls.starting_gene_edit(),
            "age": cls.starting_age()
        }
        return starting_animal


# These functions are for all newborns
class NewBorn(StartingAttr):
    age = 0

    @staticmethod
    def gene_edit():
        if npr.binomial(1, constants.gene_edite_rate) == 1:
            return True
        else:
            return False

    @classmethod
    def create_newborn_animal(cls) -> dict:
        starting_animal = {
            "id": cls.id,
            "alive": cls.alive,
            "weight": cls.weight(),
            "sex_male": cls.sex_male(),
            "gene_edit": cls.gene_edit(),
            "age": cls.age
        }
        return starting_animal


if __name__ == "__main__":
    start = timer()
    print(InitialPopulation.create_starting_animal())
    print(NewBorn.create_newborn_animal())
    end = timer()
    print(end - start)
