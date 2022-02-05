#creating aping pong game
from time import sleep
import turtle
import random
import math

sc=turtle.Screen()
sc.bgcolor('grey')
sc.tracer(2)
sc.setup(700,700)

bon=turtle.Turtle()
bon.penup()
bon.setpos(300,300)
bon.pendown()
bon.pensize(5)
for i in range(4):
    bon.back(600)
    bon.left(90)
bon.hideturtle()

s1=turtle.Turtle()
s1.shape('square')
s1.shapesize(stretch_wid=5,stretch_len=2)
s1.penup()
s1.goto(280,0)


s2=turtle.Turtle()
s2.shape('square')
s2.shapesize(stretch_wid=5,stretch_len=2)
s2.penup()
s2.goto(-280,0)

player=turtle.Turtle()
player.color("black")
player.shape("circle")
player.penup()
player.setpos(0,0)
player.speed(0)

def leftu():
    y=s2.ycor()
    y+=20
    s2.sety(y)

def leftd():
    y=s2.ycor()
    y -= 20
    s2.sety(y)

def rightu():
    y=s1.ycor()
    y+=20
    s1.sety(y)

def rightd():
    y=s1.ycor()
    y -= 20
    s1.sety(y)

def iscolli(t1,t2):
    d=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    if d < 35 :
        return True
    else:
        return False

sc.listen()
sc.onkeypress(leftu,"w")
sc.onkeypress(leftd,"x")
sc.onkeypress(rightu,"Up")
sc.onkeypress(rightd,"Down")

speed=0.3
p1=0
p2=0

angle=[70,170,110,180]
angles=[70,170]
while True:
    player.forward(speed)
   
    if  player.xcor() > int(290) or player.xcor() <int(-290):
        player.goto(-50,0)
        player.write("game over",align="center",font=("roboto",30,'bold'))
        sleep(3)
        break
    elif  player.ycor() > int(290) or player.ycor() <int(-290):
        player.right(random.choice(angle))
    if iscolli(player,s1) :
        player.right(random.choice(angles))
        p1 += 1
        speed+=0.2
        if speed >= 2:
            speed=2
        
    if iscolli(player,s2) :
        player.left(random.choice(angles))
        p2 += 1


    bon.undo()
    bon.penup()
    bon.hideturtle()
    bon.write(f"player1_score : {p1}  player2_score : {p2}",False,align="right",font=('Arial',10,'normal'))


    

    


