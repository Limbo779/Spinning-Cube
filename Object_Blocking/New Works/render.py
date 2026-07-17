# Example file showing a circle moving on screen
import pygame as pg
import numpy as np
import math
import pickle

# pg setup
pg.init()
screen = pg.display.set_mode((1080, 1080))
clock = pg.time.Clock()
running = True
dt = 0

# Helper Function
def np_to_pg(l):
    return pg.math.Vector3(l[0],l[1],l[2])

def deg_rad(x):
    return x*((math.pi)/180) 

def center(p1):
    global scale

    x = p1.x*scale*-1
    y = p1.y*scale*-1

    return (pg.Vector2(x,y)+pg.Vector2(screen.get_width() / 2, screen.get_height() / 2))

def to_2d(p):
    return pg.math.Vector2(p.x,p.y)

def rotate(s1,s2,s3,ang,axis):
    ang = deg_rad(ang)

    s1 = np.array([s1[0],s1[1],s1[2]])
    s2 = np.array([s2[0],s2[1],s2[2]])
    s3 = np.array([s3[0],s3[1],s3[2]])

        
    if axis=='x':
        r = np.array([
                [1,0,0],
                [0,np.cos(ang),np.sin(ang)],
                [0,-np.sin(ang),np.cos(ang)]
            ])
        
    elif axis=='y':
        r = np.array([
                [np.cos(ang), 0, -np.sin(ang)],
                [0, 1, 0],
                [np.sin(ang), 0, np.cos(ang)]
            ])
        
    else:
        r = np.array([
            [np.cos(ang), np.sin(ang), 0],
            [-np.sin(ang), np.cos(ang), 0],
            [0, 0, 1]
        ])
        
    r1 = np_to_pg(np.matmul(s1,r))
    r2 = np_to_pg(np.matmul(s2,r))
    r3 = np_to_pg(np.matmul(s3,r))

    return [r1,r2,r3]


# Main block

## Vertex and connectors
with open("vtx.pkl","rb") as file:
    vtx=pickle.load(file)
with open("connectors.pkl","rb") as f:
    connectors=pickle.load(f)
#vtx = [
#    [-20,  20, -20],  # 1: Top-Left-Front
#    [-20, -20, -20],  # 2: Bottom-Left-Front
#    [ 20, -20, -20],  # 3: Bottom-Right-Front
#    [ 20,  20, -20],  # 4: Top-Right-Front
#    [-20,  20,  20],  # 5: Top-Left-Back
#    [-20, -20,  20],  # 6: Bottom-Left-Back
#    [ 20, -20,  20],  # 7: Bottom-Right-Back
#    [ 20,  20,  20]   # 8: Top-Right-Back
#]
#
## 12 triangles (2 per cube face) using 1-based indexing
#connectors = [
#    [1, 2, 4], [2, 3, 4],  # Front Face
#    [5, 6, 8], [6, 7, 8],  # Back Face
#    [5, 6, 2], [5, 1, 2],  # Left Face
#    [7, 8, 3], [7, 4, 3],  # Right Face
#    [5, 1, 4], [5, 8, 4],  # Top Face 
#    [6, 2, 3], [6, 7, 3]   # Bottom Face 
#]

def project(s1,s2,s3):
    global C,P0,N

    L1 = s1-C 
    L2 = s2-C 
    L3 = s3-C 

    f1 = C + L1*((pg.math.Vector3.dot((P0-C),N)/(pg.math.Vector3.dot(L1,N))))
    f2 = C + L2*((pg.math.Vector3.dot((P0-C),N)/(pg.math.Vector3.dot(L2,N))))
    f3 = C + L3*((pg.math.Vector3.dot((P0-C),N)/(pg.math.Vector3.dot(L3,N))))

    l = [f1,f2,f3]

    return l


def draw_everything(d):
    global vtx
    for i in connectors:
        s1 = vtx[i[0]-1]
        s2 = vtx[i[1]-1]
        s3 = vtx[i[2]-1]

        p1,p2,p3 = rotate(s1,s2,s3,30+d,'y')
        #r1,r2,r3 = rotate(p1,p2,p3,30+d,'x')

        Normal = pg.math.Vector3.cross((p2-p1),(p3-p1))

        if pg.math.Vector3.dot(Normal,N) > 0 :
            f1,f2,f3 = project(p1,p2,p3)

            pg.draw.polygon(screen, "black", [center(to_2d(f1)),center(to_2d(f2)),center(to_2d(f3))],2)
        else:
            continue
        


# Screen stuffs

## Camera details
scale = 512/200
C = pg.math.Vector3([0,0,-3000])
P0 = pg.math.Vector3([0,0,-1500])
N = pg.math.Vector3([0,0,1])

d = 0
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill("white")
    
    #pg.draw.polygon(screen, "black", [center(to_2d(f1)),center(to_2d(f2)),center(to_2d(f3))],2)
    draw_everything(d*50)


    pg.display.flip()

    dt = clock.tick(60) / 1000
    d += dt

pg.quit()