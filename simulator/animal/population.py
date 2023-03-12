from simulator.animal.animal import Animal
from simulator.animal import constants
from dataclasses import dataclass
import numpy.random as npr
from timeit import default_timer as timer
import pandas as pd


def generate_starting_population(size: int = constants.starting_population_size) -> dict:
    for i in range(size):
        yield StarterAnimal().animal


def generate_newborn() -> dict:
    for i in range(newborns_survival()):
        yield NewbornAnimal().animal


def create_population_dataframe() -> object:
    population_dataframe = pd.DataFrame().from_dict(generate_starting_population()).set_index('id')
    newborn_dataframe = pd.DataFrame().from_dict(generate_newborn()).set_index('id')
    return pd.concat([population_dataframe, newborn_dataframe])


def male_to_male_interaction() -> int:
    return npr.binomial(1, 0.5)


def number_of_male_to_female_interaction() -> int:
    return npr.poisson(1)


def number_of_litters_per_female() -> int:
    number_of_litters = npr.poisson(1.5)
    return number_of_litters


def newborns_survival(newborns) -> int:
    survived = npr.binomial(newborns, constants.newborn_survival_rate)
    return survived


if __name__ == "__main__":
    start = timer()
    print(create_population_dataframe())
    end = timer()
    print(end - start)
