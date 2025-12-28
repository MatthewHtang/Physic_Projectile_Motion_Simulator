#Projectile Motion Simulator

import math
from numpy import *
from pylab import *

initial_velocity = float(input ("Enter initial velocity (m/s): "))
initial_height = float(input ("Enter initial height (m): "))
launch_angle = float(input("Enter launch angle (degree): "))

#converting angle
launch_degree = math.radians(launch_angle)

#velocity components
vx = initial_velocity * math.cos(launch_degree)
vy = initial_velocity * math.sin(launch_degree)

#gravity
earth_gravity = 9.8
mercury_gravity = 3.7
venus_gravity = 8.9
moon_gravity = 1.6
mars_gravity = 3.7
jupiter_gravity = 23.1
saturn_gravity = 9.0
uranus_gravity = 8.7
neptune = 11.0
pluto = 0.7



if initial_height <= 0:
    time_travel = round((2* vy) / earth_gravity,2)
    max_height = round((vy ** 2) / (2 * earth_gravity),2)
    final_position = round(vx * time_travel,2)
elif initial_height != 0:
    

print ("Time Travel ", time_travel )
print ("Maximum Height ", max_height)
print ("Final Position ", final_position)

