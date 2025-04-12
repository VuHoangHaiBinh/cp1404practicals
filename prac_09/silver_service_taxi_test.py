from silver_service_taxi import SilverServiceTaxi


def test():
    """Run tests for silver service taxi class."""
    silver_service_taxi = SilverServiceTaxi("Hummer", 200, 4)
    assert str(silver_service_taxi) == "Car name=Hummer, fuel=200, odometer=0, 0km on current fare, $4.92/km plus flagfall of $4.50"

    silver_service_taxi = SilverServiceTaxi("Hummer", 200, 2)
    silver_service_taxi.drive(18)
    assert silver_service_taxi.get_fare() == 48.80


if __name__ == "__main__":
    test()
