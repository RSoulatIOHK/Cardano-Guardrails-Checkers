def tfpb_01(txFeePerByte):
    return txFeePerByte >= 30

def tfpb_02(txFeePerByte):
    return txFeePerByte <= 1000

def tfpb_03(txFeePerByte):
    return txFeePerByte >= 0

def tf_01(paramProposal, proposal, constitutions):
    proposalParameters = proposal["parameter_changes"]
    return "19" in proposalParameters and ("0" in proposal or "1" in proposal)

def tf_02(paramProposal, proposal, constitutions):
    return None

def mfrs_03(executionUnitPrices, proposal, constitutions):
    return "33" in proposal

checkable = [
    { "name": "TFPB-01"
    , "description": "txFeePerByte must not be decreased below 30  (0.000030 Ada)"
    , "function": tfpb_01
    },
    { "name": "TFPB-02"
    , "description": "txFeePerByte must not be increased above 1,000 (0.001 Ada)"
    , "function": tfpb_02
    },
    { "name": "TFPB-03"
    , "description": "txFeePerByte must not be negative"
    , "function": tfpb_03
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
    , "description": "txFeePerByte should be adjusted in line with fiat changes"
    , "function": mfrs_03
    }
]