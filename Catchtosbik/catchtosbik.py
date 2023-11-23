import turtle
from random import randint

def turtlegone():
    global key
    global countdown
    if not countdown == 0:
        tosbikmove()
        turtle.ontimer(turtlegone, 340)
        key = True


def testfunc(x,y):
    print(x,y)

def timer():
    global countdown
    global tosbiktime
    global score
    global key




    if countdown > 0:
        countdown -= 1
        tosbiktime.clear()
        tosbiktime.write(countdown,font=myfont, align="center")
        turtle.ontimer(timer,1000)


    else:
        tosbikdynamic.hideturtle()
        lastword = turtle.Turtle()
        lastword.color("red")
        lastword.penup()
        lastword.hideturtle()
        tosbikscore.clear()
        lastword.write(f"your score = {score}",align="center",font=myfont)

def myscore(x,y):
    global score
    global tosbikscore
    global key
    key = True
    tosbikmove()
    score +=1
    tosbikscore.clear()
    tosbikscore.write(f"score : {score}",font=myfont,align="center")



def tosbikmove():
    global tosbikdynamic
    global key
    global countdown
    if key == True and not countdown == 0:
        tosbikdynamic.hideturtle()
        tosbikdynamic.goto(float(randint(-50,100)), float(randint(-50,100)))
        tosbikdynamic.showturtle()
        key = False






myfont=('Arial', 30, 'normal')
turtle.Screen().bgcolor("black")
tosbiktime = turtle.Turtle()
tosbikscore = turtle.Turtle()
tosbikdynamic = turtle.Turtle()
score = 0
key = False

tosbikscore.penup()
tosbiktime.penup()
tosbikdynamic.penup()

tosbikscore.hideturtle()
tosbiktime.hideturtle()

tosbikdynamic.shape("turtle")
tosbikdynamic.color("green")
tosbikdynamic.shapesize(3,3)
tosbiktime.color("red")
tosbikscore.color("red")
countdown = int(turtle.numinput("", "geri sayım kaçtan başlasın?"))

tosbiktime.goto(-56, 298)
tosbikscore.goto(-58, 198)

timer()
turtlegone()

tosbikdynamic.onclick(myscore)



turtle.mainloop()



# key true ise hareket ediyor sadece. click durumunda keyi false yapıyoruz bu sayede çakışma olmuyor
# zamandan doğan true sadece timer azaldığında geçerli
















