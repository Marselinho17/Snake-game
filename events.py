from turtle import Turtle, Screen 

screen = Screen()
tommy = Turtle("turtle")
tommy.penup()
def move_forward():
    tommy.forward(20)

# stisknutí klávesy
screen.listen()
screen.onkeypress(move_forward, "d")

screen.exitonclick()