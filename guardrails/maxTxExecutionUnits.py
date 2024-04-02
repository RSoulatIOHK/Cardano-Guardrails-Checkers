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

def mteu_m_01(maxTxExecutionUnits):
    return maxTxExecutionUnits["mem"] <= 40000000

def mteu_m_02(maxTxExecutionUnits):
    return maxTxExecutionUnits["mem"] >= 0

def mteu_m_03(maxTxExecutionUnits, proposal, constitutions):
    latest_constitution = constitutions[-1]
    return maxTxExecutionUnits["mem"] >= latest_constitution["parameters_values"]["20"]["mem"]

def mteu_m_04(maxTxExecutionUnits, proposal, constitutions):
    latest_constitution = constitutions[-1]
    return maxTxExecutionUnits["mem"] - latest_constitution["parameters_values"]["20"]["mem"] <= 2500000

def mteu_m_05(maxTxExecutionUnits, proposal, constitutions):
    if "21" in proposal:
        return maxTxExecutionUnits["mem"] <= proposal["parameters_values"]["21"]["mem"]
    else:
        return maxTxExecutionUnits["mem"] <= constitutions[-1]["parameters_values"]["21"]["mem"]
    
def mteu_s_01(maxTxExecutionUnits):
    return maxTxExecutionUnits["steps"] <= 15000000000

def mteu_s_02(maxTxExecutionUnits):
    return maxTxExecutionUnits["steps"] >= 0

def mteu_s_03(maxTxExecutionUnits, proposal, constitutions):
    latest_constitution = constitutions[-1]
    return maxTxExecutionUnits["steps"] >= latest_constitution["parameters_values"]["20"]["steps"]

def mteu_s_04(maxTxExecutionUnits, proposal, constitutions):
    latest_constitution = constitutions[-1]
    return maxTxExecutionUnits["steps"] - latest_constitution["parameters_values"]["20"]["steps"] <= 500000000

def mteu_s_05(maxTxExecutionUnits, proposal, constitutions):
    if "21" in proposal:
        return maxTxExecutionUnits["steps"] <= proposal["parameters_values"]["21"]["steps"]
    else:
        return maxTxExecutionUnits["steps"] <= constitutions[-1]["parameters_values"]["21"]["steps"]
    
checkable = [
    { "name": "MTEU-M-01"
    , "description": "maxTxExecutionUnits[memory] must not exceed 40,000,000 units"
    , "function": mteu_m_01
    },
    { "name": "MTEU-M-02"
    , "description": "maxTxExecutionUnits[memory] must not be negative"
    , "function": mteu_m_02
    },
    { "name": "MTEU-S-01"
    , "description": "maxTxExecutionUnits[steps] must not exceed 15,000,000,000 units"
    , "function": mteu_s_01
    },
    { "name": "MTEU-S-02"
    , "description": "maxTxExecutionUnits[steps] must not be negative"
    , "function": mteu_s_02
    }
]

uncheckable = [
    { "name": "MTEU-M-03"
    , "description": "maxTxExecutionUnits[memory] must not be decreased"
    , "function": mteu_m_03
    },
    { "name": "MTEU-M-04"
    , "description": "maxTxExecutionUnits[memory] should not be increased by more than 2,500,000 units in any epoch"
    , "function": mteu_m_04
    },
    { "name": "MTEU-M-05"
    , "description": "maxTxExecutionUnits[memory] must not exceed the value of the latest constitution"
    , "function": mteu_m_05
    },
    { "name": "MTEU-S-03"
    , "description": "maxTxExecutionUnits[steps] should not be changed (increased or decreased) by more than the value of the latest constitution"
    , "function": mteu_s_03
    },
    { "name": "MTEU-S-04"
    , "description": "maxTxExecutionUnits[steps] should not be increased by more than 500,000,000 units in any epoch"
    , "function": mteu_s_04
    },
    { "name": "MTEU-S-05"
    , "description": "maxTxExecutionUnits[steps] must not exceed the value of the latest constitution"
    , "function": mteu_s_05
    }
]