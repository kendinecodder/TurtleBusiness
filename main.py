import turtle

def createScreen(color,title):
   ekran = turtle.Screen()
   ekran.title(title)
   ekran.bgcolor(color)

def drawSquare(lenght):


    turtle1 = turtle.Turtle() # nasıl aynı anda çalıstırıcam ?
    turtle2 = turtle.Turtle()

    turtle1.forward(lenght/2)
    turtle1.left(90)
    turtle1.forward(lenght)
    turtle1.left(90)
    turtle1.forward(lenght)

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




createScreen("green","bekoturtle")
drawStar(50)









