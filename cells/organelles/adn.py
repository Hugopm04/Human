
class ADN():
    ADN_COMPLEMENTS : dict[str][str] = {
        "A" : "T",
        "T" : "A",
        "C" : "G",
        "G" : "C"
    }
    RNA_COMPLEMENTS : dict[str][str] = {
        "A" : "U",
        "T" : "A",
        "C" : "G",
        "G" : "C"
    }

    def __init__(self, coding_strand : str):
        self._coding_strand : str = coding_strand.upper()
        self._template_strand : str = ADN._generate_template_strand(self.coding)
        self._rna_strand : str = ADN._generate_arn_strand(self.template)

    @property
    def coding(self) -> str:
        return self._coding_strand

    @property
    def template(self) -> str:
        return self._template_strand
    
    @property
    def rna(self) -> str:
        return self._rna_strand

    @staticmethod
    def _generate_template_strand(coding_strand : str) -> str:
        template = ""
        for base in coding_strand:
            template += ADN.ADN_COMPLEMENTS[base]
        
        #In reverse order
        return(template[::-1])

    @staticmethod
    def _generate_arn_strand(template_strand : str) -> str:
        rna = ""
        for base in template_strand:
            rna += ADN.RNA_COMPLEMENTS[base]
        return(rna)

