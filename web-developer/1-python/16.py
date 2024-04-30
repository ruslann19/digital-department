class Calculator:
    _last = None

    def __init__(self):
        self._memory = []

    def sum(self, a, b):
        res = a + b
        self.make_log("sum", a, b, res)
        return res
    
    def sub(self, a, b):
        res = a - b
        self.make_log("sub", a, b, res)
        return res
    
    def mul(self, a, b):
        res = a * b
        self.make_log("mul", a, b, res)
        return res
    
    def div(self, a, b, mod=False):
        if mod == True:
            res = a % b
        else:
            res = a / b
        self.make_log("div", a, b, res)
        return res
    
    def history(self, n):
        if n > len(self._memory):
            return None
        return self._memory[-n]

    @property
    def last(self):
        return self._last

    @classmethod
    def clear(cls):
        cls._last = None
        return

    # -----------------------------------------------------

    @staticmethod
    def make_string_log(op, a, b, res):
        return f"{op}({a}, {b}) == {round(res, 1)}"

    def make_self_log(self, op, a, b, res):
        self._memory.append(self.make_string_log(op, a, b, res))
        return
    
    @classmethod
    def make_class_log(cls, op, a, b, res):
        cls._last = cls.make_string_log(op, a, b, res)
        return
    
    def make_log(self, op, a, b, res):
        args = [op, a, b, res]
        self.make_self_log(*args)
        Calculator.make_class_log(*args)
        return
