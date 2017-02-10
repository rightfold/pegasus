def showIntImpl(i):
    return str(i)

def showNumberImpl(n):
    return str(n)

def showCharImpl(c):
    return "'" + repr(c)[1:-1] + "'"

def showStringImpl(s):
    return '"' + repr(s)[1:-1] + '"'

def showArrayImpl(e):
    def showArrayImpl_(a):
        return '[' + ', '.join(e(x) for x in a) + ']'
    return showArrayImpl_
