# (✓) treasuryCut must be set between 0.1 (10%) and 0.3 (30%)

# (✓) treasuryCut must not be negative

# (✓) treasuryCut must not exceed 1.0 (100%)

# (✗ - "cannot be enforced automatically") treasuryCut must not be changed more than once in any 36 epoch period (approximately 6 months)

def tc_01(treasuryCut):
    treasuryCut = treasuryCut[0]/treasuryCut[1]
    return treasuryCut >= 0.1 and treasuryCut <= 0.3

def tc_02(treasuryCut):
    treasuryCut = treasuryCut[0]/treasuryCut[1]
    return treasuryCut >= 0

def tc_03(treasuryCut):
    treasuryCut = treasuryCut[0]/treasuryCut[1]
    return treasuryCut <= 1.0

def tc_04(paramProposal, proposal, constitutions):
    # Get the current epoch
    current_epoch = proposal["start_epoch"]
    ref_treasurycut = None
    changes = 0
    for constitution in constitutions:
        ref_treasurycut = constitution["parameters_values"]["11"]
        # Check if the constitution is less than 6 months old
        if (current_epoch - constitution["epoch"] < 36) and (ref_treasurycut != constitution["parameters_values"]["11"]):
            changes += 1
    if "11" in proposal["parameter_changes"]:
        if ref_treasurycut != proposal["parameter_changes"]["11"]:
            changes += 1
    return (changes <= 1)

def defaultCheck(paramProposal, proposal, constitutions):
    return None

checkable = [
    { "name": "TC-01"
    , "description": "treasuryCut must be set between 0.1 (10%) and 0.3 (30%)"
    , "function": tc_01
    },
    { "name": "TC-02"
    , "description": "treasuryCut must not be negative"
    , "function": tc_02
    },
    { "name": "TC-03"
    , "description": "treasuryCut must not exceed 1.0 (100%)"
    , "function": tc_03
    }
]

uncheckable = [
    { "name": "TC-04"
    , "description": "treasuryCut must not be changed more than once in any 36 epoch period (approximately 6 months)"
    , "function": tc_04
    }
]