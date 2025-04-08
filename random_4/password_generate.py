import random

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
           'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbol = ['!','@','#','$','%','^','&','*','+']

print("welcome to the password generator!")
nr_letters = int(input("how many letters would you like in your password?/n"))
nr_symbols = int(input("how many symbols would you like ?/n"))
nr_number = int(input("how many number would you like?/n"))

# random passwoed print 4 letters, 2 symbol, 2 numbers

# password = ""
# for char in range(1, nr_letters +1):
#     password += random.choice(letters)
#
# for char in range(1, nr_symbols +1):
#     password += random.choice(symbol)
#
# for char in range(1, nr_number +1):
#     password += random.choice(numbers)
#
#      print(password)


    # ------------------------------
    # HARD random placed 12 digit password

password_list = []

for char in range(1, nr_letters +1):
    password_list.append(random.choice(letters))

for char in range(1, nr_symbols +1):
    password_list += random.choice(symbol)

for char in range(1, nr_number +1):
    password_list += random.choice(numbers)
    print(password_list)
    random.shuffle(password_list)
    print(password_list)

password = ""
for char in password_list :
   password += char

print(f"your password is : {password}")

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def jump():
#     move ()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

number_of_hurdles = 6
while number_of_hurdles > 0:
    # jump()
    number_of_hurdles -= 1
    print(number_of_hurdles)
    print ()


