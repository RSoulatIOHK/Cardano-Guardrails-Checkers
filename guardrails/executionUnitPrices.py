# (✗ - “similar to”) The execution prices must be set so that

# the cost of executing a transaction with maximum CPU steps is similar to the cost of a maximum sized non-script transaction
# the cost of executing a transaction with maximum memory units is similar to the cost of a maximum sized non-script transaction


# (✗ - "should") The execution prices should be adjusted whenever transaction fees are adjusted (txFeeFixed/txFeePerByte)

# (✓) executionUnitPrices[step_price] must not exceed 2,000 / 10,000,000

# (✓) executionUnitPrices[step_price]  must not be lower than 500 / 10,000,000

# (✓) executionUnitPrices[mem_price]  must not exceed 2,000 / 10,000

# (✓) executionUnitPrices[mem_price] must not be lower than 400 / 10,000

# This one comes from minFeeRefScriptCoinsPerByte:
# (✗ - "should") To maintain a consistent level of protection against denial-of-service attacks, minFeeRefScriptCoinsPerByte should be adjusted whenever Plutus Execution prices are adjusted (executionUnitPrices[steps/memory]) and whenever txFeePerByte is adjusted



def eup_ps_01(executionUnitPrices):
    eup_ps_check = executionUnitPrices["step_price"][0]/executionUnitPrices["step_price"][1]
    return eup_ps_check <= 2000/10000000

def eup_ps_02(executionUnitPrices):
    eup_ps_check = executionUnitPrices["step_price"][0]/executionUnitPrices["step_price"][1]
    return eup_ps_check >= 500/10000000

def eup_pm_01(executionUnitPrices):
    eup_pm_check = executionUnitPrices["mem_price"][0]/executionUnitPrices["mem_price"][1]
    return eup_pm_check <= 2000/10000

def eup_pm_02(executionUnitPrices):
    eup_pm_check = executionUnitPrices["mem_price"][0]/executionUnitPrices["mem_price"][1]
    return eup_pm_check >= 400/10000

def eup_01(executionUnitPrices, proposal, constitutions):
    return None

def eup_02(executionUnitPrices, proposal, constitutions):
    proposalParameters = proposal["parameter_changes"]
    return "19" in proposalParameters and ("0" in proposalParameters or "1" in proposalParameters)

def mfrs_03(executionUnitPrices, proposal, constitutions):
    proposalParameters = proposal["parameter_changes"]
    return "33" in proposalParameters


checkable = [
    { "name": "EUP-PS-01"
    , "description": "executionUnitPrices[step_price] must not exceed 2,000 / 10,000,000"
    , "function": eup_ps_01
    },
    { "name": "EUP-PS-02"
    , "description": "executionUnitPrices[step_price] must not be lower than 500 / 10,000,000"
    , "function": eup_ps_02
    },
    { "name": "EUP-PM-01"
    , "description": "executionUnitPrices[mem_price] must not exceed 2,000 / 10,000"
    , "function": eup_pm_01
    },
    { "name": "EUP-PM-02"
    , "description": "executionUnitPrices[mem_price] must not be lower than 400 / 10,000"
    , "function": eup_pm_02
    }
]

uncheckable = [
    { "name": "EUP-01"
    , "description": "The execution prices must be set so that the cost of executing a transaction with maximum CPU steps is similar to the cost of a maximum sized non-script transaction and the cost of executing a transaction with maximum memory units is similar to the cost of a maximum sized non-script transaction"
    , "function": eup_01
    },
    { "name": "EUP-02"
    , "description": "The execution prices should be adjusted whenever transaction fees are adjusted (txFeeFixed/txFeePerByte)"
    , "function": eup_02
    },
    { "name": "MFRS-03"
    , "description": "To maintain a consistent level of protection against denial-of-service attacks, minFeeRefScriptCoinsPerByte should be adjusted whenever Plutus Execution prices are adjusted (executionUnitPrices[steps/memory]) and whenever txFeePerByte is adjusted"
    , "function": mfrs_03
    }
]