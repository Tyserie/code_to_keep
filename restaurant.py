class Restaurant():
    """The Restaurant class"""

    def __init__(self, name, cuisine):
        """Initialize basic variables"""
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        """Information about restaurant"""
        return print(f"Hospoda {self.name} typ kuchyne, {self.cuisine}.")

    def open_restaurant(self):
        """Information about availability of restaurant"""
        return print(f"Restaurace {self.name} je otevrena!")

    def set_number_served(self, served):
        """change number served"""
        self.number_served = served

    def increment_number_served(self, increment):
        """Increment number served"""
        self.number_served += increment

class IceCreamStand(Restaurant):
    """Ice cream class"""

    def __init__(self, name, cuisine):
        """Initialise attributes of the parent class """
        super().__init__(name, cuisine)
        self.flavor = 'vanila, stracatella, crenberies, pistacia'

    def display_flavor(self):
        """Prints the flavors"""
        a = str(self.flavor)[0:]
        return a


iceCream = IceCreamStand("Zmrzlinarna", "zmrzlina")
print(f"Ice shop {iceCream.name} offers {iceCream.cuisine} in following flavors, {iceCream.display_flavor()}.")
