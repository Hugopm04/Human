from . import Organelle
from . import DNA

class Nucleus(Organelle):
    #Arbitrary values
    WEIGHT = 1
    ENERGY_CONSUMPTION = 1
    VOLUME = 1
    TRANSCRIPT_CONSUMPTION = 1

    def __init__(self, dna : DNA):
        super().__init__(Nucleus.WEIGHT, Nucleus.ENERGY_CONSUMPTION, Nucleus.VOLUME)
        self._dna = dna

    
