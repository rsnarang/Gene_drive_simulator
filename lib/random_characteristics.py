from pathlib import WindowsPath

import numpy.random as npr
import scipy.stats as sp
import yaml
import itertools
from dataclasses import dataclass

config = yaml.safe_load(config.yaml)

@dataclass()
class RandomAttr:

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


