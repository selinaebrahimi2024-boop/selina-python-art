import turtle
screen=turtle.Screen()
screen.bgcolor("white")
screen.title("my first art-selina")
pen=turtle.Turtle()
pen.color("blue")
pen.pensize(4)
for i in range(4):
    pen.forward(300)
    pen.right(90)
screen.exitonclick()