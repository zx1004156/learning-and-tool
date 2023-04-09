#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
class FooParent(object):
    def __init__(self):
        self.parent = 'I\'m the parent.' #(3) (11)
        print ('Parent')#初始化瞬間就會執行，也就是此class被引用之時 (4)
    
    def bar(self,message):
        print ("%s from Parent" % message) #(8)
 
class FooChild(FooParent):
    def __init__(self):
        # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类 FooChild 的对象转换为类 FooParent 的对象
        super(FooChild,self).__init__()#繼承此class的父物件 (2)    
        print ('Child')#初始化瞬間就會執行，也就是此class被引用之時 (5)
        
    def bar(self,message):
        super(FooChild, self).bar(message)#執行FooChild 的 父物件 的 bar方法 (7)
        print ('Child bar fuction') #(9)
        print (self.parent)#此屬性在FooParent的class，因繼承，因此有此屬性 (10)
 
if __name__ == '__main__':
    fooChild = FooChild() #(1)
    fooChild.bar('HelloWorld') #(6)