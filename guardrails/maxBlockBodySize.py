# (✗ - “exceptional circumstances”) maxBlockBodySize must not be decreased, other than in exceptional circumstances
# (⧗ - no access to existing parameter values) maxBlockBodySize must be large enough to include at least one transaction plus the block header (maxBlockBodySize must be at least maxTxSize plus maxBlockHeaderSize)
# (✗ - "should") maxBlockBodySizeshould be changed by at most 10,240 Bytes (10KB) per epoch (5 days), and preferably by 8,192 Bytes (8KB) or less per epoch

# (✓) maxBlockBodySize must not exceed 122,880 Bytes (120KB)
# (✓) maxBlockBodySize must not be less than 24,576 Bytes (24KB)
# (✗ - "should") maxBlockBodySize should not induce an additional TCP round trip.  Any increase beyond this needs careful analysis

def mbbs_01(maxBlockBodySize, proposal, constitutions):
    # Find latest non current constitution
    latest_constitution = constitutions[-1]
    return (maxBlockBodySize >= latest_constitution["parameters_values"]["2"])
        
def mbbs_02(maxBlockBodySize, proposal, constitutions):
    # Find latest non current constitution
    latest_constitution = constitutions[-1]
    if "3" in proposal:
        maxTxSize = proposal["3"]
    else:
        maxTxSize = latest_constitution["parameters_values"]["3"]
    if "4" in proposal:
        maxBlockHeaderSize = proposal["4"]
    else:
        maxBlockHeaderSize = latest_constitution["parameters_values"]["4"]
    return (maxBlockBodySize >= maxTxSize + maxBlockHeaderSize)

def mbbs_03(maxBlockBodySize, proposal, constitutions):
    #Find the constitution that was in effect at the last epoch
    current_epoch = proposal["start_epoch"]
    epoch_5_days_ago = current_epoch - 1
    for constitution in constitutions:
        if epoch_5_days_ago >= constitution["epoch"]:
            constitution_5_days_ago = constitution
            break
    return (maxBlockBodySize - constitution_5_days_ago["parameters_values"]["2"])


def mbbs_04(maxBlockBodySize):
    return maxBlockBodySize <= 122880

def mbbs_05(maxBlockBodySize):
    return maxBlockBodySize >= 24576


def mbbs_06(maxBlockBodySize, proposal, constitutions):
    def TCP_simulation():
        return True
    
    return TCP_simulation()

checkable = [
    { "name": "MBBS-04"
    , "description": "maxBlockBodySize must not exceed 122,880 Bytes (120KB)"
    , "function": mbbs_04
    },
    { "name": "MBBS-05"
    , "description": "maxBlockBodySize must not be less than 24,576 Bytes (24KB)"
    , "function": mbbs_05
    }
]

uncheckable = [
    { "name": "MBBS-01"
    , "description": "maxBlockBodySize must not be decreased, other than in exceptional circumstances"
    , "function": mbbs_01
    },
    { "name": "MBBS-02"
    , "description": "maxBlockBodySize must be large enough to include at least one transaction plus the block header (maxBlockBodySize must be at least maxTxSize plus maxBlockHeaderSize)"
    , "function": mbbs_02
    },
    { "name": "MBBS-03"
     , "description": "maxBlockBodySize should be changed by at most 10,240 Bytes (10KB) per epoch (5 days), and preferably by 8,192 Bytes (8KB) or less per epoch"
     , "function": mbbs_03
    },
    { "name": "MBBS-06"
    , "description": "maxBlockBodySize should not induce an additional TCP round trip.  Any increase beyond this needs careful analysis"
    , "function": mbbs_06
    }
]