from simulator.animal import attributes
import unittest
import yaml

stream = open("../config.yaml", "r")
data = yaml.safe_load(stream)


class TestStartingAttr(unittest.TestCase):
    def test_weight(self):
        self.assertIs(type(attributes.InitialPopulation.weight()), int)
        self.assertLessEqual(attributes.InitialPopulation.weight(), data["weight"][1])
        self.assertGreaterEqual(attributes.InitialPopulation.weight(), data["weight"][0])

    def test_sex_male(self):
        self.assertIs(type(attributes.InitialPopulation.sex_male()), bool)


class TestInitialPopulation(unittest.TestCase):

    def test_starting_age(self):
        self.assertIs(type(attributes.InitialPopulation.starting_age()), int)
        self.assertLessEqual(attributes.InitialPopulation.starting_age(), data["age"][1])
        self.assertGreaterEqual(attributes.InitialPopulation.starting_age(), data["age"][0])

    def test_starting_alive(self):
        self.assertIs(type(attributes.InitialPopulation.starting_alive()), bool)

    def test_starting_gene_edit(self):
        self.assertIs(type(attributes.InitialPopulation.starting_gene_edit()), bool)


class TestNewBorn(unittest.TestCase):
    def test_age(self):
        self.assertIs(attributes.NewBorn.age() == 0)

    def test_gene_edit(self):
        self.assertIs(type(attributes.NewBorn.gene_edit()), bool)


if __name__ == '__main__':
    unittest.main()
