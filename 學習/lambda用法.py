from functools import reduce

title = "HelloPython"
(lambda title: print(title))(title)
print((lambda x,y:x*y)(4,2))

numbers = [50,2,12,30,27,4]
result = filter(lambda x:x>10,numbers)
print(list(result))

result2 = map(lambda x:x*2 , numbers)
print(list(result2))

result3 = reduce(lambda x,y:x+y,numbers)
print(result3)

cars = [
    ("mazda",2000),
    ("toyata",1000),
    ("benz",5000)
]
print(sorted(cars, key=lambda car: car[1]))

a = filter(lambda x: x % 2 == 0, range(10))
print(list(a))