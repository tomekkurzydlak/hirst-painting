import random
import turtle as t
t.colormode(255)
tim = t.Turtle()

color_palette = [(200, 167, 110), (144, 74, 52), (237, 241, 246), (169, 152, 45), (58, 92, 119), (224, 203, 131), (136, 162, 180), (131, 34, 26), (51, 117, 89), (199, 94, 72), (143, 25, 30), (18, 97, 74), (69, 47, 40), (173, 146, 153), (150, 177, 152), (131, 70, 74), (56, 43, 46), (237, 174, 163), (184, 88, 94), (38, 58, 71), (28, 82, 89), (182, 204, 178), (242, 156, 160), (93, 144, 124), (20, 66, 57), (36, 65, 96), (108, 125, 154), (103, 137, 147), (181, 190, 209), (74, 65, 49), (176, 198, 202)]

tim.hideturtle()
tim.penup()
tim.speed(0)
tim.setpos(-300, -300)
row = 0
rows = 13
def draw_horizontal():
    global row
    for i in range(rows):
        tim.dot(20, random.choice(color_palette))
        tim.forward(50)
        row += 50/rows

for i in range(rows):
    tim.setpos(-300, -300 + row)
    draw_horizontal()
    tim.left(90)
    tim.forward(50)
    tim.right(90)

screen = t.Screen()
screen.exitonclick()