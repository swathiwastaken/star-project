# star-project
code a star!
import turtle
screen=turtle.Screen()
screen.setup(500, 600, startx=0, starty=100)
t = turtle.Turtle()
s = turtle.Screen() 
s.bgcolor("black")
t.speed(10)
color = ['red', 'white', 'red', 'white'] 
c=0 
for i in range(80):
 t.forward(i*7)
 t.right(144)
 t.color(color[c])
 if c==3:
  c = 0 
 else:
  c+=1 
turtle.speed(100)
turtle.penup()
msg = "Merry Christmas :D"
turtle.goto(0, -210)  
turtle.color("red")
turtle.pendown()
turtle.write(msg, move=False, align="center", font=("script", 24, "italic"))
