# Example file showing a circle moving on screen
import pygame as pg
import numpy as np
import math

# pg setup
pg.init()
screen = pg.display.set_mode((1080, 1080))
clock = pg.time.Clock()
running = True
dt = 0

def deg_rad(x):
    return x*((math.pi)/180) 

def center(p1):
    global scale

    x = p1.x*scale
    y = p1.y*scale

    return (pg.Vector2(x,y)+pg.Vector2(screen.get_width() / 2, screen.get_height() / 2))

def to_2d(p):
    return pg.math.Vector2(p.x,p.y)

C = pg.math.Vector3([0,0,10])
P0 = pg.math.Vector3([0,0,20])
N = pg.math.Vector3([0,0,1])
scale = 512/50

s1 = pg.math.Vector3(20,-10,50)
s2 = pg.math.Vector3(20,10,50)
s3 = pg.math.Vector3(-20,-10,50)

L1 = s1-C 
L2 = s2-C 
L3 = s3-C 

f1 = C + L1*((pg.math.Vector3.dot((P0-C),N)/(pg.math.Vector3.dot(L1,N))))
f2 = C + L2*((pg.math.Vector3.dot((P0-C),N)/(pg.math.Vector3.dot(L2,N))))
f3 = C + L3*((pg.math.Vector3.dot((P0-C),N)/(pg.math.Vector3.dot(L3,N))))



d = 0
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill("white")

    # FIX 3: Multiplied 'd' by a speed factor so the rotation is actually visible.
    # Because dt is small (~0.016), rotation was incredibly slow.
    pg.draw.polygon(screen, "black", [center(to_2d(f1)),center(to_2d(f2)),center(to_2d(f3))],2)

    pg.display.flip()

    dt = clock.tick(60) / 1000
    d += dt

pg.quit()