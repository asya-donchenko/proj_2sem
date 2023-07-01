# создание класса транспортное средство
class Transport:
    def __init__(self, max_speed, num_wheels):
        self.max_speed = max_speed
        self.num_wheels = num_wheels

    def drive(self):
        print("Движение:")

# создание класса автомобиль
class Car(Transport):
    def __init__(self, max_speed, num_wheels, brand):
        super().__init__(max_speed, num_wheels)
        self.brand = brand

    # метод заставляет автомобиль ехать
    def drive(self):
        super().drive()
        print("Автомобиль едет")

    # метод заставляет автомобиль сигналить
    def honk(self):
        print("бип-бип")

# создание класса мотоцикл
class Motorcycle(Transport):
    def __init__(self, max_speed, num_wheels, has_sidecar):
        super().__init__(max_speed, num_wheels)
        self.has_sidecar = has_sidecar

    # метод заставляет мотоцикл ехать
    def drive(self):
        super().drive()
        print("Мотоцикл едет")

    # метод заставляет мотоцикл ехать на заднем колесе
    def wheelie(self):
        print("Мотоцикл едет на заднем колесе")


# Создание экземпляров классов
car = Car(200, 4, "Toyota")
motorcycle = Motorcycle(180, 2, False)

# Обращение к свойствам и методам экземпляров
print(car.max_speed)
print(motorcycle.num_wheels)

car.drive()
car.honk()

motorcycle.drive()
motorcycle.wheelie()
