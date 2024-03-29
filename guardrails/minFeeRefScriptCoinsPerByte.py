# (✓) minFeeRefScriptCoinsPerByte must not be increased above 1,000  (0.001 ada)
# This ensures that transactions can be paid for



# (✓) minFeeRefScriptCoinsPerByte must not be negative


# (✗ - unquantifiable) Any changes to minFeeRefScriptCoinsPerByte must consider the implications of reducing the cost of a denial-of-service attack or increasing the maximum transaction fee 

def mfrs_01(minFeeRefScriptCoinsPerByte):
    return minFeeRefScriptCoinsPerByte <= 1000

def mfrs_02(minFeeRefScriptCoinsPerByte):
    return minFeeRefScriptCoinsPerByte >= 0

def mfrs_04(minFeeRefScriptCoinsPerByte, proposal, constitutions):
    return None

checkable = [
    { "name": "MFRS-01"
    , "description": "minFeeRefScriptCoinsPerByte must not be increased above 1,000  (0.001 ada)"
    , "function": mfrs_01
    },
    { "name": "MFRS-02"
    , "description": "minFeeRefScriptCoinsPerByte must not be negative"
    , "function": mfrs_02
    }
]

uncheckable = [
    { "name": "MFRS-04"
    , "description": "Any changes to minFeeRefScriptCoinsPerByte must consider the implications of reducing the cost of a denial-of-service attack or increasing the maximum transaction fee"
    , "function": mfrs_04
    }
]