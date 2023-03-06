import numpy.random as npr
import pandas as pd
import random
import itertools
from dataclasses import dataclass

@dataclass
class Animal:
    species: str
    age: int
    weight: int
    sex: int
    alive: bool
    gene_edit: bool

    id_iteration = itertools.count()

    @classmethod
    def generate_uid(cls):
        uid = next(cls.id_iteration)

    @classmethod
    def generate_age(cls) -> int:
        age = npr.normal()
        return age


x = Animal("a", 5, 3, 2, False, False)
print(x.generate_uid())
# population = [Animal() for i in range(100)]




#     def __repr__(self):
#         return repr(f"Species: {self.species}, Age: {self.age}, Weight: {self.weight},"
#                     f"Sex: {self.sex}, Alive: {self.alive}, Gene_Edit: {self.gene_edit}")
# class Boar(Animal):
#     def __init__(self):
#         Animal.__init__(self, "Boar")
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