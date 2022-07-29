from turtle import Turtle, Screen
# from turtle import * -- import everything from the module
from turtle import Turtle as T

tim = T()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(100)

# challenge_1
# make tim draw a square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# challenge_2
# make tim draw dotted lines
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# challenge_3
# draw a complex polygon
# tri-60 sq - 90  pent - 72   hexa- 60  hepta-51.43 octa-45 nano- 40 deca- 36
# for _ in range(3):
#     tim.color("red")
#     tim.forward(100)
#     tim.right(120)
#
# for _ in range(4):
#     tim.color("blue")
#     tim.forward(100)
#     tim.right(90)
#
# for _ in range(5):
#     tim.color("green")
#     tim.forward(100)
#     tim.right(72)
#
# for _ in range(6):
#     tim.color("purple")
#     tim.forward(100)
#     tim.right(60)
#
# for _ in range(7):
#     tim.color("orange")
#     tim.forward(100)
#     tim.right(51.43)
#
# for _ in range(8):
#     tim.color("black")
#     tim.forward(100)
#     tim.right(45)
#
# for _ in range(9):
#     tim.color("brown")
#     tim.forward(100)
#     tim.right(40)
#
# for _ in range(10):
#     tim.color("pink")
#     tim.forward(100)
#     tim.right(36)


# simple solution
# import random
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen"]
# tim.shape("turtle")
#
#
# def draw_shape(number_of_sides):
#     for _ in range(number_of_sides):
#         angle = 360 / number_of_sides
#         tim.forward(100)
#         tim.right(angle)
#     for _ in range(number_of_sides):
#         angle = 360 / number_of_sides
#         tim.forward(200)
#         tim.right(angle)
#
#
# for shape_side in range(3,11):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side)
#
# screen = Screen()
# screen.exitonclick()


 # the turtle color walk
# import turtle as T
# import random
# tim = T.Turtle()
# T.colormode(255)
#
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color
#
# # colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen"]
#
#
# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")
#
# for _ in range(2000):
#     tim.color(random_color())
#     tim.forward(100)
#     tim.setheading(random.choice(directions))

#
# import turtle as T
# import random
# tim = T.Turtle()
# T.colormode(255)
#
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return random_color
#
# tim.speed("fastest")
#
# for _ in range(200):
#     tim.color(random_color())
#     tim.forward()
#



# Hirst painting project











































