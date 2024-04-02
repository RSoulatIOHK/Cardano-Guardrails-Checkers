# (✓) govActionLifetime must not be less than 1 epoch (5 days)

# (✗ - "should") govActionLifetime should not be less than 2 epochs (10 days)

# (✓) govActionLifetime must not be greater than 15 epochs (75 days)

# (✗ - "should") govActionLifetime should be calibrated in human terms (eg 30 days, two weeks), to allow sufficient time for voting etc. to take place

# (⧗ - no access to existing parameter values) govActionLifetime must be less than dRepActivity

def gal_01(govActionLifetime):
    return govActionLifetime >= 1

def gal_02(govActionLifetime):
    return govActionLifetime <= 15

def gal_03(govActionLifetime, proposal, constitutions):
    return govActionLifetime >= 2

def gal_04(govActionLifetime, proposal, constitutions):
    return None

def gal_05(govActionLifetime, proposal, constitutions):
    if "32" in proposal["parameter_changes"]:
        dRepActivity = proposal["parameter_changes"]["32"]
    else:
        dRepActivity = constitutions[-1]["parameters_values"]["32"]
    return govActionLifetime < dRepActivity

checkable = [
    { "name": "GAL-01"
    , "description": "govActionLifetime must not be less than 1 epoch (5 days)"
    , "function": gal_01
    },
    { "name": "GAL-02"
    , "description": "govActionLifetime must not be greater than 15 epochs (75 days)"
    , "function": gal_02
    }
]

uncheckable = [
    { "name": "GAL-03"
    , "description": "govActionLifetime should not be less than 2 epochs (10 days)"
    , "function": gal_03
    },
    { "name": "GAL-04"
    , "description": "govActionLifetime should be calibrated in human terms (eg 30 days, two weeks), to allow sufficient time for voting etc. to take place"
    , "function": gal_04
    },
    { "name": "GAL-05"
    , "description": "govActionLifetime must be less than dRepActivity"
    , "function": gal_05
    }
]