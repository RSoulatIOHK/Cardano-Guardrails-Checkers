# (⧗ - no access to existing parameter values) maxValueSize must be less than maxTxSize

# maxValueSize must not exceed 12,288 Bytes (12KB)


# (✓) maxValueSize must not be negative

# (⧗ - no access to existing parameter values) maxValueSize must never be reduced

# (✗ - “sensible output” is subject to interpretation) maxValueSize must be large enough to allow sensible outputs (e.g. any existing on-chain output or anticipated outputs that could be produced by new ledger rules)

def mvs_01(maxValueSize):
    return maxValueSize <= 12288

def mvs_02(maxValueSize):
    return maxValueSize >= 0

def mvs_03(paramProposal, proposal, constitutions):
    if "3" in proposal:
        return paramProposal > proposal["parameters_values"]["3"]
    else:
        return paramProposal > constitutions[-1]["parameters_values"]["3"]
    
def mvs_04(maxValueSize, proposal, constitutions):
    return maxValueSize >= constitutions[-1]["parameters_values"]["3"]

def mvs_05(maxValueSize, proposal, constitutions):
    return None

checkable = [
    { "name": "MVS-01"
    , "description": "maxValueSize must not exceed 12,288 Bytes (12KB)"
    , "function": mvs_01
    },
    { "name": "MVS-02"
    , "description": "maxValueSize must not be negative"
    , "function": mvs_02
    }
]

uncheckable = [
    { "name": "MVS-03"
    , "description": "maxValueSize must never be reduced"
    , "function": mvs_03
    },
    { "name": "MVS-04"
    , "description": "maxValueSize must be large enough to allow sensible outputs (e.g. any existing on-chain output or anticipated outputs that could be produced by new ledger rules)"
    , "function": mvs_04
    },
    { "name": "MVS-05"
    , "description": "maxValueSize must be less than maxTxSize"
    , "function": mvs_05
    }
]