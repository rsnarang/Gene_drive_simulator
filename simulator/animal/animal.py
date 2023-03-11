import numpy.random as npr
from simulator.animal import constants
from timeit import default_timer as timer
import itertools
from dataclasses import dataclass


@dataclass
class StartingAttr:
    id_iter = itertools.count()

    @staticmethod
    def weight() -> int:
        return int(npr.uniform(*constants.weight_range))

    @staticmethod
    def sex_male() -> bool:
        return npr.binomial(1, 0.5) == 0

    @classmethod
    def create_animal(cls) -> dict:
        return {
            "id": next(cls.id_iter),
            "alive": True,
            "sex_male": cls.sex_male(),
            "weight": cls.weight()
        }


# These functions are only for initializing our starting population
class StarterAnimal(StartingAttr):
    @staticmethod
    def starting_age() -> int:
        return int(npr.uniform(*constants.age_range))

    @staticmethod
    def starting_gene_edit() -> bool:
        return npr.binomial(1, 0.1) == 0

    @classmethod
    def create_starting_animal(cls) -> dict:
        return cls.create_animal() | {
            "gene_edit": cls.starting_gene_edit(),
            "age": cls.starting_age()
        }


# These functions are for all Newborn Animals
class NewbornAnimal(StartingAttr):
    age = 0

    @staticmethod
    def gene_edit() -> bool:
        return npr.binomial(1, constants.gene_edit_rate) == 1

    @classmethod
    def create_newborn_animal(cls) -> dict:
        return cls.create_animal() | {
            "gene_edit": cls.gene_edit(),
            "age": cls.age
        }


if __name__ == "__main__":
    start = timer()
    for i in range(100):
        print(StarterAnimal.create_starting_animal())

    end = timer()
    print(end - start)
