class ParkingSpot:
    """Represents a basic car parking spot."""

    def __init__(self, spot_number, location, base_price):
        self.spot_number = spot_number
        self.location = location
        self.__base_price = base_price

    # Getter
    def get_base_price(self):
        """Returns the base parking price."""
        return self.__base_price

    # Setter
    def set_base_price(self, new_price):
        """Changes the base price if it is greater than zero."""
        if new_price > 0:
            self.__base_price = new_price
            print("Base price successfully changed!")
        else:
            print("Error: Price must be greater than zero.")

    def calculate_price(self, hours):
        """Calculates the total parking price."""
        return self.get_base_price() * hours


class PremiumParkingSpot(ParkingSpot):
    """Represents a premium parking spot with an extra hourly fee."""

    def __init__(self, spot_number, location, base_price, extra_fee):
        super().__init__(spot_number, location, base_price)
        self.extra_fee = extra_fee

    def calculate_price(self, hours):
        """Calculates parking price including the premium fee."""
        return (self.get_base_price() + self.extra_fee) * hours


# Main program
normal_spot = ParkingSpot(1, "Ground floor", 2.0)

premium_spot = PremiumParkingSpot(
    2, "First floor", 2.0, 1.5
)

print("=== CAR PARKING SYSTEM ===")

print("\nNormal parking spot:")
print("Spot number:", normal_spot.spot_number)
print("Location:", normal_spot.location)
print("Price per hour:", normal_spot.get_base_price(), "EUR")
print("Total for 3 hours:", normal_spot.calculate_price(3), "EUR")

print("\nPremium parking spot:")
print("Spot number:", premium_spot.spot_number)
print("Location:", premium_spot.location)
print("Price per hour:", premium_spot.get_base_price(), "EUR")
print("Total for 3 hours:", premium_spot.calculate_price(3), "EUR")

print("\n=== CHANGING PARKING PRICE ===")
normal_spot.set_base_price(3.0)

print("New price:", normal_spot.get_base_price(), "EUR")
print("New total for 3 hours:",
      normal_spot.calculate_price(3), "EUR")
