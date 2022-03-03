import turtle
import time

delay = 0.1

w = turtle.Screen()
w.title("snake")
w.bgcolor("black")
w.setup(width=600, height=600)
w.tracer(0)

head = turtle.Turtle()
head.shape("circle")
head.color("red")
head.turtlesize(.5)
head.speed(0)
head.penup()
head.goto(0, 0)
head.direction = "stop"


def go_up():
    head.direction = "up"


def go_down():
    head.direction = "down"


def go_left():
    head.direction = "left"


def go_right():
    head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


w.listen()

w.onkeypress(go_up, "w")
w.onkeypress(go_left, "a")
w.onkeypress(go_right, "d")
w.onkeypress(go_down, "s")

while True:
    w.update()
    move()

    time.sleep(delay)

w.mainloop()
