# (✗ - "should") minPoolCost should be set in line with the economic cost for operating a pool
# Assumed to be approximately $30 per epoch


# (✓) minPoolCost must not be negative

# (✓) minPoolCost must not be set above 500,000,000 (500 adaAda)

def mpc_01(minPoolCost):
    return minPoolCost >= 0

def mpc_02(minPoolCost):
    return minPoolCost <= 500000000

def defaultCheck(paramProposal, proposal, constitutions):
    return None

checkable = [
    { "name": "MPC-01"
    , "description": "minPoolCost must not be negative"
    , "function": mpc_01
    },
    { "name": "MPC-02"
    , "description": "minPoolCost must not be set above 500,000,000 (500 adaAda)"
    , "function": mpc_02
    }
]

uncheckable = [
    { "name": "MPC-03"
    , "description": "minPoolCost should be set in line with the economic cost for operating a pool"
    , "function": defaultCheck
    }
]
