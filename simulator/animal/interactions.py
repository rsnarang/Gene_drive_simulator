import numpy.random as npr
from simulator.animal.animal import Animal
from simulator.animal import create_animal
from simulator.animal.configuration_modules import constants
import random
from dataclasses import asdict


# If the male carries gene edit, it spreads
# If the female carries, she cannot have kids, otherwise normal
def create_litter(animal_1, animal_2):
    if Animal.is_fertile(animal_1) and Animal.is_fertile(animal_2):
        number_of_newborns = npr.poisson(constants.litter_size)
        for newborn in range(number_of_newborns):
            print(create_animal.create_animal(starter=False, animal_1=animal_1, animal_2=animal_2))
    else:
        print("nothing happened")


def fight(animal_1, animal_2):
    pass


def animal_interaction(animal_1, animal_2):
    if animal_1.sex != animal_2.sex:
        create_litter(animal_1, animal_2)

    elif animal_1.sex and animal_1.sex:
        fight(animal_1, animal_2)

    else:
        pass





if __name__ == "__main__":
    population = []
    for i in range(constants.starting_population_size):
        population.append(create_animal.create_animal(starter=True).__dict__)