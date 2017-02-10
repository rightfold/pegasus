def arrayApply(fs):
    def arrayApply_(xs):
        result = []
        for f in fs:
            for x in xs:
                result.append(f(x))
        return result
    return arrayApply_