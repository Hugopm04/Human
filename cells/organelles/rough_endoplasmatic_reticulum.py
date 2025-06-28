from . import Organelle
from . import Ribosome
from . import AminoAcid

class RoughEndoplasmaticReticulum(Organelle):
    #Arbitrary values:
    WEIGHT : float = 1
    ENERGY_CONSUMPTION : float = 1
    VOLUME : float = 1

    def __init__(self, surface_area : float):
        super().__init__(RoughEndoplasmaticReticulum.WEIGHT, RoughEndoplasmaticReticulum.ENERGY_CONSUMPTION, RoughEndoplasmaticReticulum.VOLUME)
        self._surface_area = surface_area #With the idea of modelling how many ribosomes could bound
        self._bound_ribosomes : list[Ribosome] = []
        self._protein_storage : list[list[AminoAcid]] = []

    @property
    def ribosomes_bound(self) -> int:
        return(len(self._bind_ribosome))

    def _bind_ribosome(self, ribosome : Ribosome) -> None:
        self._bound_ribosomes.append(ribosome)
    
    def _store_protein(self, protein : list[AminoAcid]) -> None:
        self._protein_storage.append(protein)
    
    def _release_proteins(self) -> list[list[AminoAcid]]:
        proteins = self._protein_storage
        self._protein_storage.clear()
        return(proteins)

