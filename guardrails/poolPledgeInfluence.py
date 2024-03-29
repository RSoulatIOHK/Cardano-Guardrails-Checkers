# (✗ - "should") poolPledgeInfluence should not vary by more than +/- 10% in any 18-epoch period (approximately 3 months)

# (✓) poolPledgeInfluence must not be set below 0.1

# (✓) poolPledgeInfluence must not exceed 1.0

def ppi_01(poolPledgeInfluence, proposal, constitutions):
    poolPledgeInfluence = poolPledgeInfluence[0]/poolPledgeInfluence[1]
    valid_constitutions = [c for c in constitutions if abs(c["epoch"] - proposal["start_epoch"]) < 18]
    # if valid_constitutions == []:
    #     first_valid_constitution = constitutions[-1]
    # else:
    #     first_valid_constitution = valid_constitutions[0]
    all_PoolPledgeInfluence = [c["parameters_values"]["12"] for c in valid_constitutions]   
    return all([abs((ppi[0]/ppi[1])/poolPledgeInfluence) <= 0.1 for ppi in all_PoolPledgeInfluence])

def ppi_02(poolPledgeInfluence):
    poolPledgeInfluence = poolPledgeInfluence[0]/poolPledgeInfluence[1]
    return poolPledgeInfluence >= 0.1

def ppi_03(poolPledgeInfluence):
    poolPledgeInfluence = poolPledgeInfluence[0]/poolPledgeInfluence[1]
    return poolPledgeInfluence <= 1.0

checkable = [
    { "name": "PPI-02"
    , "description": "poolPledgeInfluence must not be set below 0.1"
    , "function": ppi_02
    },
    { "name": "PPI-03"
    , "description": "poolPledgeInfluence must not exceed 1.0"
    , "function": ppi_03
    }
]

uncheckable = [
    { "name": "PPI-01"
    , "description": "poolPledgeInfluence should not vary by more than +/- 10% in any 18-epoch period (approximately 3 months)"
    , "function": ppi_01
    }
]
    