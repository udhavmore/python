import csv


class Item:
    # Globals
    disc = 0.8
    all = []

    # If a parameter has default value then it becomes an optional parameter
    def __init__(self, name: str, price: float, quantity=0):
        # Validator
        assert price >= 0, "Value cannot be less than 0"
        assert quantity >= 0, "Value cannot be less than 0"

        # Assigner
        self.__name = name
        self.price = price
        self.quantity = quantity

        # Action
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    def calculate(self):
        return self.price * self.quantity

    def apply_disc(self):
        self.price = self.price * self.disc

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv') as file:
            reader = csv.DictReader(file)
            items = list(reader)

            for item in items:
                Item(
                    name=item.get('name'),
                    price=float(item.get('price')),
                    quantity=int(item.get('quantity'))
                )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}',{self.price},{self.quantity})"


