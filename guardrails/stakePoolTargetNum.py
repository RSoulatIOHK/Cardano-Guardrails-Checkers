# (✓) stakePoolTargetNum must not be set below 250

# (✓) stakePoolTargetNum must not be set above 2,000

def sptn_01(stakePoolTargetNum):
    return stakePoolTargetNum >= 250

def sptn_02(stakePoolTargetNum):
    return stakePoolTargetNum <= 2000

checkable = [
    { "name": "SPTN-01"
    , "description": "stakePoolTargetNum must not be set below 250"
    , "function": sptn_01
    },
    { "name": "SPTN-02"
    , "description": "stakePoolTargetNum must not be set above 2,000"
    , "function": sptn_02
    }
]

uncheckable = []