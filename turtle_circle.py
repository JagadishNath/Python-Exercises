"""This  program is intended for drawing  circle of different radius.
    Author:  Jagadish  Nath
    Date: 15-05-25
"""
import turtle
circle=turtle.Turtle()
radius=[50,100,150]
#radius is intended  to  be used  in pixel. That  means  it actually  depends on the size  of screen.
for i in range(3):
    circle.circle(radius[i])
turtle.mainloop()
