from simulator.animal import attributes
import pytest
import yaml

stream = open("../config.yaml", "r")
data = yaml.safe_load(stream)


class TestStartingAttr:
    def test_weight(self):
        assert type(attributes.InitialPopulation.weight()) == int
        assert attributes.InitialPopulation.weight() <= data["weight"][1]
        assert attributes.InitialPopulation.weight() >= data["weight"][0]

    def test_sex_male(self):
        assert (type(attributes.InitialPopulation.sex_male()) == bool)


class TestInitialPopulation:
    def test_starting_age(self):
        assert type(attributes.InitialPopulation.starting_age()) == int
        assert attributes.InitialPopulation.starting_age() <= data["age"][1]
        assert attributes.InitialPopulation.starting_age() >= data["age"][0]

    def test_starting_gene_edit(self):
        assert (type(attributes.InitialPopulation.starting_gene_edit()) == bool)


class TestNewBorn():
    def test_gene_edit(self):
        assert (type(attributes.NewBorn.gene_edit()) == bool)

