from enum import Enum

class AminoAcid(Enum):
    ALA = ('Ala', 'A', 89.09, False, False, False, False, False, False)
    ARG = ('Arg', 'R', 174.20, True, True, False, False, False, True)
    ASN = ('Asn', 'N', 132.12, True, False, False, False, False, False)
    ASP = ('Asp', 'D', 133.10, True, False, True, False, False, False)
    CYS = ('Cys', 'C', 121.15, False, False, False, True, False, False)
    GLN = ('Gln', 'Q', 146.15, True, False, False, False, False, False)
    GLU = ('Glu', 'E', 147.13, True, False, True, False, False, False)
    GLY = ('Gly', 'G', 75.07, False, False, False, False, False, False)
    HIS = ('His', 'H', 155.16, True, True, False, False, False, True)
    ILE = ('Ile', 'I', 131.17, False, False, False, False, False, False)
    LEU = ('Leu', 'L', 131.17, False, False, False, False, False, False)
    LYS = ('Lys', 'K', 146.19, True, True, False, False, False, True)
    MET = ('Met', 'M', 149.21, False, False, False, True, False, False)
    PHE = ('Phe', 'F', 165.19, False, False, False, False, True, False)
    PRO = ('Pro', 'P', 115.13, False, False, False, False, False, False)
    SER = ('Ser', 'S', 105.09, True, False, False, False, False, False)
    THR = ('Thr', 'T', 119.12, True, False, False, False, False, False)
    TRP = ('Trp', 'W', 204.23, False, False, False, False, True, False)
    TYR = ('Tyr', 'Y', 181.19, True, False, False, False, True, False)
    VAL = ('Val', 'V', 117.15, False, False, False, False, False, False)
    STOP = ('Stop', '*', 0.00, False, False, False, False, False, False)

    def __init__(self, three_letter : str, one_letter : str, mass : float, polarity : bool, 
                 is_basic : bool, is_acidic : bool, has_sulfur : bool, is_aromatic : bool, is_essential : bool):
        
        self.three_letter = three_letter
        self.one_letter = one_letter
        self.mass = mass #En daltons
        self.polarity = polarity
        self.is_basic = is_basic
        self.is_acidic = is_acidic
        self.has_sulfur = has_sulfur
        self.is_aromatic = is_aromatic
        self.is_essential = is_essential