import numpy.random as npr
from simulator.animal import constants
from timeit import default_timer as timer
import itertools
from dataclasses import dataclass


@dataclass
class Animal:
    id_iter = itertools.count()

    def __post_init__(self):
        self.animal = {"id": next(self.id_iter),
                       "alive": True,
                       "weight": self.weight(),
                       "sex_male": self.sex_male()
                       }

    @staticmethod
    def weight() -> int:
        return int(npr.uniform(*constants.weight_range))

    @staticmethod
    def sex_male() -> bool:
        return npr.binomial(1, 0.5) == 0

    def is_male(self) -> bool:
        return self.animal["sex_male"]


# These functions are only for initializing our starting population
class StarterAnimal(Animal):
    def __init__(self):
        super().__init__()
        self.animal = self.animal | {
            "starting_age": self.starting_age(),
            "starting_gene_edit": self.starting_gene_edit()
        }

    @staticmethod
    def starting_age() -> int:
        return int(npr.uniform(*constants.age_range))

    def starting_gene_edit(self) -> bool:
        if self.is_male():
            return npr.binomial(1, 0.1) == 1
        else:
            return False


# These functions are for all Newborn Animals
class NewbornAnimal(Animal):
    def __init__(self):
        super().__init__()
        self.animal = self.animal | {
            "starting_age": 0,
            "starting_gene_edit": self.gene_edit()
        }

    @staticmethod
    def gene_edit() -> bool:
        return npr.binomial(1, constants.gene_edit_rate) == 1


if __name__ == "__main__":
    start = timer()
    for i in range(100):
        print(StarterAnimal().animal)
    end = timer()
    print(end - start)
