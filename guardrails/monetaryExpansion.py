# (✗ - "should") monetaryExpansion should not be varied by more than +/- 10% in any 73-epoch period (approximately 12 months period)

# (✓) monetaryExpansion must not exceed 0.005

# (✓) monetaryExpansion must not be lower than 0.001

# (✓) monetaryExpansion must not be negative

def me_01(monetaryExpansion):
    monetaryExpansion = monetaryExpansion[0]/monetaryExpansion[1]
    return monetaryExpansion <= 0.005

def me_02(monetaryExpansion):
    monetaryExpansion = monetaryExpansion[0]/monetaryExpansion[1]
    return monetaryExpansion >= 0.001

def me_03(monetaryExpansion):
    monetaryExpansion = monetaryExpansion[0]/monetaryExpansion[1]
    return monetaryExpansion >= 0

def defaultCheck(paramProposal, proposal, constitutions):
    return None

def me_04(paramProposal, proposal, constitutions):
    # Get the current epoch
    current_epoch = proposal["start_epoch"]
    min_expansion = 1.0
    max_expansion = 0.0
    for constitution in constitutions:
        # Check if the constitution is less than 12 months old
        paramProposal = constitution["parameters_values"]["10"]
        paramProposal = paramProposal[0]/paramProposal[1]
        if current_epoch - constitution["epoch"] < 73:
            # print(f'constitution change: {constitution["parameters_values"]["10"]}')
            if paramProposal < min_expansion:
                min_expansion = paramProposal
            if paramProposal > max_expansion:
                max_expansion = paramProposal
    paramProposal = proposal["parameter_changes"]["10"]
    paramProposal = paramProposal[0]/paramProposal[1]
    if paramProposal < min_expansion:
        min_expansion = paramProposal
    if paramProposal > max_expansion:
        max_expansion = paramProposal
    if max_expansion - min_expansion > 0.1:
        return False
    else:
        return True
    
checkable = [
    { "name": "ME-01"
    , "description": "monetaryExpansion must not exceed 0.005"
    , "function": me_01
    },
    { "name": "ME-02"
    , "description": "monetaryExpansion must not be lower than 0.001"
    , "function": me_02
    },
    { "name": "ME-03"
    , "description": "monetaryExpansion must not be negative"
    , "function": me_03
    }
]

uncheckable = [
    { "name": "ME-04"
    , "description": "monetaryExpansion should not be varied by more than +/- 10% in any 73-epoch period (approximately 12 months period)"
    , "function": me_04
    }
]
