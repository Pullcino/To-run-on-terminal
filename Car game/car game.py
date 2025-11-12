class car :

    def __init__(self, Brand, Model, Color):

        self.Brand = Brand
        self.Model = Model
        self.Color = Color
        self.Speed = 0

    def accelerate(self):

        self.Speed += 10

        print(f"Actual speed: {self.Speed} km/h")

    def reduce_speed(self):

        self.Speed -= 10

        if self.Speed < 0:

            self.Speed = 0

        print(f"Actual speed: {self.Speed} km/h")

    def show_info(self):

        print(f"Brand: {self.Brand}, Model: {self.Model}, Color: {self.Color}")


car_list = []

while True:

    print("\n---- Menu ----")
    print("1 - Add a new car")
    print("2 - Show cars information")
    print("3 - Accelerate a car")
    print("4 - Reduce a car")
    print("5 Leave")

    choose = input("Choose one between the options: ")

    if choose == "1":

        Brand = input("Type the car make: ")
        Model = input("Type the car Model: ")
        Color = input("Type the car Color: ")

        New_car = car(Brand, Model, Color)
        car_list.append(New_car)

    elif choose == "2":

        if car_list:

            for car in car_list:

                car.show_info()

        else:

            print("You haven't added any cars yet.")

    elif choose == "3":

        Model = input("Type the car model you wanna accelerate: ")

        for car in car_list:

            if car.Model == Model:

                car.accelerate()
                break

    elif choose == "4":

        Model = input("Type the car model you wanna reduce: ")

        for car in car_list:

            if car.Model == Model:

                car.reduce_speed()
                break

    elif choose == "5":

        print("Leaving the program")

        break

    else:

        print("Try again")

