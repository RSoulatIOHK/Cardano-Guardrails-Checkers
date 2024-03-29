import matplotlib.pyplot as plt
import json
import math

parameterNames = { "0":  "txFeePerByte"
                  , "1":  "txFeeFixed"
                  # , "10": "monetaryExpansion"
                  # , "11": "treasuryCut"
                  , "16": "minPoolCost"
                  , "17": "utxoCostPerByte"
                  , "2":  "maxBlockBodySize"
                  , "22": "maxValueSize"
                  , "23": "collateralPercentage"
                  , "24": "maxCollateralInputs"
                  , "27": "committeeMinSize"
                  , "28": "committeeMaxTermLimit"
                  , "29": "govActionLifeTime"
                  , "30": "govDeposit"
                  , "3":  "maxTxSize"
                  , "31": "dRepDeposit"
                  , "32": "dRepActivity"
                  #, "33": "minFeeRefScriptCoinsPerByte"
                  , "4":  "maxBlockHeaderSize"
                  , "5":  "stakeAddressDeposit"
                  , "6":  "stakePoolDeposit"
                  , "7":  "poolRetireMaxEpoch"
                  , "8":  "stakePoolTargetNum"
                  #, "9":  "poolPledgeInfluence"
                  }
resultsJSON = json.loads(open("single-param.json").read())

fig, axs = plt.subplots(5, 5, figsize=(50, 50))
fig.suptitle('Unit tests')

for num, parameterNum in enumerate(parameterNames):
    x = math.floor(num / 5)
    y = num % 5
    parameter = parameterNames[parameterNum]
    print(resultsJSON[parameterNum])
    if resultsJSON[parameterNum] == []:
        continue
    values = [int(x[0]) for x in resultsJSON[parameterNum]]
    print(f'{parameter}: {len(values)}')
    results = [x[1] for x in resultsJSON[parameterNum]]
    axs[x,y].scatter(values, [0]*len(values), c=['red' if x == False else 'green' for x in results], marker='|')
    passingTests = [x[0] for x in resultsJSON[parameterNum] if x[1] == True]
    if len(passingTests) == 0:
        pass
    else:
        smallestPass = min(passingTests)
        largestPass = max(passingTests)
        axs[x,y].axvline(x=smallestPass, color='green', linestyle='--')
        axs[x,y].axvline(x=largestPass, color='green', linestyle='--')
        axs[x,y].text(smallestPass, 0.2, f"  {smallestPass}", fontsize=8,  horizontalalignment='left' , c='green')
        axs[x,y].text(largestPass , 0.2, f"{largestPass}  " , fontsize=8,  horizontalalignment='right', c='green')
    smallestTested = min(values)
    largestTested = max(values)
    axs[x,y].axvline(x=smallestTested, color='red', linestyle='--')
    axs[x,y].axvline(x=largestTested, color='red', linestyle='--')
    interval1 = [x[0] for x in resultsJSON[parameterNum] if x[1] == False and x[0] < smallestPass]
    interval2 = [x[0] for x in resultsJSON[parameterNum] if x[1] == False and x[0] > largestPass]
    if interval1 == []:
        pass
    else:
        LargestFailBelowSmallestPass = max(interval1, default=None)
        axs[x,y].axvline(x=LargestFailBelowSmallestPass, color='red', linestyle='--')  
        axs[x,y].text(LargestFailBelowSmallestPass, 0.4, f"{LargestFailBelowSmallestPass}  ", fontsize=8,  horizontalalignment='right', c='red')
    if interval2 == []:
        pass
    else:
        smallestFailAboveLargestPass = min(interval2, default=None)
        axs[x,y].axvline(x=smallestFailAboveLargestPass, color='red', linestyle='--')
        axs[x,y].text(smallestFailAboveLargestPass , 0.4, f"  {smallestFailAboveLargestPass}" , fontsize=8,  horizontalalignment='left' , c='red')
    if smallestTested < smallestPass - 0.2*(largestPass - smallestPass):
        axs[x,y].text(smallestPass - 0.2*(largestPass - smallestPass), 0.8, f"<-- {smallestTested}  ", fontsize=8,  horizontalalignment='left', c='red')
    else:
        axs[x,y].text(smallestTested, 0.8, f"{smallestTested}  ", fontsize=8,  horizontalalignment='right', c='red')

    if largestTested > largestPass + 0.2*(largestPass - smallestPass):
        axs[x,y].text(largestPass + 0.2*(largestPass - smallestPass), 0.8, f"  {largestTested} -->", fontsize=8,  horizontalalignment='right', c='red')
    else:
        axs[x,y].text(largestTested , 0.8, f"  {largestTested}" , fontsize=8,  horizontalalignment='left' , c='red')
    axs[x,y].set_title(parameter)
    axs[x,y].spines['top'].set_visible(False)
    axs[x,y].spines['left'].set_visible(False)
    axs[x,y].spines['right'].set_visible(False)
    axs[x,y].set_ylim(-0.1, 1.2)
    axs[x,y].set_xlim(smallestPass - 0.2*(largestPass - smallestPass), largestPass + 0.2*(largestPass - smallestPass))
    fig.subplots_adjust(hspace=0.9)

plt.savefig("./certification/unitTestCoverage.png")