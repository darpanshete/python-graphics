import turtle

turt = turtle.Turtle()

turtle.title("My first graphics")
turt.pencolor("red")
turtle.bgcolor("black")
turt.hideturtle
turt.speed(0)
count = 0
turt.color("red")

while True:
    for i in range(4):
        turt.forward(110)
        turt.right(90)
    
    turt.right(5)
    count += 1
    if count >= 360/5:
        break

turtle.done()
