from simulator.animal.population import *
import pytest


class TestStarterPopulation:

    def test_generate_initial_population(self):
        assert type(StarterPopulation.generate_initial_population()) == list
        assert len(StarterPopulation.generate_initial_population()) == 100