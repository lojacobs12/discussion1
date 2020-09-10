from turtle import *

def drawSquare(turtle, xpos, ypos, width, color1, colorr):
    turtle.color(color1, colorr)
    turtle.penup()
    turtle.goto(xpos, ypos)
    turtle.pendown()
    turtle.setheading(180)
    turtle.begin_fill()
    for x in range(4):
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()
    
    #Write a function to draw a square on the screen using the specified parameters.

    #:param turtle: An instance of the Turtle class
    #:param xpos: The X-axis coordinate for the starting point of the Square
    #:param ypos: The Y-axis coordinate for the starting point of the Square
    #:param width: The width of the Square
    #:param color: The line color and fill color to use for the Square
    

    #pass


def drawTriangle(turtle, width, color1, colort):
    turtle.color(color1, colort)
    turtle.right(180)
    turtle.begin_fill()
    for x in range(3):
        turtle.left(120)
        turtle.forward(width)
    turtle.end_fill()
    
    
    #Write a function to draw a square on the screen using the specified parameters.

    #:param turtle: An instance of the Turtle class
    #:param xpos: The X-axis coordinate for the starting point of the Triangle
    #:param ypos: The Y-axis coordinate for the starting point of the Triangle
    #:param width: The length of a side of the Triangle
    #:param color: The line color and fill color to use for the Triangle
   

   # pass

def draw_houses(turtle):
   c1 = 'black'
   cr = ['pink', 'green', 'blue', 'yellow']
   ct = ['purple', 'blue', 'green', 'orange']
   w = 100
   i = 0
   x = -200
   y = 0
   for z in range(4):
       crr = cr[i]
       drawSquare(turtle, x, y, w, c1, crr)
       ctt = ct[i]
       drawTriangle(turtle, w, c1, ctt)
       i = i+1
       x = x + w + 50


    #Write a function to create houses using loops.

   #Feel free to modify the arguments of this function as you like,
    #but you should pass in the turtle object at the very least.
    

    #pass

def main():
    space = Screen()
    space.screensize(100, 100)
    annie = Turtle()
    draw_houses(annie)
    space.exitonclick()
    
    #Write a function that will be called when you run this program
    #from the terminal.

    #Make sure to create a Screen object, a Turtle object,
    #and call draw_houses.

    #Also, make sure to call the .exitonclick() method on your Screen instance
    #to stop the program from exiting untill you close the drawing window.
    

    #pass


# Only run the main function if this file is executed (not imported)
if __name__ == '__main__':
    main()


