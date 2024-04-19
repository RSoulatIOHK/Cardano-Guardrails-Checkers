import json
from paramMap import paramMap
from contextlib import ExitStack

import guardrails.txFeeFixed as txFeeFixed
import guardrails.txFeePerByte as txFeePerByte
import guardrails.utxoCostPerByte as utxoCostPerByte
import guardrails.stakeAddressDeposit as stakeAddressDeposit
import guardrails.stakePoolDeposit as stakePoolDeposit
import guardrails.minPoolCost as minPoolCost
import guardrails.treasuryCut as treasuryCut
import guardrails.monetaryExpansion as monetaryExpansion
import guardrails.maxBlockBodySize as maxBlockBodySize
import guardrails.maxTxSize as maxTxSize
import guardrails.maxBlockHeaderSize as maxBlockHeaderSize
import guardrails.poolRetireMaxEpoch as poolRetireMaxEpoch
import guardrails.stakePoolTargetNum as stakePoolTargetNum
import guardrails.poolPledgeInfluence as poolPledgeInfluence
import guardrails.costModels as costModels
import guardrails.maxValueSize as maxValueSize
import guardrails.collateralPercentage as collateralPercentage
import guardrails.maxCollateralInputs as maxCollateralInputs
import guardrails.maxBlockExecutionUnits as maxBlockExecutionUnits
import guardrails.maxTxExecutionUnits as maxTxExecutionUnits
import guardrails.executionUnitPrices as executionUnitPrices
import guardrails.govActionLifetime as govActionLifetime
import guardrails.committeeMinSize as committeeMinSize
import guardrails.committeeMaxTermLimit as committeeMaxTermLimit
import guardrails.govDeposit as govDeposit
import guardrails.dRepDeposit as dRepDeposit
import guardrails.dRepActivity as dRepActivity
import guardrails.minFeeRefScriptCoinsPerByte as minFeeRefScriptCoinsPerByte

guardrailChecks = {
    "0": {
        "checkable": txFeePerByte.checkable,
        "uncheckable": txFeePerByte.uncheckable
    },
    "1": {
        "checkable": txFeeFixed.checkable,
        "uncheckable": txFeeFixed.uncheckable
    },
    "2": {
        "checkable": maxBlockBodySize.checkable,
        "uncheckable": maxBlockBodySize.uncheckable
    },
    "3": {
        "checkable": maxTxSize.checkable,
        "uncheckable": maxTxSize.uncheckable
    },
    "4": {
        "checkable": maxBlockHeaderSize.checkable,
        "uncheckable": maxBlockHeaderSize.uncheckable
    },
    "5": {
        "checkable": stakeAddressDeposit.checkable,
        "uncheckable": stakeAddressDeposit.uncheckable
    },
    "6": {
        "checkable": stakePoolDeposit.checkable,
        "uncheckable": stakePoolDeposit.uncheckable
    },
    "7": {
        "checkable": poolRetireMaxEpoch.checkable,
        "uncheckable": poolRetireMaxEpoch.uncheckable
    },
    "8": {
        "checkable": stakePoolTargetNum.checkable,
        "uncheckable": stakePoolTargetNum.uncheckable
    },
    "9": {
        "checkable": poolPledgeInfluence.checkable,
        "uncheckable": poolPledgeInfluence.uncheckable
    },
    "10": {
        "checkable": monetaryExpansion.checkable,
        "uncheckable": monetaryExpansion.uncheckable
    },
    "11": {
        "checkable": treasuryCut.checkable,
        "uncheckable": treasuryCut.uncheckable
    },
    "16": {
        "checkable": minPoolCost.checkable,
        "uncheckable": minPoolCost.uncheckable
    },
    "17": {
        "checkable": utxoCostPerByte.checkable,
        "uncheckable": utxoCostPerByte.uncheckable
    },
    "18": {
        "checkable": costModels.checkable,
        "uncheckable": costModels.uncheckable
    },
    "19": {
        "checkable": executionUnitPrices.checkable,
        "uncheckable": executionUnitPrices.uncheckable
    },
    "20": {
        "checkable": maxTxExecutionUnits.checkable,
        "uncheckable": maxTxExecutionUnits.uncheckable
    },
    "21": {
        "checkable": maxBlockExecutionUnits.checkable,
        "uncheckable": maxBlockExecutionUnits.uncheckable
    },
    "22": {
        "checkable": maxValueSize.checkable,
        "uncheckable": maxValueSize.uncheckable
    },
    "23": {
        "checkable": collateralPercentage.checkable,
        "uncheckable": collateralPercentage.uncheckable
    },
    "24": {
        "checkable": maxCollateralInputs.checkable,
        "uncheckable": maxCollateralInputs.uncheckable
    },
    "25": {
        "checkable": None,
        "uncheckable": None
    },
    "26": {
        "checkable": None,
        "uncheckable": None
    },
    "27": {
        "checkable": committeeMinSize.checkable,
        "uncheckable": committeeMinSize.uncheckable
    },
    "28": {
        "checkable": committeeMaxTermLimit.checkable,
        "uncheckable": committeeMaxTermLimit.uncheckable
    },
    "29": {
        "checkable": govActionLifetime.checkable,
        "uncheckable": govActionLifetime.uncheckable
    },
    "30": {
        "checkable": govDeposit.checkable,
        "uncheckable": govDeposit.uncheckable
    },
    "31": {
        "checkable": dRepDeposit.checkable,
        "uncheckable": dRepDeposit.uncheckable
    },
    "32": {
        "checkable": dRepActivity.checkable,
        "uncheckable": dRepActivity.uncheckable
    },
    "33": {
        "checkable": minFeeRefScriptCoinsPerByte.checkable,
        "uncheckable": minFeeRefScriptCoinsPerByte.uncheckable
    }
}

def checkGuardrails(value: int, checkableGuardrails, proposal=None, constitutions=None):
    check_results = {}
    check_results["value"] = value
    check_results["guardrails"] = {}
    if checkableGuardrails is None:
        return None
    for guardrail in checkableGuardrails:
        if proposal is None and constitutions is None:
            result = guardrail["function"](value)
        else:
            result = guardrail["function"](value, proposal, constitutions)
        guardrail_name = guardrail["name"]
        check_results["guardrails"][guardrail_name] = {
            "result": result,
            "description": guardrail["description"],
            "name": guardrail_name
        }
    return check_results

def addStaticCheck(proposal, checks):
    for key in proposal:
        paramProposal = proposal[key]
        results = checkGuardrails(paramProposal, guardrailChecks[key]["checkable"])
        checks[paramMap[key]["name"]] = results
    return checks

def addUncheckableCheck(proposal, all_constitutions, checks):
    for key in proposal["parameter_changes"]:
        paramProposal = proposal["parameter_changes"][key]
        if paramProposal == {}:
            paramProposal = all_constitutions[-1]["parameters_values"][key]
        if guardrailChecks[key]["uncheckable"] is None:
            continue
        results = checkGuardrails(paramProposal, guardrailChecks[key]["uncheckable"], proposal, all_constitutions)
        checks[paramMap[key]["name"]]["guardrails"].update(results["guardrails"])
    return checks

def checkProposalReturnFile(pathfile='./data/proposal.json', outfile='checks'):
    checks = {}
    infile = pathfile.split('/')[-1]
    outfile = infile.split('.')[0]

    with ExitStack() as stack:
        all_constitutions_files = [stack.enter_context(open(f'./constitutions/constitution_{i}.json')) for i in range(1, 3)]
        all_constitutions = [json.load(f) for f in all_constitutions_files]
        with open(pathfile) as f:
            proposal = json.load(f)
            current_parameter_proposal = proposal["parameter_changes"]
        
        # Static checks
        checks = addStaticCheck(current_parameter_proposal, checks)
        
        # All "uncheckable" checks
        checks = addUncheckableCheck(proposal, all_constitutions, checks)

        # For all the parameters add a "summary" field with True if all guardrails are True, False if any guardrail is False
        for parameter in checks:
            if checks[parameter] is not None:
                for guardrail in checks[parameter]["guardrails"]:
                    checks[parameter]["summary"] = True
                    result = checks[parameter]["guardrails"][guardrail]["result"]
                    if isinstance(result, bool) and not result:
                        checks[parameter]["summary"] = False
                        break
            else:
                pass                
    json.dump(checks, open("./data/checks_" + outfile + ".json", 'w'), indent=4)
    return outfile

def checkProposalReturnJSON(pathfile='./data/proposal.json'):
    checks = {}
    with ExitStack() as stack:
        all_constitutions_files = [stack.enter_context(open(f'./constitutions/constitution_{i}.json')) for i in range(1, 3)]
        all_constitutions = [json.load(f) for f in all_constitutions_files]
        with open(pathfile) as f:
            proposal = json.load(f)
            current_parameter_proposal = proposal["parameter_changes"]
        
        # Static checks
        checks = addStaticCheck(current_parameter_proposal, checks)
        
        # All "uncheckable" checks
        checks = addUncheckableCheck(proposal, all_constitutions, checks)

        # For all the parameters add a "summary" field with True if all guardrails are True, False if any guardrail is False
        for parameter in checks:
            if checks[parameter] is not None:
                for guardrail in checks[parameter]["guardrails"]:
                    checks[parameter]["summary"] = True
                    result = checks[parameter]["guardrails"][guardrail]["result"]
                    if isinstance(result, bool) and not result:
                        checks[parameter]["summary"] = False
                        break
            else:
                pass                
    return checks

def checkProposalJSON(proposal):
    checks = {}
    with ExitStack() as stack:
        all_constitutions_files = [stack.enter_context(open(f'./constitutions/constitution_{i}.json')) for i in range(1, 3)]
        all_constitutions = [json.load(f) for f in all_constitutions_files]
    
 
        current_parameter_proposal = proposal["parameter_changes"]
        
        # Static checks
        checks = addStaticCheck(current_parameter_proposal, checks)
        
        # All "uncheckable" checks
        checks = addUncheckableCheck(proposal, all_constitutions, checks)

        # For all the parameters add a "summary" field with True if all guardrails are True, False if any guardrail is False
        for parameter in checks:
            if checks[parameter] is not None:
                for guardrail in checks[parameter]["guardrails"]:
                    checks[parameter]["summary"] = True
                    result = checks[parameter]["guardrails"][guardrail]["result"]
                    if isinstance(result, bool) and not result:
                        checks[parameter]["summary"] = False
                        break
            else:
                pass                
    return checks


if __name__ == "__main__":
    checkProposal()
