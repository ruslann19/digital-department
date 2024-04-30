def get_balance(name, transactions):
    balance = 0
    for transaction in transactions:
        if transaction["name"] == name:
            balance += transaction["amount"]
    return balance

def count_debts(names, amount, transactions):
    debts = {}
    for name in names:
        balance = get_balance(name, transactions)
        if balance < amount:
            debts[name] = amount - balance
        else:
            debts[name] = 0
    return debts

# transactions = [ {"name": "Василий", "amount": 500}, {"name": "Петя", "amount": 100}, {"name": "Василий", "amount": -300}, ]

# print(get_balance("Василий", transactions))

# print(count_debts(["Василий", "Петя", "Вова"], 150, transactions))
