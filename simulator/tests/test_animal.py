from simulator.animal import animal, constants
import pytest


class TestStartingAttr:
    def test_weight(self):
        assert type(animal.InitialPopulation.weight()) == int
        assert animal.InitialPopulation.weight() <= constants.weight_range[1]
        assert animal.InitialPopulation.weight() >= constants.weight_range[0]

    def test_sex_male(self):
        assert (type(animal.InitialPopulation.sex_male()) == bool)


class TestInitialPopulation:
    def test_starting_age(self):
        assert type(animal.InitialPopulation.starting_age()) == int
        assert animal.InitialPopulation.starting_age() <= constants.age_range[1]
        assert animal.InitialPopulation.starting_age() >= constants.age_range[0]

    def test_starting_gene_edit(self):
        assert (type(animal.InitialPopulation.starting_gene_edit()) == bool)

    def test_create_starting_animal(self):
        starting_animal = animal.InitialPopulation.create_starting_animal()
        assert len(starting_animal) == 6
        assert type(starting_animal) == dict


class TestNewBorn:
    def test_gene_edit(self):
        assert (type(animal.NewBorn.gene_edit()) == bool)

    def test_create_newborn_animal(self):
        starting_animal = animal.NewBorn.create_newborn_animal()
        assert len(starting_animal) == 6
        assert type(starting_animal) == dict
