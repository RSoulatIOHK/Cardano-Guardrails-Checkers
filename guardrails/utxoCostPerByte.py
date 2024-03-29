# (✓) utxoCostPerByte must not be reduced below 3,000  (0.003 adaAda)

# (✓) utxoCostPerByte must not be increased above 6,500  (0.0065 adaAda)

# (✓) utxoCostPerByte must not be set to zero

# (✓) utxoCostPerByte must not be negative

# (✗ - "should") Changes to utxoCostPerByte need to account for
# The acceptable cost of attack (25M adaAda is assumed)
# The acceptable time for an attack (at least one epoch is assumed)
# The acceptable memory configuration for full node users (assumed to be 16GB for wallets or 24GB for stake pools)
# The sizes of UTxOs (~200B per UTxO minimum, up to about 10KB)
# The current total node memory usage (~10GB)

def ucpb_01(utxoCostPerByte):
    return utxoCostPerByte >= 3000

def ucpb_02(utxoCostPerByte):
    return utxoCostPerByte <= 6500

def ucpb_03(utxoCostPerByte):
    return utxoCostPerByte != 0

def ucpb_04(utxoCostPerByte):
    return utxoCostPerByte >= 0

def defaultCheck(paramProposal, proposal, constitutions):
    return None

checkable = [
    { "name": "UCPB-01"
    , "description": "utxoCostPerByte must not be decreased below 3,000  (0.003 adaAda)"
    , "function": ucpb_01
    },
    { "name": "UCPB-02"
    , "description": "utxoCostPerByte must not be increased above 6,500  (0.0065 adaAda)"
    , "function": ucpb_02
    },
    { "name": "UCPB-03"
    , "description": "utxoCostPerByte must not be set to zero"
    , "function": ucpb_03
    },
    { "name": "UCPB-04"
    , "description": "utxoCostPerByte must not be negative"
    , "function": ucpb_04
    }
]

uncheckable = [
    { "name": "UCPB-05"
    , "description": "Changes to utxoCostPerByte need to account for blablabla"
    , "function": defaultCheck
    }
]