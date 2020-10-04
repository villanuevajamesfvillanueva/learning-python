import turtle

wn = turtle.Screen()
wn.bgcolor("black")

colors = ["pink", "yellow", "blue", "green", "white", "red"]
MA = turtle.Turtle()

for i in range(200):
    MA.pencolor(colors[i % 6])
    MA.width(i/100 + 1)
    MA.forward(i)
    MA.left(59)