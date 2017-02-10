def unsafeCompareImpl(lt):
    def unsafeCompareImpl_(eq):
        def unsafeCompareImpl__(gt):
            def unsafeCompareImpl___(x):
                def unsafeCompareImpl____(y):
                    if x < y:
                        return lt
                    if x == y:
                        return eq
                    return gt
                return unsafeCompareImpl____
            return unsafeCompareImpl___
        return unsafeCompareImpl__
    return unsafeCompareImpl_