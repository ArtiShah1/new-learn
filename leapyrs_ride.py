numberofLetters = len("AmyPushandhabalia")
print(numberofLetters)

year = int(input("year"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("this is a leap year")
        else:
            print("not a leap year")
    else:
        print("leap year")
else:
    print("this is not a leap year")

#     height = int(input("what is your height in cm"))
#     bill =0
# if height >= 120:
#  print("you can ride the roller_coaster")
#  age = int(input("what is your age"))
# if age < 12:
#     bill = 5
#     print("child tkts are $5 ")
# elif age <= 18:
#     bill = 12
#     print("adult tkts are $12")
#
# wants_photo = input("do you want to take photots? Y or N ")
# if wants_photo == "Y":
#     bill += 3
# print(f"your final bill amount {bill}")
# print("enjoy your ride!")

size = (input("what size pizza do you want? S, M, L"))
extra_cheese = (input("do you want to add extra cheese? Y or N"))
add_pepperoni = (input("do you like to add pepperoni? Y or N "))

bill = 0

if size == "s":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

    if add_pepperoni == "Y":
        if size == "s":
            bill += 2
        else:
            bill += 3
if extra_cheese == "Y":
    bill += 1
print(f"your final bill is : ${bill}")

# ------------------------
# Love calculator game

name1 = input("what is your name?")
name2 = input("what is there name?")

combine_name = name1 + name2
lower_names = combine_name.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t+r+u+e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit =l+o+v+e

score = int(str(first_digit) + str(second_digit))
if (score<10) or (score>90):
    print(f"your score is {score}, you go together like coke and mentos")
elif (score>= 40) and (score<=50):
    print(f"your score is {score}, you are alright together")
else:
    print(f"your score{score}, GOOD LUCK!")


#     -------------task 24----------

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
def days_in_month(year,month):
    month_days= [31,28,31,30,31,30,31,31,30,31,30,31]






