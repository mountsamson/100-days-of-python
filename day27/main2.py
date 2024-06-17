# def add(*dick):
#     print(dick[3])
    
#     sum = 0
#     for n in dick:
#         sum += n
#     return sum
    
    
    
# # print(add(1, 2, 3, 4, 5))

# def calculate(**kwargs):
#     print(kwargs)
#     # for key, value in kwargs.items():
#     #     print(key)
#     #     print(value)
#     n += kwargs["add"]
#     n *= kwargs['mutiply']
#     print(n)
    
    
# calculate(2, add=3, mutiply=5)

class Car:
    
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw['model']
            
my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)
    
    
