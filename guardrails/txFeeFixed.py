def tff_01(txFeeFixed):
    return txFeeFixed >= 100000

def tff_02(txFeeFixed):
    return txFeeFixed <= 10000000

def tff_03(txFeeFixed):
    return txFeeFixed >= 0

def tf_01(paramProposal, proposal, constitutions):
    proposalParameters = proposal["parameter_changes"]
    return "19" in proposalParameters and ("0" in proposal or "1" in proposal)

def tf_02(paramProposal, proposal, constitutions):
    return None

def mfrs_03(txFeeFixed, proposal, constitutions):
    return "33" in proposal

checkable = [
    { "name": "TFF-01"
    , "description": "txFeeFixed must not be decreased below 100,000 (0.1 Ada)"
    , "function": tff_01
    },
    { "name": "TFF-02"
    , "description": "txFeeFixed must not be increased above 10,000,000 (10 Ada)"
    , "function": tff_02
    },
    { "name": "TFF-03"
    , "description": "txFeeFixed must not be negative"
    , "function": tff_03
    }
]

uncheckable = [
    { "name": "TF-01"
     , "description": "To maintain a consistent level of protection against denial-of-service attacks,  txFeePerByte and txFeeFixed should be adjusted whenever Plutus Execution prices are adjusted (executionUnitPrices[steps/memory])"
     , "function": tf_01
    },
    { "name": "TF-02"
    , "description": "Any changes to txFeePerByte or txFeeFixed must consider the implications of reducing the cost of a denial-of-service attack or increasing the maximum transaction fee"
    , "function": tf_02
    },
    { "name": "MFRS-03"
    , "description": "txFeeFixed should be adjusted in line with fiat changes"
    , "function": mfrs_03
    }
]