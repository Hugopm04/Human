from . import Organelle
from . import AminoAcid

class Ribosome(Organelle):
    TO_AMINOACID = {
        # Fenilalanina
        'UUU': AminoAcid.PHE, 'UUC': AminoAcid.PHE,
        # Leucina
        'UUA': AminoAcid.LEU, 'UUG': AminoAcid.LEU,
        'CUU': AminoAcid.LEU, 'CUC': AminoAcid.LEU, 'CUA': AminoAcid.LEU, 'CUG': AminoAcid.LEU,
        # Isoleucina
        'AUU': AminoAcid.ILE, 'AUC': AminoAcid.ILE, 'AUA': AminoAcid.ILE,
        # Metionina (start)
        'AUG': AminoAcid.MET,
        # Valina
        'GUU': AminoAcid.VAL, 'GUC': AminoAcid.VAL, 'GUA': AminoAcid.VAL, 'GUG': AminoAcid.VAL,
        # Serina
        'UCU': AminoAcid.SER, 'UCC': AminoAcid.SER, 'UCA': AminoAcid.SER, 'UCG': AminoAcid.SER,
        'AGU': AminoAcid.SER, 'AGC': AminoAcid.SER,
        # Prolina
        'CCU': AminoAcid.PRO, 'CCC': AminoAcid.PRO, 'CCA': AminoAcid.PRO, 'CCG': AminoAcid.PRO,
        # Treonina
        'ACU': AminoAcid.THR, 'ACC': AminoAcid.THR, 'ACA': AminoAcid.THR, 'ACG': AminoAcid.THR,
        # Alanina
        'GCU': AminoAcid.ALA, 'GCC': AminoAcid.ALA, 'GCA': AminoAcid.ALA, 'GCG': AminoAcid.ALA,
        # Tirosina
        'UAU': AminoAcid.TYR, 'UAC': AminoAcid.TYR,
        # Histidina
        'CAU': AminoAcid.HIS, 'CAC': AminoAcid.HIS,
        # Glutamina
        'CAA': AminoAcid.GLN, 'CAG': AminoAcid.GLN,
        # Asparagina
        'AAU': AminoAcid.ASN, 'AAC': AminoAcid.ASN,
        # Lisina
        'AAA': AminoAcid.LYS, 'AAG': AminoAcid.LYS,
        # Ácido aspártico
        'GAU': AminoAcid.ASP, 'GAC': AminoAcid.ASP,
        # Ácido glutámico
        'GAA': AminoAcid.GLU, 'GAG': AminoAcid.GLU,
        # Cisteína
        'UGU': AminoAcid.CYS, 'UGC': AminoAcid.CYS,
        # Triptófano
        'UGG': AminoAcid.TRP,
        # Arginina
        'CGU': AminoAcid.ARG, 'CGC': AminoAcid.ARG, 'CGA': AminoAcid.ARG, 'CGG': AminoAcid.ARG,
        'AGA': AminoAcid.ARG, 'AGG': AminoAcid.ARG,
        # Glicina
        'GGU': AminoAcid.GLY, 'GGC': AminoAcid.GLY, 'GGA': AminoAcid.GLY, 'GGG': AminoAcid.GLY,
        # Codones stop
        'UAA': AminoAcid.STOP, 'UAG': AminoAcid.STOP, 'UGA': AminoAcid.STOP
    }

    #Arbitrary values:
    WEIGHT : float = 1
    ENERGY_CONSUMPTION : float = 1
    VOLUME : float = 1

    def __init__(self):
        super().__init__(Ribosome.WEIGHT, Ribosome.ENERGY_CONSUMPTION, Ribosome.VOLUME)
        self._bound_mrna : str = None
        self._protein_product : list[str] = []
        self._position : int = 0
        self._working : bool = False
    
    @property
    def working(self) -> bool:
        return self._working

    def _bind(self, mrna : str) -> None:
        self._bound_mrna = mrna
        self._position = 0
        self._protein_product = []
        self._working = True

    def _translate_step(self) -> None:
        if self._bound_mrna == None:
            self._stop_working()
            return

        if self._position + 3 > len(self._bound_mrna):
            self._stop_working()
            return

        #Check this works!
        codon : str = self._bound_mrna[self._position:self._position + 3]
        aminoacid : AminoAcid = Ribosome.TO_AMINOACID[codon]
        self._position += 3

        if aminoacid == AminoAcid.STOP:
            self._stop_working()
        else:
            self._protein_product.append(aminoacid)

    def _translate_all(self) -> list[AminoAcid]:
        while self.working:
            self._translate_step()
        return self._protein_product

    def _release(self) -> list[AminoAcid]:
        protein : list[AminoAcid] = self._protein_product
        self.__init__() #Resets ribosome (CAUTION IF CHANGING INIT FUNCTION)
        return protein

    def _stop_working(self) -> None:
        self._working = False