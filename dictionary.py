from clear import clear

programming_dictionary = {"Bug": "An error in a program that prevents the program "
                                 "from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again.",
                          "Loop": "adding something", "For": "printing value by adding something"}

print(programming_dictionary["Loop"])
# adding a dictionary

# create an empty dictionary
empty_dictionary = {}

# wipe an existing dictionary
# programming_dictionary = {}

# Edit an items in dictionary
programming_dictionary["Bug"] = "A moth in your computer"
# print(programming_dictionary)

# loop through a dictionary

for key in programming_dictionary:
    print(key)
print(programming_dictionary)
# -------------------- student scores ----------------------

student_scores = {
    "Harry": 81,
    "Amy": 99,
    "Dhyani": 78,
    "Lehek": 74,
    "vivaan": 79,
    "alina": 65
}

# print(student_scores)

student_grades = {}

# to convert scores in to a grade
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "outstanding"
    elif score > 80:
        student_grades[student] = "exceed expectations"
    elif score > 70:
        student_grades[student] = "acceptable"
    else:
        student_grades[student] = "fail"

print(student_grades)

# --------------------- travel log --------------------
# Nesting
capitals = {
    "France": "paris",
    "germany": "Berlin",
    "India": "Delhi"
}
# Nesting a list in a dictionary
travel_log = {
    # only Key and value
    "France": ["paris", "lille", "dijon"],
    "India": ["Mumbai", "Delhi", "Bangalore", "Chennai"],

    # many value - you can pass on this way
    "France": {"cities_visited": ["paris", "lille", "dijon"], "total_visites": 12},
    "India": {"cities_visited": ["Mumbai", "Delhi", "Bangalore", "Chennai"], "total_visites": 5}, }

#  Nesting dictionary in a List
travel_logg = [
    {"country": "France",
     "cities_visited": ["paris", "lille", "dijon"],
     "total_visites": 12},
    {"country": "India",
     "cities_visited": ["Mumbai", "Delhi", "Bangalore", "Chennai"],
     "total_visites": 5}, ]


# print(travel_logg)

# -----------------task -----------------

# country = input("Country name")
# visits = int(input("number of visits"))
# list_of_cities = eval(input("create list "))


def add_new_country(name, time_visited, cities_visited):
    new_country = {}
    new_country["country"] = name
    new_country["visits"] = time_visited
    new_country["cities"] = cities_visited

    # travel_logg.append(new_country)


# add_new_country(country, visits, list_of_cities)
# print(f"i have been to {travel_logg[2]['country']} {travel_log[2]['visits']} times.")
# print(f"my favorite city was {travel_log[2]['cities'][0]}")

# print(travel_logg)

# -------------Bidding auction ------------------

from logo import logo1

print(logo1)

bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    #     bidding_record = {"Arti":123, "Pushan": 321}
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"the winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("what is your name")
    price = int(input("what is your bid? $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'Yes' or 'No'.\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()
