from simulator.animal import animal, constants
import pytest


class TestAnimal:
    def test_weight(self):
        assert type(animal.StarterAnimal.weight()) == int
        assert animal.StarterAnimal.weight() <= constants.weight_range[1]
        assert animal.StarterAnimal.weight() >= constants.weight_range[0]

    def test_sex_male(self):
        assert (type(animal.StarterAnimal.sex_male()) == bool)


class TestStarterAnimal:
    def test_starting_age(self):
        assert type(animal.StarterAnimal.starting_age()) == int
        assert animal.StarterAnimal.starting_age() <= constants.age_range[1]
        assert animal.StarterAnimal.starting_age() >= constants.age_range[0]

    def test_create_starting_animal(self):
        starting_animal = animal.StarterAnimal.create_starting_animal()
        assert len(starting_animal) == 6
        assert type(starting_animal) == dict


class TestNewBornAnimal:
    def test_gene_edit(self):
        assert (type(animal.NewbornAnimal.gene_edit()) == bool)

    def test_create_newborn_animal(self):
        starting_animal = animal.NewbornAnimal.create_newborn_animal()
        assert len(starting_animal) == 6
        assert type(starting_animal) == dict
