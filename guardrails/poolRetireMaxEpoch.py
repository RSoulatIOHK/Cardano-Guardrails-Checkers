def prme_01(poolRetireMaxEpoch, proposal, constitutions):
    return poolRetireMaxEpoch >= 1

def prme_02(poolRetireMaxEpoch):
    return poolRetireMaxEpoch >= 0

checkable = [
    { "name": "PRME-02"
    , "description": "poolRetireMaxEpoch must not be negative"
    , "function": prme_02
    }
]

uncheckable = [
    { "name": "PRME-01"
    , "description": "poolRetireMaxEpoch must not be lower than 1"
    , "function": prme_01
    }
]