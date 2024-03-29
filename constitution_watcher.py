import json
from paramMap import paramMap
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
from contextlib import ExitStack
from typing import Any
from pprint import pprint

mapKeyChecks = {
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

def checkGuardrails(value: int, guardrails, proposal = None, constitutions = None):
    check_results = {}
    if guardrails == None:
        return None
    for guardrail in guardrails:
        if proposal == None and constitutions == None:
            result = guardrail["function"](value)
        else:
            result = guardrail["function"](value, proposal, constitutions)
        if guardrail["name"] not in check_results:
            check_results[guardrail["name"]] = {}
        check_results[guardrail["name"]]["value"] = value
        check_results[guardrail["name"]]["result"] = result
        check_results[guardrail["name"]]["description"] = guardrail["description"]
        check_results[guardrail["name"]]["name"] = guardrail["name"]
    return check_results

def staticCheck(proposal, checks):
    for key in proposal:
        paramProposal = proposal[key]
        results = None
        results = checkGuardrails(paramProposal, mapKeyChecks[key]["checkable"])
        checks[paramMap[key]["name"]] = results
        # print(f'Guardrails not checked by script for key {key} (param {paramMap[key]["name"]}) is done')
    return checks

def uncheckableCheck(proposal, all_constitutions, checks):
    for key in proposal["parameter_changes"]:
        paramProposal = proposal["parameter_changes"][key]
        if paramProposal == {}:
            paramProposal = all_constitutions[-1]["parameters_values"][key]
        if mapKeyChecks[key]["uncheckable"] == None:
            continue
        results = checkGuardrails(paramProposal, mapKeyChecks[key]["uncheckable"], proposal, all_constitutions)
        checks[paramMap[key]["name"]] = (checks[paramMap[key]["name"]] | results) 
        # print(f'Guardrails not checked by script for key {key} (param {paramMap[key]["name"]}) is done')
    return checks

def param_checkers(pathfile = './data/proposal.json', outfile = './data/checks.json'):
    checks = {}
    with ExitStack() as stack:
        all_constitutions_files = [stack.enter_context(open(f'./constitutions/constitution_{i}.json')) for i in range(1, 3)]
        all_constitutions = [json.load(f) for f in all_constitutions_files]
        with open(pathfile) as f:
            proposal = json.load(f)
            current_parameter_proposal = proposal["parameter_changes"]
        
        # Static checks
        checks = staticCheck(current_parameter_proposal, checks)
        
        # All "uncheckable" checks
        checks = uncheckableCheck(proposal, all_constitutions, checks)

    # pprint(checks)
    json.dump(checks, open(outfile, 'w'), indent=4)
    return outfile

if __name__ == "__main__":
    param_checkers()