import turtle
t=turtle.Turtle()
def rectangle(color):
          t.fillcolor(color)
          t.begin_fill()
          t.fd(600)
          t.lt(90)
          t.fd(100)
          t.lt(90)
          t.fd(600)
          t.lt(90)
          t.fd(100)
          t.end_fill()

def flag():
          l=['green','white','orange']
          for i in range(3):
                    rectangle(l[i])
                    t.back(100)
                    t.lt(90)
          t.rt(90)
          t.fd(200)
          t.lt(90)
          t.fd(300)
          t.pensize(width=2)
          t.pencolor('blue')
          t.circle(50)
          t.lt(90)
          t.fd(50)
          for i in range(24):
                    t.fd(50)
                    t.back(50)
                    t.rt(15)
                    
'''
t.back(300)
t.rt(90)
t.fd(100)
t.lt(90)
flag()
'''

def _143():
          wn=turtle.Screen()
          wn.bgcolor('black')
          t.pensize(width=2)
          t.fillcolor('red')
          t.begin_fill()
          t.lt(45)
          t.fd(200)
          t.circle(85,195)
          t.rt(120)
          t.circle(85,195)
          t.end_fill()
          ##
          t.goto(x=-350,y=45)
          t.pencolor('red')
          t.write('',font=("Verdana",20, "normal"))
          ##
          t.pencolor('black')
          t.home()
          t.goto(x=-200,y=80)
          t.pensize(width=3)
          t.pencolor('red')
          t.lt(20)
          t.fd(242)
          t.pencolor('black')
          t.fd(180)
          t.pencolor('red')
          t.write('',font=("Verdana",20, "normal"))
          
_143()

turtle.done()
