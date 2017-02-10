_mask = 0xffffffff

def intSub(a):
    def intSub_(b):
        return (a - b) & _mask
    return intSub_

def numSub(a):
    def numSub_(b):
        return a - b
    return numSub_
