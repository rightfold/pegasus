def arrayMap(f):
    def arrayMap_(xs):
        return [f(x) for x in xs]
    return arrayMap_
