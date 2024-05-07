import turtle

turtle.shape('turtle')
turtle.speed(1000)

for i in range(0, 360):
    turtle.forward(1)
    turtle.right(360 / 360)


turtle.exitonclick()