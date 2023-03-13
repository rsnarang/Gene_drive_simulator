from simulator.animal import animal
from simulator.animal.configuration_modules import constants, set_trait


def gene_edit_condition(starter, sex, animal_1=None, animal_2=None) -> bool:
    if starter and sex:
        return set_trait.trait_function['gene_edit'](constants.starting_gene_edit_rate)

    elif not starter:
        animal_1 = animal_1
        animal_2 = animal_2
        if animal_1.gene_edit or animal_2.gene_edit:
            return set_trait.trait_function['gene_edit'](constants.newborn_gene_edit_rate)

    else:
        return False


def generate_traits(starter, animal_1=None, animal_2=None) -> tuple:
    sex = set_trait.trait_function['sex'](constants.sex_rate)
    life_span = int(round(set_trait.trait_function['life_span'](constants.lifespan)))
    weight = int(round(set_trait.trait_function['weight'](constants.weight_range)))

    if starter:
        age = int(round(set_trait.trait_function['age'](constants.starting_age_range)))
        if life_span <= age:
            age -= constants.lifespan[1]
        gene_edit = gene_edit_condition(starter, sex=sex)

    else:
        age = 0
        gene_edit = gene_edit_condition(starter, sex=sex, animal_1=animal_1, animal_2=animal_2)

    return tuple([age, life_span, weight, sex, gene_edit])


def create_animal(starter, animal_1=None, animal_2=None) -> object:
    if starter:
        traits = generate_traits(starter=True)
        return animal.Animal(*traits)

    elif not starter:
        traits = generate_traits(starter, animal_1=animal_1, animal_2=animal_2)
        return animal.Animal(*traits)

# if __name__ == "__main__":
#     for i in range(10):
#         print(create_animal(starter=True))