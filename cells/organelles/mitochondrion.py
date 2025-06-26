from . import Organelle
from . import DNA

class Mitochondrion(Organelle):
    #Arbitrary values:
    WEIGHT : float = 1
    ENERGY_CONSUMPTION : float = 1
    VOLUME : float = 1

    def __init__(self, apt_production_rate : float, oxygen_consumption_rate : float, 
                 inner_membrane_surface_area : float, dna : DNA):
        
        super().__init__(Mitochondrion.WEIGHT, Mitochondrion.ENERGY_CONSUMPTION, Mitochondrion.VOLUME)
        self._atp_production_rate : float = apt_production_rate # ATP produced each second
        self._oxygen_consumption_rate : float = oxygen_consumption_rate # Oxygen consumed each second
        self._inner_membrane_surface_area : float = inner_membrane_surface_area #Surface for Energy production in either nm^2 or um^2
        self._dna : DNA = dna #Mitochondria have their own dna.
        self._working = True
    
