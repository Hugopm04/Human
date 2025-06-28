from . import Organelle

class SmoothEndoplasmaticReticulum(Organelle):
    
    #Arbitrary values:
    WEIGHT : float = 1
    ENERGY_CONSUMPTION : float = 1
    VOLUME : float = 1
    
    def __init__(self):
        super().__init__(SmoothEndoplasmaticReticulum.WEIGHT, SmoothEndoplasmaticReticulum.ENERGY_CONSUMPTION, SmoothEndoplasmaticReticulum.VOLUME)
        self._lipid_synthesis_rate