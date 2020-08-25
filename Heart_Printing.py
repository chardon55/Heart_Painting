import turtle
import time


def heart_paint():
    turtle.seth(120)
    turtle.color("red")
    turtle.pendown()
    turtle.begin_fill()

    turtle.fillcolor("pink")
    turtle.hideturtle()
    turtle.circle(70, 180)
    turtle.circle(170, 51.5)
    turtle.seth(9.5)
    turtle.circle(170, 51.5)
    turtle.circle(70, 180)

    turtle.end_fill()
    turtle.penup()
    turtle.showturtle()


def write_script(_str):
    turtle.write(_str, align=("center"), font=("Vladimir Script", 72, "normal"))

    
turtle.setup(700, 500)
turtle.penup()
turtle.speed(1)
turtle.seth(90)
turtle.fd(100)
time.sleep(0.5)

heart_paint()

turtle.seth(-90)
turtle.fd(300)
turtle.hideturtle()
time.sleep(0.5)

write_script('I love you')

turtle.done()
