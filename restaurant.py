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

    def __init__(self, name, cuisine):
        super().__init__(name, cuisine)
        self.flavor = 'vanila, stracatella, crenberies, pistacia'

    def display_flavor(self):
        a = str(self.flavor)[0:]
        return a


iceCream = IceCreamStand("Zmrzlinarna", "zmrzlina")
print(f"Ice shop {iceCream.name} offers {iceCream.cuisine} in following flavors, {iceCream.display_flavor()}.")
#iceCream.display_flavor()






#conan_restika = Restaurant("U Conana", "grillovane dobroty")
#conan_restika.set_number_served(12)
#conan_restika.increment_number_served(12)
#print(f"{conan_restika.name} served {conan_restika.number_served} customers!")


#moje_restika = Restaurant("Vaclavka", "treti cenova")
#erikovo_restika = Restaurant("Mlsna Koza", "domaci kuchyne")
#print(f"Hospoda {moje_restika.name} byla {moje_restika.cuisine}, ale dobra.")
#moje_restika.describe_restaurant()
#moje_restika.open_restaurant()
#erikovo_restika.describe_restaurant()
