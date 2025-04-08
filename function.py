def greet():
    print("Hello i am ")
    print("i am learning")
    print("my target is to complite in month")


greet()

def greet_by_name(name, sub):
    print(f"Hello i am {name} ")
    print(f"i am learning {sub}")


#  position argument
# greet_by_name("Amy","python")

# keyword argument
greet_by_name(sub="python", name="Amy")


def paint_calc(height, width, cover):
    num_cans = (height * width) / cover


# parameter and argument
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("it's a prime number")
    else:
        print("it's not a prime number")


n = int(input("what is your number"))

prime_checker(n)
