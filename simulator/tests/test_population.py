from simulator.animal.population import *
import pytest


class TestStarterPopulation:

    def test_generate_initial_population(self):
        population = StarterPopulation.generate_initial_population()
        assert type(population) == list
        assert len(population) == constants.starting_population_size
