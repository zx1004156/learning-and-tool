class student():
    def __init__(self,gender,number,name):
        self.gender = gender
        self.number = number 
        self.name = name

class subject(student):
    def __init__(self,gender,number,name,sub):
        super().__init__(gender,number,name)
        self.sub = sub
    
    def read(self):
        if self.name == 'Marie':
            print("{} like {}".format(self.name,self.sub))


Jack = subject('male','V123456','Marie','math')
Jack.read()