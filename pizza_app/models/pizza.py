class Pizza:
    def __init__(self, name, size, price):
        self.name = name
        self.size = size
        self.price = price
        self.toppings = []

    def add_topping(self, topping):
        self.toppings.append(topping)
        self.price += topping.price

class PizzaFactory:
    @staticmethod
    def create_pizza(choice):
        if choice == '1':
            return Pizza('Margherita', 'medium', 120)
        elif choice == '2':
            return Pizza('Pepperoni', 'medium', 150)
        elif choice == '3':
            return Pizza('Hawai', 'medium', 140)
        elif choice == '4':
            return Pizza('Speck e funghi', 'medium', 160)
        elif choice == '5':
            return Pizza('Quatro Stagioni', 'medium', 170)
        elif choice == '6':
            return Pizza('Salami', 'medium', 155)
        else:
            return None
