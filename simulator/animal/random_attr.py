import numpy.random as npr
import scipy.stats as sp
import yaml
from timeit import default_timer as timer
import itertools
from dataclasses import dataclass


@dataclass()
class RandomAttr:
    stream = open("../config.yaml", "r")
    data = yaml.safe_load(stream)

    @classmethod
    def age(cls) -> int:
        starting_age = cls.data["age"][0]
        ending_age = cls.data["age"][1]
        return int(npr.uniform(starting_age, ending_age))

    @classmethod
    def weight(cls) -> int:
        pass

    @classmethod
    def sex_male(cls) -> bool:
        pass

    @classmethod
    def alive(cls) -> bool:
        pass

    @classmethod
    def gene_edit(cls) -> bool:
        pass


if __name__ == "__main__":
    start = timer()
    print(RandomAttr.age())
    end = timer()
    print(end - start)
