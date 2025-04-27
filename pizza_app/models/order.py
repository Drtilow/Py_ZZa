class Order:
    def __init__(self):
        self.pizzas = []
        self.total_price = 0.0

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)
        self.total_price += pizza.price

    def __str__(self):
        pizza_list = ', '.join([pizza.name for pizza in self.pizzas])
        return f"Objednávka: {len(self.pizzas)} pizza/y ({pizza_list}) | Celkem: {self.total_price} Kč"
