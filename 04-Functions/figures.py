import turtle

def draw_square(pen, length):
    # Rysuj kwadrat
    for i in range(4):
        pen.forward(length)
        pen.right(90)

def draw_triangle(pen, length):
    # Rysuj trójkąt
    for i in range(3):
        pen.forward(length)
        pen.left(120)

def draw_rectangle(pen, length_a, length_b):
    # Rysuj prostokąt
    for i in range(2):
        pen.forward(length_a)
        pen.right(90)
        pen.forward(length_b)
        pen.right(90)

def main():
    # Ustaw ekran
    window = turtle.Screen()
    window.bgcolor("lightgreen")

    # Twórz pióro do rysowania (raz, na początku)
    pen = turtle.Turtle()
    pen.speed(5)

    # Rysuj dwa kwadraty w różnych miejscach
    pen.penup()
    pen.goto(-150, 150)
    pen.pendown()
    draw_square(pen, 50)

    pen.penup()
    pen.goto(0, 150)  # Przesunięcie w prawo
    pen.pendown()
    draw_square(pen, 50)

    # Rysuj dwa trójkąty w różnych miejscach
    pen.penup()
    pen.goto(-150, 50)
    pen.pendown()
    draw_triangle(pen, 50)

    pen.penup()
    pen.goto(0, 50)  # Przesunięcie w prawo
    pen.pendown()
    draw_triangle(pen, 50)

    # Rysuj dwa prostokąty w różnych miejscach
    pen.penup()
    pen.goto(-150, -100)
    pen.pendown()
    draw_rectangle(pen, 70, 40)

    pen.penup()
    pen.goto(0, -100)  # Przesunięcie w prawo
    pen.pendown()
    draw_rectangle(pen, 70, 40)

    # Ukryj pióro i zakończ
    pen.hideturtle()
    window.mainloop()

# Uruchom główną funkcję
if __name__ == "__main__":
    main()
