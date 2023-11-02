from turtle import *

forward(180)
left(90)
forward(200)
left(90)
forward(180)
left(90)
forward(200)

left(140)
forward(80)
right(50)
forward(170)
right(125)
forward(80)
left(180)
forward(80)



exitonclick()

from turtle import *

color("green")
begin_fill()
for i in range(6):
    forward(100)
    left(120)
    forward(50)
    right(60)

end_fill()

color("blue")
begin_fill()
for i in range(6):
    forward(50)
    left(120)
    forward(25)
    right(60)
end_fill()

color("purple")
begin_fill()
for i in range(6):
    forward(25)
    left(120)
    forward(12)
    right(60)
end_fill()

color("white")
begin_fill()
for i in range(360):
    forward(1)
    left(1)
end_fill()


exitonclick()