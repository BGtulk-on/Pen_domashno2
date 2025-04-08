class BusPassengeritos:
    def __init__(self, passengers):
        self.passengers = passengers
        self.index = 0
    
    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        if self.index < len(self.passengers):
            passenger = self.passengers[self.index]
            self.index += 1
            return passenger
        raise StopIteration


def greet_passengers():
    passenger_names = ["Иванка", "Марийка", "Джеорджия", "Елица", "Петранос"]
    
    bus = BusPassengeritos(passenger_names)
    
    print("Здр на всеки пасажер:")
    for passenger in bus:
        print(f"Хеллоу, {passenger}! Добре дошъл на кораба Яхта.")


if __name__ == "__main__":
    greet_passengers()
