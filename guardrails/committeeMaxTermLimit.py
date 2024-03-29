# (✓) committeeMaxTermLimit must not be zero or negative

# (✓) committeeMaxTermLimit must not be less than 18 epochs (90 days, or approximately 3 months)

# (✓) committeeMaxTermLimit must not be more than 293 epochs (approximately 4 years)

# (✗ - "should") committeeMaxTermLimit should not be more than 220 epochs (approximately 3 years)

def cmtl_01(committeeMaxTermLimit):
    return committeeMaxTermLimit > 0

def cmtl_02(committeeMaxTermLimit):
    return committeeMaxTermLimit >= 18

def cmtl_03(committeeMaxTermLimit):
    return committeeMaxTermLimit <= 293

def cmtl_04(committeeMaxTermLimit, proposal, constitutions):
    return committeeMaxTermLimit <= 220

checkable = [
    { "name": "CMTL-01"
    , "description": "committeeMaxTermLimit must not be zero or negative"
    , "function": cmtl_01
    },
    { "name": "CMTL-02"
    , "description": "committeeMaxTermLimit must not be less than 18 epochs (90 days, or approximately 3 months)"
    , "function": cmtl_02
    },
    { "name": "CMTL-03"
    , "description": "committeeMaxTermLimit must not be more than 293 epochs (approximately 4 years)"
    , "function": cmtl_03
    }
]

uncheckable = [
    { "name": "CMTL-04"
    , "description": "committeeMaxTermLimit should not be more than 220 epochs (approximately 3 years)"
    , "function": cmtl_04
    }
]