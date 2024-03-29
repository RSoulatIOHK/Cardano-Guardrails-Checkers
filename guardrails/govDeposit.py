# (✗ - "should") govDeposit should be adjusted in line with fiat changes

# (✓) govDeposit must not be negative

# (✓)  govDeposit must not be reduced below 1,000,000 (1 ada)

# (✓) govDeposit must not be more than 10,000,000,000,000 (10 Million ada)


def gd_01(govDeposit):
    return govDeposit >= 0

def gd_02(govDeposit):
    return govDeposit >= 1000000

def gd_03(govDeposit):
    return govDeposit <= 10000000000000

def gd_04(govDeposit, proposal, consitutions):
    return None

checkable = [
    { "name": "GD-01"
    , "description": "govDeposit must not be negative"
    , "function": gd_01
    },
    { "name": "GD-02"
    , "description": "govDeposit must not be reduced below 1,000,000 (1 ada)"
    , "function": gd_02
    },
    { "name": "GD-03"
    , "description": "govDeposit must not be more than 10,000,000,000,000 (10 Million ada)"
    , "function": gd_03
    }
]

uncheckable = [
    { "name": "GD-04"
    , "description": "govDeposit should be adjusted in line with fiat changes"
    , "function": gd_04
    }
]