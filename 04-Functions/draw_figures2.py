import turtle
from figures import draw_square

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Side length
length = 100

draw_square(length)

window.mainloop()