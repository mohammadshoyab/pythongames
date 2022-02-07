#creating a ping pong game
from time import sleep
import turtle
import random
import math

#setting screen 
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

# to create block 1( or player 1)
s1=turtle.Turtle()
s1.shape('square')
s1.shapesize(stretch_wid=5,stretch_len=2)
s1.penup()
s1.goto(280,0)

#creating player 2
s2=turtle.Turtle()
s2.shape('square')
s2.shapesize(stretch_wid=5,stretch_len=2)
s2.penup()
s2.goto(-280,0)

# creating a movable object 
player=turtle.Turtle()
player.color("black") # any colour u wish
player.shape("circle") # any shape you can 
player.penup()
player.setpos(0,0) # you can go to anypos
player.speed(0)


# creating functions 

# for left block moving up
def leftu():
    y=s2.ycor()
    y+=20
    s2.sety(y)

# for left block moving down

def leftd():
    y=s2.ycor()
    y -= 20
    s2.sety(y)

    
# for right block moving up
def rightu():
    y=s1.ycor()
    y+=20
    s1.sety(y)

    
# for right block moving down
def rightd():
    y=s1.ycor()
    y -= 20
    s1.sety(y)

# this to check the collision between borders 
def iscolli(t1,t2):
    d=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    if d < 35 :
        return True
    else:
        return False

    
    #assigning keys  you can have any keys from a-z or 0-9 or arrows
    
sc.listen()
#left player keys
sc.onkeypress(leftu,"w") 
sc.onkeypress(leftd,"x")

#right player keys
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

# score turtle
    bon.undo()
    bon.penup()
    bon.hideturtle()
    bon.write(f"player1_score : {p1}  player2_score : {p2}",False,align="right",font=('Arial',10,'normal'))


    

    


