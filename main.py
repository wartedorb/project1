import turtle as t
import math
t.speed(100)
t.up()


def square(a, color):
    ''' Русует квадрат стороной - а, возвращает в начальное положение + цвет '''
    t.down()
    t.color(color)
    t.begin_fill()
    for g in range(4):
        t.forward(a)
        t.right(90)
    t.end_fill()
    t.up()


def triangle(a, color):
    ''' Рисует р\б, п\у треугольник + цвета '''
    t.color(color)
    t.begin_fill()
    t.down()
    t.right(45)
    t.forward(a)
    t.left(90)
    t.forward(a)
    t.left(135)
    t.forward(math.sqrt(a ** 2 * 2))
    t.end_fill()
    t.up()
    t.left(180)


def main(a, b):
    ''' Главная фигура, координаты а,в '''
    # Рисуем каркас основной фигуры
    t.goto(a, b)
    square(10, 'black')
    t.goto(a + 90, b)
    square(10, 'black')
    t.goto(a, b - 90)
    square(10, 'black')
    t.goto(a + 90, b - 90)
    square(10, 'black')
    t.goto(a, b)
    t.down()
    t.right(45)
    t.forward(math.sqrt(20000))
    t.up()
    t.goto(a, b - 100)
    t.left(90)
    t.down()
    t.forward(math.sqrt(20000))
    t.right(45)
    t.up()
    t.goto(a + 40, b - 40)
    square(20, 'black')
    t.goto(a + 45, b - 45)
    square(10, 'white')
    # Каркас закончен

    # Рисуем галочки внутри фигуры
    t.goto(a, b)
    t.forward(20)
    triangle(math.sqrt(1800), 'red')
    t.goto(a, b)
    t.forward(30)
    triangle(math.sqrt(800), 'black')
    t.goto(a, b)
    t.forward(40)
    triangle(math.sqrt(200), 'white')
    # Верх - конец

    t.goto(a, b - 80)
    t.left(90)
    triangle(math.sqrt(1800), 'red')
    t.goto(a, b - 70)
    triangle(math.sqrt(800), 'black')
    t.goto(a, b - 60)
    triangle(math.sqrt(200), 'white')
    t.right(90)
    # Лево - конец

    t.goto(a + 100, b)
    t.right(90)
    t.forward(20)
    triangle(math.sqrt(1800), 'red')
    t.goto(a + 100, b)
    t.forward(30)
    triangle(math.sqrt(800), 'black')
    t.goto(a + 100, b)
    t.forward(40)
    triangle(math.sqrt(200), 'white')
    t.left(90)
    # Право - конец

    t.goto(a + 100, b - 100)
    t.left(180)
    t.forward(20)
    triangle(math.sqrt(1800), 'red')
    t.goto(a + 100, b - 100)
    t.forward(30)
    triangle(math.sqrt(800), 'black')
    t.goto(a + 100, b - 100)
    t.forward(40)
    triangle(math.sqrt(200), 'white')
    t.right(180)
    # Низ - конец


def cvetok(a, b, color):
    ''' Рисует цветок. а,в - координаты + цвет'''
    t.goto(a, b)
    t.down()
    square(15, color)
    t.down()
    t.goto(a + 7.5, b - 7.5)
    t.left(45)
    t.width(2)
    t.color('white')
    t.forward(math.sqrt(7.5 ** 2 * 2) + 2)
    t.backward(math.sqrt(7.5 ** 2 * 2) + 2)
    t.left(90)
    t.forward(math.sqrt(7.5 ** 2 * 2) + 2)
    t.backward(math.sqrt(7.5 ** 2 * 2) + 2)
    t.left(90)
    t.forward(math.sqrt(7.5 ** 2 * 2) + 2)
    t.backward(math.sqrt(7.5 ** 2 * 2) + 2)
    t.left(90)
    t.forward(math.sqrt(7.5 ** 2 * 2) + 2)
    t.up()
    t.left(45)
    t.goto(a + 7.5, b - 10.5)
    t.color('yellow')
    t.begin_fill()
    t.circle(3)
    t.end_fill()
    t.up()


def ramkaside(a, b, color):
    ''' Рисует сторону рамки, а в - начало координат + цвет '''
    t.goto(a, b)
    t.width(2)
    t.color('black')
    t.down()
    t.forward(400)
    t.backward(400)
    t.color(color)
    t.begin_fill()
    for r in range(10):
        t.right(45)
        t.forward(math.sqrt(800))
        t.left(90)
        t.forward(math.sqrt(800))
        t.right(45)
    t.end_fill()
    t.color('black')
    t.backward(400)
    for r in range(10):
        t.right(45)
        t.forward(math.sqrt(800))
        t.left(90)
        t.forward(math.sqrt(800))
        t.right(45)
    t.width(1)


# Рисуем 9 основных фигур
main(0, 0)
main(100, 0)
main(-100, 0)
main(-100, -100)
main(0, -100)
main(100, -100)
main(-100, 100)
main(0, 100)
main(100, 100)
# Конец

# Обведем чтоб получше выглядело
t.goto(-100, -200)
t.left(90)
t.down()
t.color('black')
t.forward(300)
t.right(90)
t.forward(300)
t.right(90)
t.forward(300)
t.right(90)
t.forward(300)
t.right(180)
t.up()

# Рисуем цветочки
cvetok(-120, -42.5, 'red')
cvetok(-120, -142.50, 'red')
cvetok(-120, 57.5, 'red')
# Лево - конец
cvetok(-57.5, 120, 'orange')
cvetok(-57.5 + 100, 120, 'orange')
cvetok(-57.5 + 200, 120, 'orange')
# Верх - конец
cvetok(205, 57.5, 'purple')
cvetok(205, -42.5, 'purple')
cvetok(205, -142.5, 'purple')
# Право - конец
cvetok(-57.5, -205, 'blue')
cvetok(-57.5 + 100, -205, 'blue')
cvetok(-57.5 + 200, -205, 'blue')
# Низ - конец

# Рисуем рамку
ramkaside(-150, 150, 'orange')
t.right(90)
# Верх - конец
ramkaside(250, 150, 'purple')
t.right(90)
# Право - конец
ramkaside(250, -250, 'blue')
t.right(90)
# Низ -конец
ramkaside(-150, -250, 'red')
# Лево - конец

t.right(90)
t.done()
