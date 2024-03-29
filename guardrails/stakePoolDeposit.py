# (✓) stakePoolDeposit must not be decreased below 250,000,000 (250 adaAda)

# (✓) stakePoolDeposit must not be increased above 500,000,000 (500 adaAda)

# (✓) stakePoolDeposit must not be negative


def spd_01(stakePoolDeposit):
    return stakePoolDeposit >= 250000000

def spd_02(stakePoolDeposit):
    return stakePoolDeposit <= 500000000

def spd_03(stakePoolDeposit):
    return stakePoolDeposit >= 0

checkable = [
    { "name": "SPD-01"
    , "description": "stakePoolDeposit must not be decreased below 250,000,000 (250 adaAda)"
    , "function": spd_01
    },
    { "name": "SPD-02"
    , "description": "stakePoolDeposit must not be increased above 500,000,000 (500 adaAda)"
    , "function": spd_02
    },
    { "name": "SPD-03"
    , "description": "stakePoolDeposit must not be negative"
    , "function": spd_03
    }
]

uncheckable = []