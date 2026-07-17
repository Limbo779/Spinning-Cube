import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider
import math 
import pickle

def deg_rad(x):
    return x*((math.pi)/180)
def length(a):
    return (np.dot(a,a))**0.5

with open("vtx.pkl","rb") as file:
    vtx=pickle.load(file)
with open("mess.pkl","rb") as f:
    mess=pickle.load(f)

connectors = [
    [0, 1], [1, 2], [0,2]
]

#vtx = {
#    "x":np.array([-1,1,1,-1,-1,1,1,-1]),
#    "y":np.array([-1,-1,1,1,-1,-1,1,1]),
#    "z":np.array([-1,-1,-1,-1,1,1,1,1])
#}
#
#
#connectors = [
#    [0, 1], [1, 2], [2, 3], [0, 3],
#    [4, 5], [5, 6], [6, 7], [4, 7],
#    [1, 5], [2, 6], [3, 7], [0, 4]
#]

#vtx={
#    "x":np.array([0,1,1,0,0.5]),
#    "y":np.array([0,0,1,1,0.5]),
#    "z":np.array([0,0,0,0,1])
#}
#
#connectors=[
#    [1,2],[2,3],[3,4],[4,1],
#    [1,5],[2,5],[3,5],[4,5]
#]

def to_2d(arr):
    z1=1/arr[2]
    
    reduce = np.array([[z1,0,0],[0,z1,0]])
    
    final = np.matmul(reduce,arr)

    return final

def block_check(l):
    normal = l
    z = np.array([0,0,1])
    value = np.dot(normal,z)/(length(normal)*length(z))
    if value > 0:
        return True
    else:
        return False


# ploting

fig = plt.figure()

# FIX 3: Plot the lines correctly by grabbing specific start and end points
for i in range(len(mess)):
    if block_check(mess[i][3]):
        p1 = vtx[mess[i][0]]
        p2 = vtx[mess[i][1]]
        p3 = vtx[mess[i][2]]
        
        plt.plot(p1, p2, 'r-')
        plt.plot(p1, p3, 'r-')
        plt.plot(p2, p3, 'r-')
    else:
        continue

# Render it to the screen
plt.show()

### Animation
#fig = plt.figure(figsize=(6, 6)) 
#
## Create axes with equal aspect ratio so the cube isn't squished
#axis = plt.axes(xlim=(-1, 1), ylim=(-1, 1)) 
#axis.set_aspect('equal')
#axis.axis('off') # Hides the grid and borders for a cleaner look
#
## FIX 1: Create an array of 12 separate line objects (one for each edge)
## Notice the 'r-' styling is applied here!
#lines = [axis.plot([], [], 'r-', lw=2)[0] for _ in connectors]
#
#def init(): 
#    # Initialize all 12 lines to be empty
#    for line in lines:
#        line.set_data([], [])
#    return lines
# 
#def animate(i):
#    # FIX 3: Spin faster! 'i * 2' means 2 degrees per frame.
#    # We rotate X, then take that result and rotate Y for a cool tumbling
#    rot_vtx=rotate_y(vtx,5*i)
#    
#
#    ## Camera Change
#
#    rot_vtx["x"] -= Camera["x"]
#    rot_vtx["y"] -= Camera["y"]
#    rot_vtx["z"] -= Camera["z"]
#
#    screen = to_2d(rot_vtx["x"],rot_vtx["y"],rot_vtx["z"])
#
#    # FIX 2: Loop through our 12 line objects and update their specific coordinates
#    for j, (p1, p2) in enumerate(connectors):
#        x_line = [screen["x"][p1-1], screen["x"][p2-1]]
#        y_line = [screen["y"][p1-1], screen["y"][p2-1]]
#        
#        # Update the line object at index 'j'
#        lines[j].set_data(x_line, y_line)
#    
#    return lines
# 
#anim = FuncAnimation(fig, animate, init_func=init, frames=1024, interval=5, blit=True)
#
## Shows the animation live in a window!
#plt.show()


## --- INTERACTIVE PLOT SETUP ---
#fig, axis = plt.subplots(figsize=(6, 7))
## Adjust the main plotting window to leave room at the bottom for UI sliders
#plt.subplots_adjust(bottom=0.3)
#
#axis.set_aspect('equal')
#axis.axis('off') 
#
#lines = [axis.plot([], [], 'r-', lw=2, markersize=5)[0] for _ in connectors]
#
## --- CREATING THE SLIDERS (KNOBS) ---
## Format: [left, bottom, width, height]
#ax_cam_x = plt.axes([0.2, 0.18, 0.6, 0.03], facecolor='lightgoldenrodyellow')
#ax_cam_y = plt.axes([0.2, 0.12, 0.6, 0.03], facecolor='lightgoldenrodyellow')
#ax_cam_z = plt.axes([0.2, 0.06, 0.6, 0.03], facecolor='lightgoldenrodyellow')
#
#slider_x = Slider(ax_cam_x, 'Camera X', -10.0, 10.0, valinit=0.0, valfmt='%1.1f')
#slider_y = Slider(ax_cam_y, 'Camera Y', -10.0, 10.0, valinit=0.0, valfmt='%1.1f')
#slider_z = Slider(ax_cam_z, 'Camera Z (Zoom)', -4.0, 4.0, valinit=0.0, valfmt='%1.1f')
#
#def init(): 
#    for line in lines:
#        line.set_data([], [])
#    return lines
# 
#def animate(i):
#    # 1. Base Rotations (Tumbling on X and Y axes simultaneously)
#    rot_vtx = rotate_x(vtx, i * 1.5)
#    rot_vtx = rotate_y(rot_vtx, i * 1.0)
#    
#    # 2. Read values in real-time from the sliders
#    cam_x = slider_x.val
#    cam_y = slider_y.val
#    cam_z = slider_z.val
#
#    # 3. Transform World Space to Camera Space (Move world opposite to camera)
#    view_x = rot_vtx["x"] - cam_x
#    view_y = rot_vtx["y"] - cam_y
#    view_z = (rot_vtx["z"] + 5) - cam_z  # Baseline camera distance is 5 units away
#
#    # 4. Perspective Project
#    screen = to_2d(view_x, view_y, view_z)
#
#    # 5. DYNAMIC AUTO-FRAMING MATH
#    # Find the boundary box of the projected 2D coordinates
#    x_min, x_max = np.min(screen["x"]), np.max(screen["x"])
#    y_min, y_max = np.min(screen["y"]), np.max(screen["y"])
#    
#    # Calculate screen center and spans
#    x_center = (x_max + x_min) / 2
#    y_center = (y_max + y_min) / 2
#    max_range = max(x_max - x_min, y_max - y_min)
#    
#    # Add 25% padding buffer so the cube never tightly clips the screen edges
#    padding = max_range * 0.25 if max_range > 0 else 0.5
#    half_span = (max_range / 2) + padding
#    
#    # Update viewport framing on the fly while maintaining aspect ratio
#    axis.set_xlim(x_center - half_span, x_center + half_span)
#    axis.set_ylim(y_center - half_span, y_center + half_span)
#
#    # 6. Render individual lines
#    for j, (p1, p2) in enumerate(connectors):
#        x_line = [screen["x"][p1], screen["x"][p2]]
#        y_line = [screen["y"][p1], screen["y"][p2]]
#        lines[j].set_data(x_line, y_line)
#    
#    return lines
#
## Note: blit=False is mandatory here because the axis limits shift dynamically
#anim = FuncAnimation(fig, animate, init_func=init, frames=1024, interval=15, blit=False)
#
#plt.show()