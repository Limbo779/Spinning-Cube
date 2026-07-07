import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider
import math 
import pickle


a = np.array([2,3])
b = np.array([6.3,79])

#z = np.array([0,0,1])
#
#def length(a):
#    return (np.dot(a,a))**0.5
#
#print(np.dot(a,z)/(length(a)*length(z)))

plt.plot(a,b)
plt.show()