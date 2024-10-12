import turtle
a=open("ra.txt", "r")
c=open("red.txt", "r")
b=a.read()
d=c.read()
turtle.fillcolor(d)
turtle.begin_fill()
turtle.circle(float(b))
turtle.end_fill()
