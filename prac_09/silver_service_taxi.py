from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Inherit from taxi."""
    FLAG_FALL = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance.

        fanciness: float, multiplier for price_per_km
        """
        super().__init__(name, fuel)
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string like taxi but with flagfall."""
        return super().__str__() + f" plus flagfall of ${self.FLAG_FALL:.2f}"

    def get_fare(self):
        """Return the fare of trip with an initial flag fare."""
        return self.FLAG_FALL + super().get_fare()
