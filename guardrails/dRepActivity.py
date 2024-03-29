# (✓) dRepActivity must not be less than 13 epochs (2 months)
# (✓) dRepActivity must not exceed 37 epochs (6 months)
# (⧗ - no access to existing parameter values) dRepActivity must be greater than govActionLifetime
# (✓) dRepActivity must not be negative
# (✗ - "should") dRepActivity should be calculated in human terms (2 months etc)

def dra_01(dRepActivity):
    return dRepActivity >= 13

def dra_02(dRepActivity):
    return dRepActivity <= 37

def dra_03(dRepActivity):
    return dRepActivity > 0

def dra_04(dRepActivity, proposal, constitutions):
    if "29" in proposal:
        govActionLifetime = proposal["29"]
    else:
        govActionLifetime = constitutions[-1]["parameters_values"]["29"]
    return dRepActivity > govActionLifetime

def dra_05(dRepActivity, proposal, constitutions):
    return None

checkable = [
    { "name": "DRA-01"
    , "description": "dRepActivity must not be less than 13 epochs (2 months)"
    , "function": dra_01
    },
    { "name": "DRA-02"
    , "description": "dRepActivity must not exceed 37 epochs (6 months)"
    , "function": dra_02
    },
    { "name": "DRA-03"
    , "description": "dRepActivity must not be negative"
    , "function": dra_03
    }
]

uncheckable = [
    { "name": "DRA-04"
    , "description": "dRepActivity must be greater than govActionLifetime"
    , "function": dra_04
    },
    { "name": "DRA-05"
    , "description": "dRepActivity should be calculated in human terms (2 months etc)"
    , "function": dra_05
    }
]