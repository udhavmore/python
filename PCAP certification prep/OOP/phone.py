from item import Item


# inheriting item class from other file
class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int = 0, broken_phones: int = 0):
        # Calling Super
        super().__init__(name, price, quantity)
        # Validator
        assert broken_phones >= 0, "Value cannot be less than 0"

        # Assigner
        self.broken_phones = broken_phones

