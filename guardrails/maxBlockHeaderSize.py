# (✗ - “largest valid header” is subject to change) maxBlockHeaderSize must be large enough for the largest valid header
# (✗ - "should") maxBlockHeaderSize should only normally be increased if the protocol changes
# (✗ - "should") maxBlockHeaderSize should be within TCP’s initial congestion window (3 or 10 MTUs).
# (✓) maxBlockHeaderSize must not exceed 5,000 Bytes


# (✓) maxBlockHeaderSize must not be negative

largest_valid_header = -1

def mbhs_01(maxBlockHeaderSize, proposal, constitutions):
    return True

def mbhs_02(maxBlockHeaderSize, proposal, constitutions):
    latest_constitution = constitutions[-1]
    return (maxBlockHeaderSize >= latest_constitution["parameters_values"]["4"])

def mbhs_03(maxBlockHeaderSize, proposal, constitutions):
    def TCP_simulation():
        return 7
    return TCP_simulation()

def mbhs_04(maxBlockHeaderSize):
    return maxBlockHeaderSize <= 5000

def mbhs_05(maxBlockHeaderSize):
    return maxBlockHeaderSize >= 0

checkable = [
    { "name": "MBHS-04"
    , "description": "maxBlockHeaderSize must not exceed 5,000 Bytes"
    , "function": mbhs_04
    },
    { "name": "MBHS-05"
    , "description": "maxBlockHeaderSize must not be negative"
    , "function": mbhs_05
    }
]

uncheckable = [
    { "name": "MBHS-01"
    , "description": "maxBlockHeaderSize must not be decreased, other than in exceptional circumstances"
    , "function": mbhs_01
    },
    { "name": "MBHS-02"
    , "description": "maxBlockHeaderSize must not be less than the current maxBlockHeaderSize"
    , "function": mbhs_02
    },
    { "name": "MBHS-03"
    , "description": "maxBlockHeaderSize must be within TCP’s initial congestion window (3 or 10 MTUs)"
    , "function": mbhs_03
    }
]