# (✓) maxCollateralInputs must not be reduced below 1

def mci_01(maxCollateralInputs):
    return maxCollateralInputs >= 1

checkable = [
    { "name": "MCI-01"
    , "description": "maxCollateralInputs must not be reduced below 1"
    , "function": mci_01
    }
]

uncheckable = [
]