# (⧗ - no access to existing parameter values) maxTxExecutionUnits[memory] must not be decreased
# (✗ - "should") maxTxExecutionUnits[memory] should not be increased by more than 2,500,000 units in any epoch
# (✗ - "should") maxBlockExecutionUnits[memory] should not be changed (increased or decreased) by more than 10,000,000 units in any epoch
# (✓) maxTxExecutionUnits[memory] must not exceed 40,000,000 units
# (✓) maxBlockExecutionUnits[memory] must not exceed 120,000,000 units
# (⧗ - no access to existing parameter values) maxBlockExecutionUnits[memory]  must not be less than maxTxExecutionUnits[memory]
# (✓) maxTxExecutionUnits[memory] must not be negative
# (✓) maxBlockExecutionUnits[memory]  must not be negative

# (⧗ - no access to existing parameter values) maxTxExecutionUnits[steps] must not be decreased
# (✗ - "should") maxTxExecutionUnits[steps] should not be increased by more than 500,000,000 (500M) units in any epoch (5 days)
# (✗ - "should") maxBlockExecutionUnits[steps]  should not be changed  (increased or decreased) by more than 2,000,000,000 (2Bn) units in any epoch (5 days)
# (✓) maxTxExecutionUnits[steps] must not exceed 15,000,000,000 (15Bn) units
# (✓) maxBlockExecutionUnits[steps] must not exceed 40,000,000,000 (40Bn) units
# (⧗ - no access to existing parameter values) maxBlockExecutionUnits[steps] must not be less than maxTxExecutionUnits[steps]
# (✓) maxBlockExecutionUnits[steps] must not be negative
# (✓) maxTxExecutionUnits[steps] must not be negative

def mbeu_m_01(maxBlockExecutionUnits):
    return maxBlockExecutionUnits["mem"] <= 120000000

def mbeu_m_02(maxBlockExecutionUnits):
    return maxBlockExecutionUnits["mem"] >= 0

def mbeu_m_03(maxBlockExecutionUnits, proposal, constitutions):
    latest_constitution = constitutions[-1]
    return abs(maxBlockExecutionUnits["mem"] - latest_constitution["parameters_values"]["21"]["mem"]) <= 10000000

def mbeu_m_04(maxBlockExecutionUnits, proposal, constitutions):
    if "20" in proposal:
        return maxBlockExecutionUnits["mem"] >= proposal["parameters_values"]["20"]["mem"]
    else:
        return maxBlockExecutionUnits["mem"] >= constitutions[-1]["parameters_values"]["20"]["mem"]
    
def mbeu_s_01(maxBlockExecutionUnits):
    return maxBlockExecutionUnits["steps"] <= 40000000000

def mbeu_s_02(maxBlockExecutionUnits):
    return maxBlockExecutionUnits["steps"] >= 0

def mbeu_s_03(maxBlockExecutionUnits, proposal, constitutions):
    latest_constitution = constitutions[-1]
    return abs(maxBlockExecutionUnits["steps"] - latest_constitution["parameters_values"]["21"]["steps"]) <= 2000000000

def mbeu_s_04(maxBlockExecutionUnits, proposal, constitutions):
    if "20" in proposal:
        return maxBlockExecutionUnits["steps"] >= proposal["parameters_values"]["20"]["steps"]
    else:
        return maxBlockExecutionUnits["steps"] >= constitutions[-1]["parameters_values"]["20"]["steps"]
    
checkable = [
    { "name": "MBEU-M-01"
    , "description": "maxBlockExecutionUnits[memory] must not exceed 120,000,000 units"
    , "function": mbeu_m_01
    },
    { "name": "MBEU-M-02"
    , "description": "maxBlockExecutionUnits[memory] must not be negative"
    , "function": mbeu_m_02
    },
    { "name": "MBEU-S-01"
    , "description": "maxBlockExecutionUnits[steps] must not exceed 40,000,000,000 units"
    , "function": mbeu_s_01
    },
    { "name": "MBEU-S-02"
    , "description": "maxBlockExecutionUnits[steps] must not be negative"
    , "function": mbeu_s_02
    }
]

uncheckable = [
    { "name": "MBEU-M-03"
    , "description": "maxBlockExecutionUnits[memory] should not be changed (increased or decreased) by more than 10,000,000 units in any epoch"
    , "function": mbeu_m_03
    },
    { "name": "MBEU-M-04"
    , "description": "maxBlockExecutionUnits[memory] should not be decreased"
    , "function": mbeu_m_04
    },
    { "name": "MBEU-S-03"
    , "description": "maxBlockExecutionUnits[steps] should not be changed  (increased or decreased) by more than 2,000,000,000 (2Bn) units in any epoch"
    , "function": mbeu_s_03
    },
    { "name": "MBEU-S-04"
    , "description": "maxBlockExecutionUnits[steps] should not be decreased"
    , "function": mbeu_s_04
    }
]