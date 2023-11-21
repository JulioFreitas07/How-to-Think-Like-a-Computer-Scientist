import turtle            # permite usar as funções e objetos do módulo turtle

wn = turtle.Screen()     # cria uma janela gráfica
wn.bgcolor("black")

alex = turtle.Turtle()   # cria um turtle chamado alex
alex.color("green")
alex.pensize(4)
alex.speed(30)
alex.shape("blank")

''' dany = turtle.Turtle()   # cria um turtle chamado alex
    dany.color("red")
    dany.pensize(2)
    dany.speed(3)'''

for i in range(1, 3600, 3):
    alex.forward(15)
    alex.left(i)

wn.exitonclick() #pede para para somente com um clique

