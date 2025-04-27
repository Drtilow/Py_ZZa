class Order:
    def __init__(self):
        self.pizzas = []
        self.total_price = 0.0

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)
        self.total_price += pizza.price

    def __str__(self):
        return f"Objednávka obsahuje {len(self.pizzas)} pizze. Celková cena: {self.total_price}€"
