import turtle

my_turtle_cursor = turtle.Turtle()
my_turtle_screen = turtle.Screen()
y_coordinate = -125


def draw_candle_for_cake(fill_color, border_color, x, y):
    my_turtle_cursor.penup()
    my_turtle_cursor.color(border_color)
    my_turtle_cursor.fillcolor(fill_color)
    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.pendown()
    my_turtle_cursor.begin_fill()
    my_turtle_cursor.forward(25)
    my_turtle_cursor.left(90)
    my_turtle_cursor.forward(60)
    my_turtle_cursor.left(90)
    my_turtle_cursor.forward(25)
    my_turtle_cursor.left(90)
    my_turtle_cursor.forward(60)
    my_turtle_cursor.left(90)
    my_turtle_cursor.end_fill()
    my_turtle_cursor.getscreen().update()




def draw_stick(fill_color, border_color, x, y):
    my_turtle_cursor.penup()
    my_turtle_cursor.pensize(3)
    my_turtle_cursor.color(border_color)
    my_turtle_cursor.fillcolor(fill_color)
    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.begin_fill()
    my_turtle_cursor.pendown()
    my_turtle_cursor.left(180)
    my_turtle_cursor.forward(200)
    my_turtle_cursor.end_fill()
def draw_stick_on_candle(fill_color, x, y, cursor_size):
    my_turtle_cursor.penup()
    my_turtle_cursor.color(fill_color)
    my_turtle_cursor.fillcolor(fill_color)
    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.pensize(cursor_size)
    my_turtle_cursor.begin_fill()
    my_turtle_cursor.pendown()
    my_turtle_cursor.right(90)
    my_turtle_cursor.forward(12)
    my_turtle_cursor.end_fill()
    my_turtle_cursor.getscreen().update()



def draw_toppings_on_cake(fill_color, border_color, x, y, radius):
    my_turtle_cursor.penup()
    my_turtle_cursor.color(border_color)
    my_turtle_cursor.fillcolor(fill_color)
    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.pendown()
    my_turtle_cursor.begin_fill()
    my_turtle_cursor.forward(10)
    my_turtle_cursor.left(90)
    my_turtle_cursor.circle(radius, extent = 180)
    my_turtle_cursor.left(90)
    my_turtle_cursor.forward(10)
    my_turtle_cursor.end_fill()
    my_turtle_cursor.getscreen().update()

def draw_layer_of_the_cake(fill_color, border_color, cursor_size, x, y, width, height):
    my_turtle_cursor.hideturtle()
    my_turtle_cursor.penup()
    my_turtle_cursor.pensize(cursor_size)
    my_turtle_cursor.color(border_color)
    my_turtle_cursor.fillcolor(fill_color)
    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.pendown()
    my_turtle_cursor.begin_fill()

    for i in range(2):
        my_turtle_cursor.forward(width)
        my_turtle_cursor.left(90)
        my_turtle_cursor.forward(height)
        my_turtle_cursor.left(90)

    my_turtle_cursor.end_fill()
    my_turtle_cursor.setheading(0)
    my_turtle_cursor.getscreen().update()

my_turtle_screen.bgcolor("#B6E0F0")

parts_of_cake = []
parts_of_cake.append(["#C22146", "#000000", 3, 60])
parts_of_cake.append(["#8cB06f", "#000000", 3, 40])
parts_of_cake.append(["#FFFC63", "#000000", 3, 30])
parts_of_cake.append(["#fC49A0", "#000000", 3, 20])


draw_layer_of_the_cake("#4A4844", "#000000", 3, -220, y_coordinate - 70, 400, 10)

for parts in parts_of_cake:
    draw_layer_of_the_cake(parts[0], parts[1], parts[2], -135, y_coordinate - 60, 240, parts[3])
    y_coordinate += parts[3]

draw_toppings_on_cake("#C20067", "#000000", -100, y_coordinate - 60, 10)
draw_toppings_on_cake("#FFFF00", "#000000", -70, y_coordinate - 60, 10)
draw_toppings_on_cake("#BBFFB5", "#000000", 25, y_coordinate - 60, 10)
draw_toppings_on_cake("#442F52", "#000000", 59, y_coordinate - 60, 10)
draw_toppings_on_cake("#FF00A2", "#000000", -120, y_coordinate - 100, 10)
draw_toppings_on_cake("#00FF51", "#000000", 60, y_coordinate - 100, 10)
draw_toppings_on_cake("#FFD700", "#000000", -95, y_coordinate - 140, 10)
draw_toppings_on_cake("#FF1900", "#000000", 10, y_coordinate - 140, 10)
draw_toppings_on_cake("#FFD700", "#000000", 75, y_coordinate - 140, 10)
draw_candle_for_cake("#FF4F4F", "#000000", -30, y_coordinate - 60)
draw_stick_on_candle("#181A18", -21, y_coordinate + 15, 7)

turtle.penup()
turtle.goto(-160, 100)
turtle.pendown()
turtle.write("Happy Birthday Joe!", font=("Poppinssans-serif", 25, "normal"))

turtle.done()