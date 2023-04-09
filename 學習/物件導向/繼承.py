class Car:
    def __init__(self, color, seat):
        self.color = color
        self.seat = seat

    def drive(self):  # 區分一般函數與 物件導向函數，物件導向函數的方法()裡要加self
        print(f'My color is {self.color} ,My seat have {self.seat} seats')


class Airport(Car):  # 繼承Car
    def __init__(self, color, seat):
        self.color = color
        self.seat = seat

    def fly(self):
        print("I can fly")

    def drive(self):
        super().drive()  # super會引用父物件(Car)的drive()這個方法
        # 因為繼承Car，所以self.seat與self.color這兩個物件都能用
        print(f'My seat have {self.seat} seats, My color is {self.color}')


#mazda = Car('blue', 4)
# mazda.drive()

flow = Airport('white', 6)
flow.fly()
flow.drive()
