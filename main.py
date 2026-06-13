import turtle

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
t.left(90)
t.penup()
t.goto(0, -250)
t.pendown()
t.pensize(3)

def tree(length):

    if length < 10:
        t.color("gold")
        t.dot(8)
        return

    t.color("#8B4513")  
    t.forward(length)

    t.color("gold")
    t.dot(5)

    t.left(30)
    tree(length * 0.75)

    t.right(60)
    tree(length * 0.75)

    t.left(30)
    t.backward(length)

tree(120)

t.hideturtle()
turtle.done()
