_mask = 0xffffffff

def intAdd(a):
    def intAdd_(b):
        return (a + b) & _mask
    return intAdd_

def intMul(a):
    def intMul_(b):
        return (a * b) & _mask
    return intMul_

def numAdd(a):
    def numAdd_(b):
        return a + b
    return numAdd_

def numMul(a):
    def numMul_(b):
        return a * b
    return numMul_
