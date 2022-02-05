import turtle

turtle.pensize(3)
turtle.fillcolor("orange")
turtle.begin_fill()
turtle.forward(300)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(300)
turtle.left(90)
turtle.forward(100)
turtle.end_fill()

turtle.fillcolor("white")
turtle.begin_fill()
turtle.left(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(100)
turtle.end_fill()

turtle.goto(0,-100)
turtle.fillcolor("light green")
turtle.begin_fill()
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(100)
turtle.end_fill()

turtle.up()
turtle.goto(200,-50)
turtle.down()
turtle.circle(50)

turtle.up()
turtle.goto(150,-50)
turtle.down()
turtle.color("navy blue")
turtle.goto(150,-100)

for i in range(18):
    turtle.forward(100)
    turtle.right(170)

turtle.hideturtle()


turtle.done()


