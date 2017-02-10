def boolConj(a):
    def boolConj_(b):
        return a and b
    return boolConj_

def boolDisj(a):
    def boolDisj_(b):
        return a or b
    return boolDisj_

def boolNot(a):
    return not a
