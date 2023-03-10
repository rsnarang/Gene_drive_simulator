import numpy.random as npr
import scipy.stats as sp
import yaml
import itertools
from dataclasses import dataclass

stream = open("../../config.yaml", "r")
data = yaml.safe_load(stream)
print(data["age"])

@dataclass()
class RandomAttr:

    @staticmethod
    def age() -> int:
        starting_age = data["age"][0]
        ending_age = data["age"][1]
        return int(npr.uniform(starting_age, ending_age))

    @staticmethod
    def weight(self) -> int:
        pass

    @staticmethod
    def sex_male(self) -> bool:
        pass

    @staticmethod
    def alive(self) -> bool:
        pass

    @staticmethod
    def gene_edit(self) -> bool:
        pass