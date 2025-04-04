from taxi import Taxi


def test_taxi():
    """Test taxi class features."""
    my_taxi = Taxi("Prius 1", 100, 1.23)
    assert my_taxi.drive(40) == 40
    assert my_taxi.get_fare() == 40*1.23
    print(my_taxi)

    my_taxi.start_fare()
    assert my_taxi.drive(100) == 60
    assert my_taxi.current_fare_distance == 60
    assert my_taxi.get_fare() == 60*1.23
    print(my_taxi)

if __name__ == "__main__":
    test_taxi()
