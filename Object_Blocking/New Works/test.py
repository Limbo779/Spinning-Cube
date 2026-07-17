# Example file showing a circle moving on screen
import pygame as pg
import numpy as np
import math

# pg setup
pg.init()
screen = pg.display.set_mode((1980, 1080))
clock = pg.time.Clock()
running = True
dt = 0

def deg_rad(x):
    return x*((math.pi)/180) 

def vtr_2(l):
    # FIX 1: Z-Clipping. 
    # Added a Z-offset (1500) to push the cube away from the camera. 
    # Without this, rotating vertices cross Z=0, dividing by negatives and breaking the math.
    z = l[2] + 1500 
    
    # Safety net to prevent division by zero
    if z == 0: 
        z = 0.1 
        
    # Adjusted the FOV scale (multiplier) to 600 so it looks good at this new distance
    return pg.math.Vector2([l[0]/z, l[1]/z]) * 600

def center(p1):
    p1.y -= -1
    return (p1+pg.Vector2(screen.get_width() / 2, screen.get_height() / 2))

def draw_everything(ang,axis):
    global vtx, vtx_main, connectors

    ang = deg_rad(ang)
    # Rotation loop
    if axis=='x':
        for i in vtx_main:
            v = np.array(i)
            r = np.array([
                [1,0,0],
                [0,np.cos(ang),np.sin(ang)],
                [0,-np.sin(ang),np.cos(ang)]
            ])
            vtx.append((np.matmul(v,r)).tolist())
    
    elif axis=='y':
        for i in vtx_main:
            v = np.array(i)
            # FIX 2: Corrected the Y-axis rotation matrix. 
            # You accidentally copied the X matrix here earlier.
            r = np.array([
                [np.cos(ang), 0, -np.sin(ang)],
                [0, 1, 0],
                [np.sin(ang), 0, np.cos(ang)]
            ])
            vtx.append((np.matmul(v,r)).tolist())


    for i in range(len(connectors)):
        pg.draw.polygon(screen, "black", [center(vtr_2(vtx[connectors[i][0]-1])),center(vtr_2(vtx[connectors[i][1]-1])),center(vtr_2(vtx[connectors[i][2]-1]))],2)
    
    vtx = []

vtx_main = [
    [-500,500,-500],
    [-500,-500,-500],
    [500,-500,-500],
    [500,500,-500],
    [-500,500,500],
    [-500,-500,500],
    [500,-500,500],
    [500,500,500]
]

vtx = [] #since vtx is gonna be rotated, we need to store the main vtx data safe

connectors = [
    [1,2,4],
    [2,3,4],
    [5,7,8],
    [5,6,8],
    [5,6,2],
    [5,1,2],
    [7,4,3],
    [7,8,3],
    [5,7,4],
    [5,1,4],
    [6,2,3],
    [6,8,3]
]

d = 0
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill("white")

    # FIX 3: Multiplied 'd' by a speed factor so the rotation is actually visible.
    # Because dt is small (~0.016), rotation was incredibly slow.
    draw_everything(20 + (d * 50), 'y') # Swapped to 'y' so you can see your fixed matrix!

    pg.display.flip()

    dt = clock.tick(60) / 1000
    d += dt

pg.quit()