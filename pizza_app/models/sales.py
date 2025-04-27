class Sales:
    __instance = None

    def __init__(self):
        if Sales.__instance is not None:
            raise Exception("Singleton class already exists!")
        self.orders = []
        Sales.__instance = self

    @staticmethod
    def get_instance():
        if Sales.__instance is None:
            Sales()
        return Sales.__instance

    def add_order(self, order):
        self.orders.append(order)

    def show_sales(self):
        return [str(order) for order in self.orders]
