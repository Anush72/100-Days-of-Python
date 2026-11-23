# creating object from class
from turtle import Turtle, Screen

hello = Turtle()
print(hello)
hello.shape('turtle')
hello.color('coral')
# moving the turtle by 100 paces
hello.forward(100)

my_screen = Screen()

# object attributes of Turtle
print(my_screen.canvheight)

# methods of object
my_screen.exitonclick()
