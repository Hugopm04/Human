from abc import ABC

class Organlle(ABC):
    def __init__(self):
        self._weight : float
        self._energy_consumption : float #In ATP/s
        self._volume : float

    