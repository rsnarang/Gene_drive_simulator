import numpy.random as npr
import scipy.stats as scistat
from simulator.animal import constants
from timeit import default_timer as timer
import itertools
from dataclasses import dataclass, asdict, field


@dataclass
class Animal:
    uid = itertools.count()

    gene_edit: bool

    def __post_init__(self):
        self.animal_id = next(self.uid)
        self.alive = True
        self.age = self.set_age()
        self.sex_male = self.set_sex_male()
        self.lifespan = self.set_lifespan()
        self.weight = self.set_weight()

    @staticmethod
    def set_weight() -> int:
        return int(scistat.truncnorm.rvs(*constants.weight_range))

    @staticmethod
    def set_sex_male() -> bool:
        return npr.binomial(1, 0.5) < 0.5

    @staticmethod
    def set_lifespan() -> int:
        return int(scistat.truncnorm.rvs(*constants.lifespan))

    @staticmethod
    def set_age() -> int:
        return int(scistat.truncnorm.rvs(*constants.starting_age_range))

    def is_starter_animal(self) -> bool:
        return self.animal_id <= constants.starting_population_size

    def is_male_starter_animal(self) -> bool:
        return self.is_starter_animal() and self.sex_male

    def is_fertile(self) -> bool:
        if self.age < 5:

            if self.sex_male:
                return True

            elif not self.sex_male and not self.gene_edit:
                return True

            else:
                return False


def evaluate_starter_gene_edit() -> bool:
    return npr.binomial(1, constants.starting_gene_edit) > 0.5


def evaluate_gene_edit() -> bool:
    return npr.binomial(1, constants.gene_edit_rate) > 0.5


def create_starting_animal() -> object:
    if evaluate_starter_gene_edit():
        return Animal(True)
    else:
        return Animal(False)


def is_parent_gene_edit(animal_1, animal_2) -> bool:
    return animal_1.gene_edit or animal_2.gene_edit


def create_newborn(animal_1, animal_2):
    if is_parent_gene_edit(animal_1, animal_2):
        if evaluate_gene_edit():
            return Animal(True)
        else:
            return Animal(False)
    else:
        return Animal(False)


# If the male carries gene edit, it spreads
# If the female carries, she cannot have kids, otherwise normal
# def create_litter(animal_1: object, animal_2: object) -> None:
#     if animal_1.is_fertile() and animal_2.is_fertile():
#         number_of_newborns = npr.poisson(5)
#         for newborn in number_of_newborns:
#             create_newborn(animal_1, animal_2)
#
#
# def fight(animal_1, animal_2):
#     return max(animal_1["weight"], animal_2["weight"])
#
#
# def animal_interaction(animal_1, animal_2) -> None:
#     genders = get_gender()
#     if animal_1["sex_male"] != animal_2["sex_male"]:
#         create_litter(animal_1, animal_2)
#
#     elif animal_1["sex_male"] and animal_2["sex_male"] is True:
#         fight(animal_1, animal_2)
#
#     else:
#         pass


if __name__ == "__main__":
    start = timer()
    for i in range(10):
        print("starter:")
        print(create_starting_animal())
        print("newborn")
        print(create_newborn(Animal(False), Animal(True)))
    end = timer()
    print(end - start)
