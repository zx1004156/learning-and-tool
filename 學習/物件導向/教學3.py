# 1.類別 2.屬性 3.方法 4.給他一個物件
# 1.類別 2.初始化__init__ 3.self 與 參數
# 我想要建兩個藍圖 一個飛機 一個車子

class Mix:
    def __init__(self, color, seat):
        self.color111 = color
        self.seat222 = seat


class Airplane(Mix):  # self拿來區分 是外面變數 還是 物件導向裡的變數
    # def __init__(self, color, seat):
    #self.color111 = color
    #self.seat222 = seat

    def fly(self):
        print(f"MY Airplane color {self.color111}")


class Car(Mix):
    # def __init__(self, color, seat):
    #self.color111 = color
    #self.seat222 = seat

    def drive(self):
        print(f"MY Car color {self.color111}")


Fly = Airplane("white", 4)

mazda = Car("black", 6)

print(Fly.fly())

print(mazda.drive())

print(Fly.color111)
