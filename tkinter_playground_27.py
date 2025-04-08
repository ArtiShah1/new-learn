def add(*args):
    # print(type(args))
    # print(args)

    print(args[1])
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(3, 4, 5, 6))

def calculte(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    print(kwargs["multiply"])

    n+= kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculte(2, add=3, multiply =5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")



my_car = Car(make="ford", model="figo_blu" )
print(my_car.model)



