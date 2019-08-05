"""Marc Ojalvo and Daniel Licht
CMPS 1500
Thursday 3:30-4:45
Lab 8 Part 0
04/11/2018"""


import random
import time
import turtle

#Create objects of class turtle and store them in variables Alex, Tess, Zuki
Alex = turtle.Turtle()
Tess = turtle.Turtle()
Zuki = turtle.Turtle()

#Place Alex at position 0,20, and Tess at position 0,40 (without leaving the trace)
Alex.penup()
Tess.penup()
Zuki.penup()
Alex.setposition(0,20)
Tess.setposition(0,40)

#Make Alex, Tess and Zuki to look like turtles rather than like arrows
Alex.shape("turtle")
Tess.shape("turtle")
Zuki.shape("turtle")


#Make Alex red, Tess green and Zuki blue
Tess.fillcolor("green")
Alex.fillcolor("red")
Zuki.fillcolor("blue")

def moveme(turtle, number):
    """ Moves the turtle foward by the given number of units
        Args:
            turtle (str): Name of turtle
            number (int): Number of units
        Returns:
            Movment: A turtle moved by the number of units given
    """
    return turtle.forward(number)


#create finishline
finishline = turtle.Turtle()
finishline.penup()
finishline.setposition(250,-250)
finishline.pendown()
finishline.left(90)
finishline.forward(500)
finishline.ht()

#add starting message
turtle.pencolor('black')
turtle.write("Ready!", align = 'center', font = ('comicsans', 100, ))
time.sleep(0.5)
turtle.pencolor('white')
turtle.write("Ready!", align = 'center', font = ('comicsans', 100, ))

turtle.pencolor('black')
turtle.write("Set!", align = 'center', font = ('comicsans', 100, ))
time.sleep(0.5)
turtle.pencolor('white')
turtle.write("Set!", align = 'center', font = ('comicsans', 100, ))

turtle.pencolor('black')
turtle.write("Go!", align = 'center', font = ('comicsans', 100, ))
time.sleep(0.5)
turtle.pencolor('white')
turtle.write("Go!", align = 'center', font = ('comicsans', 100, ))


turtle.ht()
turtle.penup()
turtle.goto(50,50)
count = 0

for i in range(50):
    moveme(Alex,random.randint(1,10))
    moveme(Tess,random.randint(1,10))
    moveme(Zuki,random.randint(1,10))
    count += 1
    turtle.pencolor('black')
    turtle.write(count, align = 'right', font = ('comicsans', 100, ))
    time.sleep(0.1)
    turtle.pencolor('white')
    turtle.write(count, align = 'right', font = ('comicsans', 100, ))
    #display a victory message when turtle passes finish line
    turtle.pencolor('Pink')
    if Alex.xcor() >= 250:
        turtle.write('Victory! Congrats Alex!', align = 'center', font = ('comicsans', 50, 'bold'))
        break
    elif Tess.xcor() >= 250:
        turtle.write('Victory! Congrats Tess!', align = 'center', font = ('comicsans', 50, 'bold'))
        break
    elif Zuki.xcor() >= 250:
        turtle.write('Victory! Congrats Zuki', align = 'center', font = ('comicsans', 50, 'bold'))
        break



    
turtle.done()
