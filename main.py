import turtle

def createScreen(color,title):
   ekran = turtle.Screen()
   ekran.title(title)
   ekran.bgcolor(color)

def drawSquare(lenght):


    tosbik = turtle.Turtle() # nasıl aynı anda çalıstırıcam ?
    turtle2 = turtle.Turtle()

    tosbik.forward(lenght/2)
    tosbik.left(90)
    tosbik.forward(lenght)
    tosbik.left(90)
    tosbik.forward(lenght)

    turtle2.left(180)
    turtle2.forward(lenght / 2)
    turtle2.right(90)
    turtle2.forward(lenght)
    turtle2.right(90)
    turtle2.forward(lenght)

    turtle.done()

def drawStar(length):
   tospik = turtle.Turtle()
   for a in range(5):
      tospik.right(45)
      tospik.forward(length)
      tospik.left(120)
      tospik.forward(length)
   turtle.done()

def shrinkingSquare(length,number_of_square):
    tosbik = turtle.Turtle()
    a = True
    step = 0
    while a == True:
        tosbik.forward(length)
        tosbik.left(90)
        step = step + 1
        if step % 4 == 0:
            length = length - length/number_of_square
        if step == 4*number_of_square :
            a = False

    turtle.done()





createScreen("green","Tosbik")
shrinkingSquare(300,10)









