from enum import Enum

class Lipid(Enum):
    PHOSPHATIDYLCHOLINE = {
        "mass": 760,  # Da
        "saturation": "mixed",
        "charge": 0,
        "role": "membrane"
    }
    CHOLESTEROL = {
        "mass": 386,
        "saturation": "unsaturated",
        "charge": 0,
        "role": "membrane fluidity"
    }
    TRIGLYCERIDE = {
        "mass": 885,
        "saturation": "variable",
        "charge": 0,
        "role": "energy storage"
    }
