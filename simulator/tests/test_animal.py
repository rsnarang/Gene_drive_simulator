from simulator.animal import create_animal


class TestCreate:
    def test_create_starter_animal(self):
        assert type(create_animal.create_starter_animal(1)) == dict
        assert weight() <= constants.weight_range[1]
        assert weight() >= constants.weight_range[0]

    def test_sex_male(self):
        assert (type(sex_male()) == bool)


class TestStarterAnimal:
    def test_starting_age(self):
        assert type(starting_age()) == int
        assert starting_age() <= constants.age_range[1]
        assert starting_age() >= constants.age_range[0]


class TestNewBornAnimal:
    def test_gene_edit(self):
        assert (type(gene_edit()) == bool)
