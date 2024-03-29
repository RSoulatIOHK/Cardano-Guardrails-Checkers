# (✓) collateralPercentage must not be reduced below 100

# (✓) collateralPercentage must not be set above 200

# (✓) collateralPercentage must not be negative or zero

def cp_01(collateralPercentage):
    return collateralPercentage >= 100

def cp_02(collateralPercentage):
    return collateralPercentage <= 200

def cp_03(collateralPercentage):
    return collateralPercentage > 0

checkable = [
    { "name": "CP-01"
    , "description": "collateralPercentage must not be reduced below 100"
    , "function": cp_01
    },
    { "name": "CP-02"
    , "description": "collateralPercentage must not be set above 200"
    , "function": cp_02
    },
    { "name": "CP-03"
    , "description": "collateralPercentage must not be negative or zero"
    , "function": cp_03
    }
]

uncheckable = [
]