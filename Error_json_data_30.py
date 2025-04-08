
try:
    file = open("a_file.text")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.text", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The Key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")

height = float(input("Height: "))
weight = int (input("weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters")

bmi = weight/height ** 2
print(bmi)

