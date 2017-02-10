def ordArrayImpl(f):
    def ordArrayImpl_(xs):
        def ordArrayImpl__(ys):
            for x, y in xs.zip(ys):
                o = f(x)(y)
                if o != 0:
                    return o
            xs_len = len(xs)
            ys_len = len(ys)
            if xs_len == ys_len:
                return 0
            if xs_len < ys_len:
                return -1
            return 1
        return ordArrayImpl__
    return ordArrayImpl_
