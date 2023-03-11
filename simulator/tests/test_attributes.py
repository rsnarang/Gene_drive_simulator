from simulator.animal import attributes, constants
import pytest


class TestStartingAttr:
    def test_weight(self):
        assert type(attributes.InitialPopulation.weight()) == int
        assert attributes.InitialPopulation.weight() <= constants.weight_range[1]
        assert attributes.InitialPopulation.weight() >= constants.weight_range[0]

    def test_sex_male(self):
        assert (type(attributes.InitialPopulation.sex_male()) == bool)


class TestInitialPopulation:
    def test_starting_age(self):
        assert type(attributes.InitialPopulation.starting_age()) == int
        assert attributes.InitialPopulation.starting_age() <= constants.age_range[1]
        assert attributes.InitialPopulation.starting_age() >= constants.age_range[0]

    def test_starting_gene_edit(self):
        assert (type(attributes.InitialPopulation.starting_gene_edit()) == bool)


class TestNewBorn:
    def test_gene_edit(self):
        assert (type(attributes.NewBorn.gene_edit()) == bool)

