class Cars:
    def __init__(self,name,color):
        self.a = name
        self.b = color
    def introduce(self):
      print(f"My car name is {self.a} and color is {self.b}")
Car1 = Cars("mazuda","blue")
#建立名為Car1的物件
Car1.name = "mazuda2"
Car1.introduce()

print(Car1.name)

#--------------------------------------------
'''
class Demo:
  def set_att(self, a=22, b=33):
    self.__a = a
    self.__b = b
    
  def do_something(self):
    return self.__a + self.__b
    
d = Demo()
d.set_att()
print(d.do_something())
d.__a = 5
print(d.__a)
print(d.do_something())
'''