#Noel Abeje
#Some this code follows instructions from a series of videos by free code camp (link is below)
#https://www.youtube.com/watch?v=C6jJg9Zan7w
import turtle
import random
import winsound
import pygame
pygame.init()
#Screen
wn=turtle.Screen()
wn.title('Pong')
wn.bgcolor('black')
wn.setup(width=800,height=600)
wn.tracer(0)

#Paddle 1
paddle1=turtle.Turtle()
paddle1.speed(0)
paddle1.shape('square')
paddle1.color('white')
paddle1.shapesize(stretch_wid=5,stretch_len=1)
paddle1.penup()
paddle1.goto(-350,-250)

#Paddle 2
paddle2=turtle.Turtle()
paddle2.speed(0)
paddle2.shape('square')
paddle2.color('white')
paddle2.shapesize(stretch_wid=5,stretch_len=1)
paddle2.penup()
paddle2.goto(350,250)

#Ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0,0)
ball.dx=0.2
ball.dy=0.2

#Scores
score1=0
score2=0

#Function
def paddle1up():
    y=paddle1.ycor()
    y+=20
    paddle1.sety(y)
def paddle1down():
    y=paddle1.ycor()
    y-=20
    paddle1.sety(y)

def paddle2up():
    y=paddle2.ycor()
    y+=20
    paddle2.sety(y)
def paddle2down():
    y=paddle2.ycor()
    y-=20
    paddle2.sety(y)
    
#Key bindings
wn.listen()
wn.onkeypress(paddle1up,"w")
wn.onkeypress(paddle1down,"s")
wn.onkeypress(paddle2up,"Up")
wn.onkeypress(paddle2down,"Down")

#Pen
pen=turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write('Player 1: {}        Player 2: {}'.format(score1,score2), align='center',font=("courier",24,'normal'))


while True:
    wn.update()
    
    #Ball movement
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #Border constraining
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy*=-1
        winsound.PlaySound('laser.wav',winsound.SND_ASYNC)
    if ball.ycor() < -285:
        ball.sety(-285)
        ball.dy*=-1
        winsound.PlaySound('laser.wav',winsound.SND_ASYNC)

    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=-1
        score1+=1
        pen.clear()
        pen.write('Player 1: {}        Player 2: {}'.format(score1,score2), align='center',font=("courier",24,'normal'))
        winsound.PlaySound('explosion.wav',winsound.SND_ASYNC)
    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx*=-1
        score2+=1
        pen.clear()
        pen.write('Player 1: {}        Player 2: {}'.format(score1,score2), align='center',font=("courier",24,'normal'))
        winsound.PlaySound('explosion.wav',winsound.SND_ASYNC)

    #Collision
    if ball.xcor()>340 and ball.xcor()<350 and ball.ycor()<paddle2.ycor()+50 and ball.ycor()>paddle2.ycor()-50:
        ball.setx(340)
        ball.dx*=-1
        winsound.PlaySound('laser.wav',winsound.SND_ASYNC)
    if ball.xcor()<-340 and ball.xcor()>-350 and ball.ycor()<paddle1.ycor()+50 and ball.ycor()>paddle1.ycor()-50:
        ball.setx(-340)
        ball.dx*=-1
        winsound.PlaySound('laser.wav',winsound.SND_ASYNC)

    #Winner
    if score1==5:
        pen.clear()
        ball.dx=0
        pen.write('Player 1 Wins', align='center',font=("courier",24,'normal'))
    elif score2==5:
        pen.clear()
        ball.dx=0
        pen.write('Player 2 Wins', align='center',font=("courier",24,'normal'))
        
