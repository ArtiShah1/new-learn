import random
import turtle as t

tim = t.Turtle()
t.colormode(255)


# colors = ["cyan", "blue", "yellow", "red", "pink", "orange"]

# -----------------DIFFERENT SHAPE DRAW TOGETHER---------------
#
# def draw_shape(num_sides):
#     angle = 360/num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
# for shape_side in range(3,11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side)

# ---------------RANDOM WALK WITH RANDOM COLOURS AND SPEED-------------------


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# direction = [0,90,180,270]
# tim.pensize(15)
tim.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + 10)


draw_spirograph(5)
screen = t.Screen()
screen.exitonclick()

# for _ in range(500):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(direction))

# -------MAKE A SPIROGRAPH ----------------


# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
# tim.left(90)
# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# tim.left(90)


# screen = Screen()
# screen.exitonclick()
