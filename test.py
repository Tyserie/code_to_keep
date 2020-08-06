class Restaurant():
    """The Restaurant class"""

    def __init__(self, name, cuisine):
        """Initialize basic variables"""
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        """Information about restaurant"""
        return print(f"Hospoda {self.name} typ kuchyne, {self.cuisine}.")

    def open_restaurant(self):
        """Information about availability of restaurant"""
        return print(f"Restaurace {self.name} je otevrena!")



moje_restika = Restaurant("Vaclavka", "treti cenova")
erikovo_restika = Restaurant("Mlsna Koza", "domaci kuchyne")
conan_restika = Restaurant("U Conana", "grillovane dobroty")

#print(f"Hospoda {moje_restika.name} byla {moje_restika.cuisine}, ale dobra.")
moje_restika.describe_restaurant()
#moje_restika.open_restaurant()
erikovo_restika.describe_restaurant()
conan_restika.describe_restaurant()


