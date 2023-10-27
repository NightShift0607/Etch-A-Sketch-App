from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move():
    tim.forward(10)

def back():
    tim.backward(10)

def clockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def anticlockwise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.setposition(0.00, 0.00)
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=move)
screen.onkey(key="s", fun=back)
screen.onkey(key="a", fun=anticlockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()