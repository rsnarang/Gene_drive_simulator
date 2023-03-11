from simulator.animal import attributes, constants, create_animal
import pytest


def test_create_initial_population():
    initial_population = create_animal.create_initial_population(constants.starting_population_size)
    assert type(initial_population) == list
    assert len(initial_population) == constants.starting_population_size


def test_size_of_each_element_in_initial_population():
    initial_population = create_animal.create_initial_population(constants.starting_population_size)
    assert len(initial_population[1]) == 6
