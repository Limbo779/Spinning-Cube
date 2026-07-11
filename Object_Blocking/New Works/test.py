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

#player_pos = pg.Vector2(screen.get_width() / 2, screen.get_height() / 2)

def deg_rad(x):
    return x*((math.pi)/180) 

def vtr_2(l):
    return pg.math.Vector2([l[0]/l[2],l[1]/l[2]])*(27/5)

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
            r = np.array([
                [1,0,0],
                [0,np.cos(ang),np.sin(ang)],
                [0,-np.sin(ang),np.cos(ang)]
            ])

            vtx.append((np.matmul(v,r)).tolist())


    for i in range(len(connectors)):
        pg.draw.polygon(screen, "black", [center(vtr_2(vtx[connectors[i][0]-1])),center(vtr_2(vtx[connectors[i][1]-1])),center(vtr_2(vtx[connectors[i][2]-1]))],2)
    
    vtx = []



#p1 = vtr_2([0,-100.5,1])
#p2 = vtr_2([0,0,0.1])
#p3 = vtr_2([100.67,0,50])

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


### Display

#p1 = center(p1)
#p2 = center(p2)
#p3 = center(p3)

d=0
while running:
    # poll for events
    # pg.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    #pg.draw.polygon(screen, "black", [p1,p2,p3],2)
    draw_everything(20+d,'x')


    #keys = pg.key.get_pressed()
    #if keys[pg.K_w]:
    #    player_pos.y -= 300 * dt
    #if keys[pg.K_s]:
    #    player_pos.y += 300 * dt
    #if keys[pg.K_a]:
    #    player_pos.x -= 300 * dt
    #if keys[pg.K_d]:
    #    player_pos.x += 300 * dt
#
    ## flip() the display to put your work on screen
    pg.display.flip()
#
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
    d += dt

pg.quit()