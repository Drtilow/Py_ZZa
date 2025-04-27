def show_main_menu():
    print("\n=== Pizza aplikace ===")
    print("1. Vytvořit objednávku")
    print("2. Platba")
    print("3. Admin menu")
    print("4. Ukončit aplikaci")
    return input("Zvol možnost: ")

def show_pizza_menu():
    print("\nVyber druh pizzy:")
    print("1. Margherita (120 Kč)")
    print("2. Pepperoni (150 Kč)")
    print("3. Hawai (140 Kč)")
    print("4. Speck e funghi (160 Kč)")
    print("5. Quatro Stagioni (170 Kč)")
    print("6. Salami (155 Kč)")
    return input("Zadej volbu: ")
