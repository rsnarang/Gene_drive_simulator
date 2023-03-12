from simulator.animal.animal import Animal, StarterAnimal, NewbornAnimal
from simulator.animal import constants
from dataclasses import dataclass
from timeit import default_timer as timer


def generate_animal() -> object:
    return StarterAnimal().animal


population = []


def generate_starting_population(size: int = constants.starting_population_size) -> []:
    for i in range(size):
        animal = generate_animal()
        population.append(animal)


if __name__ == "__main__":
    start = timer()
    generate_starting_population()
    end = timer()
    print(end - start)
