from typing import Self

class Human():
    def __init__(self, name : str, father : Self, mother : Self, sons : list[Self]):
        self._name : str = name
        self._father : Self = father
        self._mother : Self = mother
        self._sons : list[Self] = sons
    pass