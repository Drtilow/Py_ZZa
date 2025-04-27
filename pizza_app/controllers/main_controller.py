from views.ui import show_main_menu, show_pizza_menu
from models.pizza import PizzaFactory
from models.order import Order
from models.sales import Sales
from models.payment import CardPayment, CashPayment


def main():
    sales = Sales.get_instance()
    order = Order()

    while True:
        choice = show_main_menu()

        if choice == '1':
            pizza_choice = show_pizza_menu()
            pizza = PizzaFactory.create_pizza(pizza_choice)

            if pizza:
                order.add_pizza(pizza)
                print(f"Přidána pizza: {pizza.name}, cena: {pizza.price} Kč")
            else:
                print("Neplatná volba pizzy!")

        elif choice == '2':
            if order.total_price > 0:
                print("\nVyber způsob platby:")
                print("1. Kartou")
                print("2. Hotově")
                payment_choice = input("Zadej volbu platby: ")

                if payment_choice == '1':
                    payment_method = CardPayment()
                elif payment_choice == '2':
                    payment_method = CashPayment()
                else:
                    print("Neplatná volba platby!")
                    continue

                print(payment_method.pay(order.total_price))
                sales.add_order(order)
                order = Order()  # vytvoříme novou prázdnou objednávku

            else:
                print("Objednávka je prázdná!")

        elif choice == '3':
            print("\n--- Admin menu: Přehled všech objednávek ---")
            all_sales = sales.show_sales()
            if all_sales:
                for order_info in all_sales:
                    print(order_info)
            else:
                print("Žádné objednávky k zobrazení.")

        elif choice == '4':
            print("Aplikace byla ukončena.")
            break

        else:
            print("Neplatná volba, zkus to znovu.")


if __name__ == "__main__":
    main()
