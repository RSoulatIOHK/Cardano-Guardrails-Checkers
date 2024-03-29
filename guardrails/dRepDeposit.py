# (✗ - "should") dRepDeposit should be adjusted in line with fiat changes

# (✓) dRepDeposit must not be negative

# (✓) dRepDeposit  must not be reduced below 1,000,000 (1 ada)

# (✓) dRepDeposit must be no more than 100,000,000,000 (100,000 ada)

def drd_01(dRepDeposit):
    return dRepDeposit >= 0

def drd_02(dRepDeposit):
    return dRepDeposit >= 1000000

def drd_03(dRepDeposit):
    return dRepDeposit <= 100000000000

def drd_04(dRepDeposit, proposal, constitutions):
    return None

checkable = [
    { "name": "DRD-01"
    , "description": "dRepDeposit must not be negative"
    , "function": drd_01
    },
    { "name": "DRD-02"
    , "description": "dRepDeposit must not be reduced below 1,000,000 (1 ada)"
    , "function": drd_02
    },
    { "name": "DRD-03"
    , "description": "dRepDeposit must be no more than 100,000,000,000 (100,000 ada)"
    , "function": drd_03
    }
]

uncheckable = [
    { "name": "DRD-04"
    , "description": "dRepDeposit should be adjusted in line with fiat changes"
    , "function": drd_04
    }
]

