#this is a turtle game tring to eat some food

import turtle
import random
import math
import time

#setting screen
sc=turtle.Screen()
sc.bgcolor('grey')
sc.tracer(1.8)

#creating boundries

bon=turtle.Turtle()
bon.penup()
bon.setpos(300,300)
bon.pendown()
bon.pensize(5)
for i in range(4):
    bon.back(600)
    bon.left(90)

bon.hideturtle()

# creating food

goal=turtle.Turtle()
goal.color('yellow')
goal.shape('circle')
goal.penup()
goal.setpos(random.randint(-300,300),random.randint(-300,300))


#creating a player

player=turtle.Turtle()
player.color("green")
player.shape("turtle")
player.penup()
player.setpos(0,0)
player.speed(0)


#creating functions
speed = 0.5

def turn_left():
    player.left(90)

def turn_right():
    player.right(90)

def up():
    global speed
    speed+=0.5
    if speed>=3:
        speed=3

def low():
    global speed
    speed-=0.5
    if speed<=0:
        speed=1

def iscolli(t1,t2):
    d=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    if d< 20 :
        return True
    else:
        return False



     #assign buttons
turtle.listen()
turtle.onkey(turn_left,"4")
turtle.onkey(turn_right,"6")
turtle.onkey(up,"8")
turtle.onkey(low,"2")

score=0

while True:
    player.forward(speed)

    if player.xcor() > int(290) or player.xcor() <int(-290) or player.ycor() > int(290) or player.ycor() <int(-290):
        goal.penup()
        goal.goto(0,0)
        print(goal.write("game over", score ,font=('Verdana',17,'bold')))
        time.sleep(1)
        break
        
    

    if iscolli(player,goal):
        goal.setpos(random.randint(-250,250),random.randint(-250,250))
        score+=1
        speed+=0.2
        if speed >=4:
            speed=4


        bon.undo()
        bon.penup()
        bon.setpos(-290,300)
        bon.hideturtle()
        bon.write(f"score : {score}",False,align="left",font=('Arial',10,'normal'))





