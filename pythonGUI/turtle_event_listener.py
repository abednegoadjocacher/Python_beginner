from turtle import Turtle, Screen
turtle_move = Turtle()
screen = Screen()

def up():
    turtle_move.setheading(90)
    turtle_move.forward(30)


def down():
    turtle_move.setheading(270)
    turtle_move.forward(30)

def left():
    turtle_move.setheading(180)
    turtle_move.forward(30)


def right():
    turtle_move.setheading(0)
    turtle_move.forward(30)

def clear_screen():
    turtle_move.clear()
    turtle_move.penup()
    turtle_move.home()
    turtle_move.pendown()

screen.listen()
screen.onkey(fun=up, key="Up")
screen.onkey(fun=down, key="Down")
screen.onkey(fun=left, key="Left")
screen.onkey(fun=right, key="Right")
screen.onkey(fun=clear_screen, key="c")


screen.exitonclick()