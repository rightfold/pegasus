def foldrArray(f):
    def foldrArray_(init):
        def foldrArray__(xs):
            acc = init
            for x in reversed(xs):
                acc = f(x)(acc)
            return acc
        return foldrArray__
    return foldrArray_

def foldlArray(f):
    def foldlArray_(init):
        def foldlArray__(xs):
            acc = init
            for x in xs:
                acc = f(acc)(x)
            return acc
        return foldlArray__
    return foldlArray_
