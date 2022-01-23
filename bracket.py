# Import turtle package
import turtle

# Creating a turtle object(pen)
pen = turtle.Turtle()


def box(l, w, val):
    for i in range(2):
        pen.forward(l)
        pen.right(90)
        pen.forward(w)
        pen.right(90)

    pen.up()
    pen.right(90)
    pen.forward(w*2/3)
    pen.left(90)
    pen.forward(l/3)
    pen.down()
    pen.write(val, font=("Verdana", 12, "bold"))

def draw_tournament_bracket():
    WIDTH, HEIGHT = 800, 800
    screen = turtle.Screen()
    screen.setup(WIDTH + 40, HEIGHT + 40)

    # turtle.screensize(canvwidth=600, canvheight=800, bg="white")
    # turtle.delay(0)
    pen.speed(0)

    x = -1 * WIDTH / 2
    y = HEIGHT / 2

    teams_left = ['FCB', 'RMA', 'BAY', 'DOR', 'ATM', 'LIV', 'CHE']
    for team in teams_left:
        pen.up()
        pen.setpos(x, y)
        pen.down()
        box(80, 50, team)
        y = y - 100

    pen.ht()

    turtle.mainloop()


if __name__ == '__main__':
    draw_tournament_bracket()