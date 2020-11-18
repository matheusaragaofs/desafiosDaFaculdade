import turtle
tela = turtle.Screen()
t = turtle.Turtle()
t.shape('turtle')
grid_x = 4
grid_y = 2
t.speed(0)
#forwward CASO 1
if grid_y ==1:
    def fazerQuadrados(x,y):
        for i in range(grid_x):
            t.forward(100)
            t.left(90)

    for x in range(grid_x):
        fazerQuadrados(grid_x,grid_y)
        t.forward(100)

    

# t.forward(100)

# for i in range(4):
#     t.forward(100)
#     t.left(90)

# t.forward(100)

# for i in range(4):
#     t.forward(100)
#     t.left(90)

# t.forward(100)
# for i in range(4):
#     t.forward(100)
#     t.left(90)

turtle.done()
