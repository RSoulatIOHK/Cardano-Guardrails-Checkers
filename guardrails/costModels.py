# (✗ - unquantifiable) Cost model values must be set by benchmarking on a reference architecture

# (✗ - primitives and language versions aren’t introduced in transactions) The cost model must be updated if new primitives are introduced or a new Plutus language version is added

# (⧗ - no access to Plutus cost model parameters) Cost model values must not be negative

# (⧗ - no access to Plutus cost model parameters) A cost model must be supplied for each Plutus language version that the protocol supports

# costmdls =
#   { ? 0 : [ 166* int ] ; Plutus v1, only 166 integers are used, but more are accepted (and ignored)
#   , ? 1 : [ 175* int ] ; Plutus v2, only 175 integers are used, but more are accepted (and ignored)
#   , ? 2 : [ 233* int ] ; Plutus v3, only 233 integers are used, but more are accepted (and ignored)
#   , ? 3 : [ int ] ; Any 8-bit unsigned number can be used as a key.
#   }

languages = {"0": 166, "1": 175, "2": 233, "3": 0}

def cm_01(costModel, proposal, constitutions):
    def benchmarking():
        return True
    return benchmarking()

def cm_02(costModel, proposal, constitutions):
    def newPrimitives():
        return True
    def newLanguageVersion():
        return True
    return newPrimitives() or newLanguageVersion()

def cm_03(costModel, proposal, constitutions):
    for key in costModel:
        # print(f'key: {key}, costModel is {costModel["parameter_changes"][key]} and is of type: {type(costModel["parameter_changes"][key])}')
        if type(costModel["parameter_changes"][key]) == list:
            # Let's assume it's a rational disguised, but we're going to run into issues in the future
            # I guarantee it
            costModelProposal = costModel["parameter_changes"][key][0]/costModel["parameter_changes"][key][1]
        elif type(costModel["parameter_changes"][key]) == int:
            costModelProposal = costModel["parameter_changes"][key]
        elif type(costModel["parameter_changes"][key]) == dict and costModel["parameter_changes"][key] != {}:
            for key2 in costModel["parameter_changes"][key]:
                if type(costModel["parameter_changes"][key][key2]) == list:
                    costModelProposal = costModel["parameter_changes"][key][key2][0]/costModel["parameter_changes"][key][key2][1]
                    if costModelProposal < 0:
                        return False
                    else:
                        pass
                else:
                    costModelProposal = costModel["parameter_changes"][key][key2]
                    if costModelProposal < 0:
                        return False
                    else:
                        pass
        else:
            continue
        if costModelProposal < 0:
            return False
    return True

def cm_04(costModel, proposal, constitutions):
    for language in range(3):
        if (language in costModel and costModel[language] < languages[str(language)]):
            return False          
    return True

checkable = []

uncheckable = [
    { "name": "CM-01"
    , "description": "Cost model values must be set by benchmarking on a reference architecture"
    , "function": cm_01
    },
    { "name": "CM-02"
    , "description": "The cost model must be updated if new primitives are introduced or a new Plutus language version is added"
    , "function": cm_02
    },
    { "name": "CM-03"
    , "description": "Cost model values must not be negative"
    , "function": cm_03
    },
    { "name": "CM-04"
    , "description": "A cost model must be supplied for each Plutus language version that the protocol supports"
    , "function": cm_04
    }
]