# (✓) stakeAddressDeposit must not be decreased below 1,000,000 (1 adaAda)

# (✓) stakeAddressDeposit must not be increased above 5,000,000 (5 adaAda)

# (✓) stakeAddressDeposit must not be negative

def sad_01(stakeAddressDeposit):
    return stakeAddressDeposit >= 1000000

def sad_02(stakeAddressDeposit):
    return stakeAddressDeposit <= 5000000

def sad_03(stakeAddressDeposit):
    return stakeAddressDeposit >= 0

checkable = [
    { "name": "SAD-01"
    , "description": "stakeAddressDeposit must not be decreased below 1,000,000 (1 adaAda)"
    , "function": sad_01
    },
    { "name": "SAD-02"
    , "description": "stakeAddressDeposit must not be increased above 5,000,000 (5 adaAda)"
    , "function": sad_02
    },
    { "name": "SAD-03"
    , "description": "stakeAddressDeposit must not be negative"
    , "function": sad_03
    }
]

uncheckable = []