from simulator.animal.animal import StarterAnimal, NewbornAnimal
from simulator.animal import constants
from dataclasses import dataclass
from timeit import default_timer as timer


@dataclass
class StarterPopulation:

    @staticmethod
    def generate_initial_population() -> []:
        population = []
        for i in range(constants.starting_population_size):
            population.append(StarterAnimal.create_starting_animal())
        return population

    @staticmethod
    def generate_newborn_population() -> dict:
        pass


if __name__ == "__main__":
    start = timer()
    print(StarterPopulation.generate_initial_population())
    end = timer()
    print(end - start)
