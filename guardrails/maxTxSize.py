# (⧗ - no access to existing parameter values) maxTxSize must not be decreased
# (⧗ - no access to existing parameter values) maxTxSize must not exceed maxBlockBodySize minus maxBlockHeaderSize
# (✗ - "should") maxTxSize should not be increased by more than 2,560 Bytes (2.5KB) in any epoch, and preferably should be increased by 2,048 Bytes (2KB) or less per epoch
# (✗ - "should") maxTxSize should not exceed 1/4 of the block size
# (✓) maxTxSize must not exceed 32,768 Bytes (32KB)
# (✓) maxTxSize must not be negative

def mts_01(maxTxSize, proposal, constitutions):
    # Get the current value of maxBlockBodySize
    latest_constitution = constitutions[-1]
    maxBlockBodySize = latest_constitution["parameters_values"]["2"]
    return (maxTxSize <= maxBlockBodySize)

def mts_02(maxTxSize, proposal, constitutions):
    # Get the current value of maxBlockBodySize
    latest_constitution = constitutions[-1]

    if "2" in proposal:
        maxBlockBodySize = proposal["2"]
    else:
        maxBlockBodySize = latest_constitution["parameters_values"]["2"]
    
    if "4" in proposal:
        maxBlockHeaderSize = proposal["4"]
    else:
        maxBlockHeaderSize = latest_constitution["parameters_values"]["4"]

    return (maxTxSize <= maxBlockBodySize - maxBlockHeaderSize)

def mts_03(maxTxSize, proposal, constitutions):
    latest_constitution = constitutions[-1]
    return abs(maxTxSize - latest_constitution["parameters_values"]["3"])

def mts_04(maxTxSize, proposal, constitutions):
    latest_constitution = constitutions[-1]
    if "2" in proposal:
        maxBlockBodySize = proposal["2"]
    else:
        maxBlockBodySize = latest_constitution["parameters_values"]["2"]
    return (maxTxSize <= maxBlockBodySize/4)

def mts_05(maxTxSize):
    return maxTxSize <= 32768

def mts_06(maxTxSize):
    return maxTxSize >= 0

checkable = [
    { "name": "MTS-05"
    , "description": "maxTxSize must not exceed 32,768 Bytes (32KB)"
    , "function": mts_05
    },
    { "name": "MTS-06"
    , "description": "maxTxSize must not be negative"
    , "function": mts_06
    }
]

uncheckable = [
    { "name": "MTS-01"
    , "description": "maxTxSize must not be decreased, other than in exceptional circumstances"
    , "function": mts_01
    },
    { "name": "MTS-02"
    , "description": "maxTxSize must not exceed maxBlockBodySize minus maxBlockHeaderSize"
    , "function": mts_02
    },
    { "name": "MTS-03"
    , "description": "maxTxSize must not be increased"
    , "function": mts_03
    },
    { "name": "MTS-04"
    , "description": "maxTxSize must not exceed 1/4 of the block size"
    , "function": mts_04
    }
]

