#______________________________PONG________________________________________
#Creates the game pong

#Imports___________________________________________________________________
import turtle
import os
import time
import math

#Setup Window_____________________________________________________________
#creates window
window = turtle.Screen()
#renames window
window.title("PONG")
#change color
window.bgcolor("green")
#change size
window.setup(width=800, height=600)
#makes game faster
window.tracer(0)
start = time.time()
os.system("afplay pong.wav&")

class Paddle:
	def __init__(self,x,y):
                self.x = x
                self.y = y
                self.paddle = turtle.Turtle()
                self.paddle.speed(0)
                self.paddle.color("white")
                self.paddle.shape("square")
                self.paddle.shapesize(stretch_wid=5, stretch_len=1)
                self.paddle.penup()
                self.paddle.goto(self.x,self.y)
	def up(self):
		self.y += 20
		self.paddle.sety(self.y)
	def down(self):
		self.y -= 20
		self.paddle.sety(self.y)
	def xcord(self):
        	return self.x
	def ycord(self):
        	return self.y

class Ball:
        def __init__(self,x,y,paddle_a,paddle_b, pen, score_a, score_b):
                self.score_a = score_a
                self.score_b = score_b
                self.x = x
                self.y = y
                self.paddle_a = paddle_a
                self.paddle_b = paddle_b
                self.pen = pen
                self.ball = turtle.Turtle()
                self.ball.speed(0)
                self.ball.color("white")
                self.ball.shape("square")
                self.ball.penup()
                self.ball.goto(self.x,self.y)
                self.dx = .01
                self.dy = .01
        def move(self):
                self.x += self.dx
                self.y += self.dy
                self.boarder()
                self.ball.setx(self.x)
                self.ball.sety(self.y)
        def update(self):
                self.pen.clear()
                self.pen.write("Player A: {}   Player B: {}".format(self.score_a, self.score_b), align="center", font=("Courier", 24, "bold"))
        def boarder(self):
                if self.ball.ycor() > 290:
                        self.y = 290
                        self.dy *= -1
                if self.ball.ycor() < -290:
                        self.y = -290
                        self.dy *= -1
                if self.ball.xcor() > 390:
                        self.x = 0
                        self.y = 0
                        self.dx *= -1
                        self.score_a += 1
                        self.update()
                if self.ball.xcor() < -390:
                        self.x = 0
                        self.y = 0
                        self.dx *= -1
                        self.score_b += 1
                        self.update()
                if self.ball.xcor() < self.paddle_a.xcord() + 20 and self.ball.xcor() > self.paddle_a.xcord() - 10 and self.ball.ycor() < self.paddle_a.ycord() + 40 and self.ball.ycor() > self.paddle_a.ycord()-40:
                        self.x = -340
                        self.dx *= -1 + (self.ball.ycor()-self.paddle_b.ycord())/40.0
                        self.dy *= 1 + (self.ball.ycor()-self.paddle_b.ycord())/40.0
                if self.ball.xcor() < self.paddle_b.xcord() + 20 and self.ball.xcor() > self.paddle_b.xcord() - 10 and self.ball.ycor() < self.paddle_b.ycord() + 40 and self.ball.ycor() > self.paddle_b.ycord()-40:
                        self.x = 340
                        self.dx *= -1 + (self.ball.ycor()-self.paddle_b.ycord())/40.0
                        self.dy *= 1 + (self.ball.ycor()-self.paddle_b.ycord())/40.0

#Score________________________________________________________________
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0   Player B: 0", align="center", font=("Courier", 24, "bold"))

paddle_a = Paddle(-350,0)
paddle_b = Paddle(350,0)
ball = Ball(0, 0, paddle_a, paddle_b, pen, 0, 0)

#Keyboard binding_____________________________________________________
window.listen()
window.onkeypress(paddle_a.up, "w")
window.onkeypress(paddle_a.down, "s")
window.onkeypress(paddle_b.up, "Up")
window.onkeypress(paddle_b.down, "Down")

#main loop
while True:
	if (math.ceil(time.time()-start) % 34 == 0):
            start = time.time()
            os.system("afplay pong.wav&")
	window.update()
	ball.move()
