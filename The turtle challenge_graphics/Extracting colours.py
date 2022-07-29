# import colorgram
#
# rgb_colors = []
#
# colors = colorgram.extract('images.jfif', 20)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import random

# color_list = [(246, 240, 228), (248, 237, 243), (234, 246, 239), (235, 240, 247), (196, 153, 117), (139, 71, 89), (145, 81, 69), (61, 97, 127), (225, 215, 109), (136, 165, 184), (187, 145, 159), (34, 20, 15), (20, 26, 41), (133, 176, 148), (191, 93, 81), (45, 24, 33), (54, 123, 94), (186, 88, 104), (15, 25, 19), (83, 156, 112)]

# Draw Hirsts painting

import turtle as turtle_module
import random


turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.hideturtle()
tim.penup()

color_list = [(196, 153, 117), (139, 71, 89), (145, 81, 69), (61, 97, 127), (225, 215, 109), (136, 165, 184), (187, 145, 159), (34, 20, 15), (20, 26, 41), (133, 176, 148), (191, 93, 81), (45, 24, 33), (54, 123, 94), (186, 88, 104), (15, 25, 19), (83, 156, 112)]

tim.setheading(225)
tim.forward(500)
tim.setheading(0)

number_of_dots = 1000

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)




screen = turtle_module.Screen()
screen.exitonclick()





