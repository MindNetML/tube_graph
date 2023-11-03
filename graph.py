import turtle as t
import colorsys

def draw_pattern():
    h = 0.5
    i = 0
    mode = 1  # Start with mode 1
    while True:
        # Clear the screen and reset the turtle every 100 iterations
        if i % 100 == 0:
            t.clear()
            t.penup()
            t.goto(50, 0)
            t.pendown()
            mode = 1 if mode == 2 else 2  # Switch modes between 1 and 2
        
        c = colorsys.hsv_to_rgb(h % 1, 1, 1)  # Use modulo to cycle hue between 0 and 1
        h += 0.003  # Slower hue change
        t.fillcolor(c)
        t.begin_fill()
        
        if mode == 1:
            t.fd(i * 2)
            rotation_angle = 190 - i * 0.01  # Gradually change the rotation angle
            t.rt(rotation_angle)
            circle_radius = i + 20 + i * 0.1  # Gradually change the circle radius
        else:  # mode == 2
            t.fd(i * 1.5)
            rotation_angle = 170 - i * 0.01  # Different rotation angle
            t.rt(rotation_angle)
            circle_radius = i + 30 - i * 0.1  # Different circle radius
        
        t.circle(circle_radius, 144)
        t.end_fill()
        i += 0.1  # Increment i more slowly for a longer run
        
        # Reset i to 0 every 100 iterations to repeat the pattern
        if i >= 100:
            i = 0

if __name__ == "__main__":
    t.bgcolor("black")
    t.tracer(10)
    t.pensize(2)
    draw_pattern()
    t.done()