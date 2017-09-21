import turtle

def drawsquare():
    sidelength=100
    turtle.forward(sidelength)
    turtle.right(90)
    turtle.forward(sidelength)
    turtle.right(90)
    turtle.forward(sidelength)
    turtle.right(90)
    turtle.forward(sidelength)
    turtle.right(90)

def squares():
    value=turtle.numinput('','Enter a Number: ')
    while value<10:
        drawsquare()
        turtle.right(360/value)
        value=value+1

def main():
    squares()

if __name__ == '__main__':
    main()
