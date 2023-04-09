class Cars:

    # init 目的是 在class裡面建立參數 與 把參數從外傳到內
    # 建構式 init初始化
    def __init__(self, color, seat):  # Cars(color,seat) class與init一起看
        self.color123 = color  # 顏色屬性
        self.seat123 = seat  # 座位屬性

    # 方法(Method)

    def drive(self):
        print(f"My car is {self.color123} and has {self.seat123} seats.")


mazda = Cars("blue", 4)  # 解讀從這裡開始解讀
mazda.drive()
