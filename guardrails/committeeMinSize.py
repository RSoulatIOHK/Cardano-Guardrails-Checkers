# (✓) committeeMinSize must not be negative

# (✓) committeeMinSize must not be less than 3

# (✓) committeeMinSize must not be more than 10

def cms_01(committeeMinSize):
    return committeeMinSize >= 0

def cms_02(committeeMinSize):
    return committeeMinSize >= 3

def cms_03(committeeMinSize):
    return committeeMinSize <= 10

checkable = [
    { "name": "CMS-01"
    , "description": "committeeMinSize must not be negative"
    , "function": cms_01
    },
    { "name": "CMS-02"
    , "description": "committeeMinSize must not be less than 3"
    , "function": cms_02
    },
    { "name": "CMS-03"
    , "description": "committeeMinSize must not be more than 10"
    , "function": cms_03
    }
]

uncheckable = []
