def concatString(a):
    def concatString_(b):
        return a + b
    return concatString_

def concatArray(xs):
    def concatArray_(ys):
        return xs + ys
    return concatArray_
