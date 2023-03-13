from simulator.animal import create_population
import pandas as pd
import numpy as np


def create_population_dataframe() -> object:
    population_dataframe = pd.DataFrame().from_dict(create_population.generate_starting_population()).set_index(
        'id_number')
    return population_dataframe
