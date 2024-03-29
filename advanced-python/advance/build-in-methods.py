class Currency:
    def __init__(self, code, exchange_to_usd):
        self.amount = 0.00
        self.code = code
        self.exchange_to_usd = exchange_to_usd

    # Not necessary but interesting. in python we can do pounds.amount = 15
    def set_amount(self, amount):
        self.amount = amount

    def in_currency(self, amount):
        return amount / self.exchange_to_usd

    def to_usd(self, amount=None):
        to_convert = amount if amount is not None else self.amount
        return to_convert * self.exchange_to_usd

    # Build-in-method: Greater than
    # others: lt: less than, le: less than or equal... etc
    def __gt__(self, other):
        return self.to_usd() > other.to_usd()

pounds = Currency("GBP", 1.21)
euros = Currency("EUR", 1.07)

euros.set_amount(500)
pounds.set_amount(500)
print(pounds.in_currency(1000))
print(pounds.to_usd())
print(pounds.to_usd(1000))

print(pounds.exchange_to_usd > euros.exchange_to_usd)

print(pounds > euros) # pounds __gt__