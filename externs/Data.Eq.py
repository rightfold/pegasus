def refEq(a):
    def refEq_(b):
        return a == b
    return refEq_

def refIneq(a):
    def refIneq_(b):
        return a != b
    return refIneq_

def eqArrayImpl(f):
    def eqArrayImpl_(xs):
        def eqArrayImpl__(ys):
            for x, y in xs.zip(ys):
                if not f(x)(y):
                    return False
            return True
        return eqArrayImpl__
    return eqArrayImpl_
