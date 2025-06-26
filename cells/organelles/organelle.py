from abc import ABC

class Organelle(ABC):
    def __init__(self, weight : float, energy_consumption : float, volume : float):
        self._weight : float = weight
        self._energy_consumption : float = energy_consumption #In ATP/s
        self._volume : float = volume