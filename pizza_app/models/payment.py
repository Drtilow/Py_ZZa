class PaymentMethod:
    def pay(self, amount):
        raise NotImplementedError

class CardPayment(PaymentMethod):
    def pay(self, amount):
        return f"Zaplaceno kartou {amount} Kč."

class CashPayment(PaymentMethod):
    def pay(self, amount):
        return f"Zaplaceno hotově {amount} Kč."
