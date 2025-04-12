from unreliable_car import UnreliableCar

def test():
    """Run tests on UnreliableCar class."""
    unreliable_car = UnreliableCar("A", 100, 30)
    for i in range(100):
        unreliable_car.drive(1)
    print(unreliable_car) # Expect odometer to be near 30


if __name__ == "__main__":
    test()
