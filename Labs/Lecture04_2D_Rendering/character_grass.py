from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 50
y = 90
size = 200
speed = 5
radius = 150
cx = 400
cy = 300

def square_motion():
    for x in range(50, 750 + 1, speed): 
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        delay(0.01)
    for y in range(90, 550 + 1, speed):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(750, y)
        delay(0.01)
    for x in range(750, 50 - 1, -speed):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 550)
        delay(0.01)
    for y in range(550, 90 - 1, -speed):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(50, y)
        delay(0.01)

def circular_motion():
    for degree in range(0, 360, 5):
        clear_canvas_now()
        grass.draw_now(400, 30)
        rad = math.radians(degree)
        x = cx + radius * math.cos(rad)
        y = cy + radius * math.sin(rad)
        character.draw_now(x, y)
        delay(0.01)


while True:
    square_motion()
    circular_motion()

close_canvas()
