class Car:

    def __init__(self, speed: int = 30, name: str = "None"):
        self.speed = speed
        self.name = name


if __name__ == "__main__":
    car = Car()
    print(car.speed)
    print(car.name)
    car.name = "lada"
    car.speed = "20"
    print(car.speed)
    print(car.name)
    print(car)