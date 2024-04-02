
from guardrails import (
    txFeeFixed,
    txFeePerByte,
    utxoCostPerByte,
    stakeAddressDeposit,
    stakePoolDeposit,
    minPoolCost,
    treasuryCut,
    monetaryExpansion,
    maxBlockBodySize,
    maxTxSize,
    maxBlockHeaderSize,
    poolRetireMaxEpoch,
    stakePoolTargetNum,
    poolPledgeInfluence,
    costModels,
    maxValueSize,
    collateralPercentage,
    maxCollateralInputs,
    maxBlockExecutionUnits,
    maxTxExecutionUnits,
    executionUnitPrices,
    govActionLifetime,
    committeeMinSize,
    committeeMaxTermLimit,
    govDeposit,
    dRepDeposit,
    dRepActivity,
    minFeeRefScriptCoinsPerByte
)

guardrailChecksList = {
    "txFeePerByte": {
        "checkable": txFeePerByte.checkable,
        "uncheckable": txFeePerByte.uncheckable
    },
    "txFeeFixed": {
        "checkable": txFeeFixed.checkable,
        "uncheckable": txFeeFixed.uncheckable
    },
    "maxBlockBodySize": {
        "checkable": maxBlockBodySize.checkable,
        "uncheckable": maxBlockBodySize.uncheckable
    },
    "maxTxSize": {
        "checkable": maxTxSize.checkable,
        "uncheckable": maxTxSize.uncheckable
    },
    "maxBlockHeaderSize": {
        "checkable": maxBlockHeaderSize.checkable,
        "uncheckable": maxBlockHeaderSize.uncheckable
    },
    "stakeAddressDeposit": {
        "checkable": stakeAddressDeposit.checkable,
        "uncheckable": stakeAddressDeposit.uncheckable
    },
    "stakePoolDeposit": {
        "checkable": stakePoolDeposit.checkable,
        "uncheckable": stakePoolDeposit.uncheckable
    },
    "poolRetireMaxEpoch": {
        "checkable": poolRetireMaxEpoch.checkable,
        "uncheckable": poolRetireMaxEpoch.uncheckable
    },
    "stakePoolTargetNum": {
        "checkable": stakePoolTargetNum.checkable,
        "uncheckable": stakePoolTargetNum.uncheckable
    },
    "poolPledgeInfluence": {
        "checkable": poolPledgeInfluence.checkable,
        "uncheckable": poolPledgeInfluence.uncheckable
    },
    "monetaryExpansion": {
        "checkable": monetaryExpansion.checkable,
        "uncheckable": monetaryExpansion.uncheckable
    },
    "treasuryCut": {
        "checkable": treasuryCut.checkable,
        "uncheckable": treasuryCut.uncheckable
    },
    "minPoolCost": {
        "checkable": minPoolCost.checkable,
        "uncheckable": minPoolCost.uncheckable
    },
    "utxoCostPerByte": {
        "checkable": utxoCostPerByte.checkable,
        "uncheckable": utxoCostPerByte.uncheckable
    },
    "costModels": {
        "checkable": costModels.checkable,
        "uncheckable": costModels.uncheckable
    },
    "executionUnitPrices": {
        "checkable": executionUnitPrices.checkable,
        "uncheckable": executionUnitPrices.uncheckable
    },
    "maxTxExecutionUnits": {
        "checkable": maxTxExecutionUnits.checkable,
        "uncheckable": maxTxExecutionUnits.uncheckable
    },
    "maxBlockExecutionUnits": {
        "checkable": maxBlockExecutionUnits.checkable,
        "uncheckable": maxBlockExecutionUnits.uncheckable
    },
    "maxValueSize": {
        "checkable": maxValueSize.checkable,
        "uncheckable": maxValueSize.uncheckable
    },
    "collateralPercentage": {
        "checkable": collateralPercentage.checkable,
        "uncheckable": collateralPercentage.uncheckable
    },
    "maxCollateralInputs": {
        "checkable": maxCollateralInputs.checkable,
        "uncheckable": maxCollateralInputs.uncheckable
    },
    "committeeMinSize": {
        "checkable": committeeMinSize.checkable,
        "uncheckable": committeeMinSize.uncheckable
    },
    "committeeMaxTermLimit": {
        "checkable": committeeMaxTermLimit.checkable,
        "uncheckable": committeeMaxTermLimit.uncheckable
    },
    "govActionLifetime": {
        "checkable": govActionLifetime.checkable,
        "uncheckable": govActionLifetime.uncheckable
    },
    "govDeposit": {
        "checkable": govDeposit.checkable,
        "uncheckable": govDeposit.uncheckable
    },
    "dRepDeposit": {
        "checkable": dRepDeposit.checkable,
        "uncheckable": dRepDeposit.uncheckable
    },
    "dRepActivity": {
        "checkable": dRepActivity.checkable,
        "uncheckable": dRepActivity.uncheckable
    },
    "minFeeRefScriptCoinsPerByte": {
        "checkable": minFeeRefScriptCoinsPerByte.checkable,
        "uncheckable": minFeeRefScriptCoinsPerByte.uncheckable
    }
}
