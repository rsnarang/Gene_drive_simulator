import numpy.random as npr
import scipy.stats as sp
import yaml
import pandas as pd
import random
import itertools
from dataclasses import dataclass


@dataclass()
class RandomCharacteristics:

    @staticmethod
    def age() -> int:
        n = 1
        p = 6
        return int(sp.truncnorm.rvs(n, p))

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

x = RandomCharacteristics.age()
print(x)


class TestRandomCharacteristic():

    def test_age(self):
        assert type(RandomCharacteristics.age()) is int
        assert 1 <= RandomCharacteristics.age() <= 6

    def test_weight_type(self):
        assert type(RandomCharacteristics.weight()) is int
        assert 1 <= RandomCharacteristics.weight() <= 400




# @dataclass
# class animal:
#
#     def __post_init__(self) -> None:
#         uid = itertools.count()
#         species = "Boar"
#         age = None
#
#
#     @classmethod
#     def generate_age(cls) -> int:
#         age = npr.normal()
#         return age
#
#
# x = animal("a", 5, 3, 2, False, False)











# population = [animal() for i in range(100)]




#     def __repr__(self):
#         return repr(f"Species: {self.species}, Age: {self.age}, Weight: {self.weight},"
#                     f"Sex: {self.sex}, Alive: {self.alive}, Gene_Edit: {self.gene_edit}")
# class Boar(animal):
#     def __init__(self):
#         animal.__init__(self, "Boar")
#
#
#     # def __repr__(self):
#     #     return repr(f"Name: {self.name}, Age: {self.age}, weight: {self.weight}")
#     #
#     # def __str__(self):
#     #     return f"Name: {self.name}, Age: {self.age}, weight: {self.weight}"
#
#
# uid = [i for i in range(10)]
# weights = [int(npr.uniform(100,400)) for j in range(10)]
# age = [npr.uniform(0.5,5) for k in range(10)]
#
# dict = {'uid': uid, 'weights': weights, 'age': age}
#
# print(uid)
# print(weights)
# print(age)
#
# df = pd.DataFrame(data=dict)
# print(df)