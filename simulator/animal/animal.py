import itertools
from dataclasses import dataclass, asdict, field
from typing import ClassVar


@dataclass
class Animal:
    id_number = itertools.count()

    age: int
    life_span: int
    weight: int
    sex: bool
    gene_edit: bool
    alive: bool = field(init=False, repr=False)

    def __post_init__(self):
        self.id_number = next(self.id_number)
        self.alive = True

    def is_fertile(self) -> bool:
        if self.sex:
            return True

        elif not self.sex and not self.gene_edit:
            return True

        else:
            return False

    def update_age_and_alive(self) -> None:
        self.age += 1
        if self.age > self.life_span:
            self.alive = False
