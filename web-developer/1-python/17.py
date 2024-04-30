class BaseWallet:
    exchange_rate = 1

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    # -------------------------------------------------------

    def __add__(self, other):
        if isinstance(other, BaseWallet):
            money = (self.to_base() + other.to_base()) / self.__class__.exchange_rate
        else:
            money = self.amount + other
        return self.__class__(self.name, money)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        self = self + other
        return self

    # -------------------------------------------------------

    def __sub__(self, other):
        if isinstance(other, BaseWallet):
            money = (self.to_base() - other.to_base()) / self.__class__.exchange_rate
        else:
            money = self.amount - other
        return self.__class__(self.name, money)

    def __rsub__(self, other):
        if isinstance(other, BaseWallet):
            money = (other.to_base() - self.to_base()) / self.__class__.exchange_rate
        else:
            money = other - self.amount
        return self.__class__(self.name, money)
        

    def __isub__(self, other):
        self = self - other
        return self
    
    # -------------------------------------------------------

    def __mul__(self, other):
        return self.__class__(self.name, self.amount * other)

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        self = self * other
        return self

    # -------------------------------------------------------

    def __truediv__(self, other):
        return self.__class__(self.name, self.amount / other)

    def __rtruediv__(self, other):
        return self / other

    def __itruediv__(self, other):
        self = self / other
        return self

    # -------------------------------------------------------

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.amount == other.amount
        return False

    def __str__(self):
        return f"Base Wallet {self.name} {self.amount}"

    def to_base(self):
        return self.amount * self.__class__.exchange_rate

    def spend_all(self):
        if self.amount > 0:
            self.amount = 0

# -------------------------------------------------------

class RubbleWallet(BaseWallet):
    exchange_rate = 1

    def __str__(self):
        return f"Rubble Wallet {self.name} {self.amount}"

class DollarWallet(BaseWallet):
    exchange_rate = 60

    def __str__(self):
        return f"Dollar Wallet {self.name} {self.amount}"

class EuroWallet(BaseWallet):
    exchange_rate = 70

    def __str__(self):
        return f"Euro Wallet {self.name} {self.amount}"
