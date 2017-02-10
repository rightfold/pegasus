_mask = 0xffffffff

def intDegree(x):
    return abs(x) & _mask

def intDiv(a):
    def intDiv_(b):
        return a // b
    return intDiv_

def intMod(a):
    def intMod_(b):
        return a % b
    return intMod_

def numDiv(a):
    def numDiv_(b):
        return a / b
    return numDiv_
