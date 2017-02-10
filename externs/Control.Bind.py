def arrayBind(xs):
    def arrayBind_(k):
        result = []
        for x in xs:
            result.append(*k(x))
        return result
    return arrayBind_