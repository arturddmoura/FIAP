#Create the following pattern:
import turtle

for i in range (0,10):
    for i in range (0,8):
        turtle.forward(50)
        turtle.left(45)

    turtle.penup()
    turtle.right(35)
    turtle.pendown()

turtle.exitonclick()