from simulator.animal.animal import Animal, StarterAnimal, NewbornAnimal
from simulator.animal import constants
from dataclasses import dataclass
import numpy.random as npr
from timeit import default_timer as timer


def generate_animal() -> object:
    return StarterAnimal().animal


population = []


def generate_starting_population(size: int = constants.starting_population_size) -> []:
    for i in range(size):
        animal = generate_animal()
        population.append(animal)


def male_to_male_interaction():
    return npr.binomial(1, 0.5)


def number_of_male_to_female_interaction():
    return npr.poisson(1)


def newborns_per_litter() -> int:
    newborns = npr.poisson(5)
    return newborns

def litter_per_female() -> int:
    litter = npr.poisson(1.5)
    return litter

def newborns_survival(newborns) -> int:
    survived = npr.binomial(newborns, constants.newborn_survival_rate)
    return survived

if __name__ == "__main__":
    start = timer()
    end = timer()
    print(end - start)
