class T:
    def __init__(self, S, V):
        self.S = S
        self.V = V


class M(T):
    def __init__(self,S, V):
        super().__init__(S, V)


class B(T):
    def __init__(self,S, V):
        super().__init__(S, V)