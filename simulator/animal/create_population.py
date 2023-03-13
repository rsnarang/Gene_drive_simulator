from simulator.animal.configuration_modules import constants
from simulator.animal import create_animal
from simulator.animal import interactions
import numpy.random as npr
import numpy as np
import pandas as pd
import random


def generate_starting_population(size: int = constants.starting_population_size):
    for i in range(size):
        yield create_animal.create_animal(starter=True).__dict__


def number_of_male_to_female_interaction_for_each_male() -> int:
    return npr.poisson(2)


def newborns_survival(newborns) -> int:
    survived = npr.binomial(newborns, constants.newborn_survival_rate)
    return survived


def separate_population_by_gender():
    males = []
    females = []
    size = 10
    for animal in generate_starting_population():
        if animal.get('sex'):
            males.append(animal)
        else:
            females.append(animal)

    return males, females


def shuffle_animals_create_pairs(males, females):
    population = males + females
    print(population)

def split_pairs(population, n):
    pairs = np.array_split(population, n)
    print(pairs)

if __name__ == "__main__":
    # males, females = separate_population_by_gender()
    # shuffle_animals_create_pairs(males, females)
    population = []
    for animal in generate_starting_population():
        population.append(animal)
    random.shuffle(population)

    split_pairs(population, len(population)/2)





