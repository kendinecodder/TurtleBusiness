import turtle
from random import randint

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
        tosbiktime.write(countdown,font=myfont)
        tosbikmove()
        key = True
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
    if key == True:
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
countdown = int(turtle.numinput("", "sayıyı gir", ))

tosbiktime.goto(-56, 298)
tosbikscore.goto(-58, 198)

timer()

tosbikdynamic.onclick(myscore)



turtle.mainloop()



# key true ise hareket ediyor sadece. click durumunda keyi false yapıyoruz bu sayede çakışma olmuyor
# zamandan doğan true sadece timer azaldığında geçerli
















