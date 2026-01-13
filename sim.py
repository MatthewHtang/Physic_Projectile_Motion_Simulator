# Projectile Motion Simulator with Simple GUI Animation

import math
import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ---------------- GRAVITY ----------------
planet_gravity = [
    ["earth", 9.8], ["mercury", 3.7], ["venus", 8.9],
    ["moon", 1.6], ["mars", 3.7], ["jupiter", 23.1],
    ["saturn", 9.0], ["uranus", 8.7], ["neptune", 11.0],
    ["pluto", 0.7], ["sun", 274]
]

def launch():
    global x_vals, y_vals, index

    initial_velocity = velocity_slider.get()
    initial_height = height_slider.get()
    launch_angle = angle_slider.get()
    gravity = planet_var.get()

    # converting angle
    launch_degree = math.radians(launch_angle)

    #velocity components
    vx = initial_velocity * math.cos(launch_degree)
    vy = initial_velocity * math.sin(launch_degree)

    #setting up the gravity for user input
    grav = None
    for planet in planet_gravity:
        if planet[0] == gravity:
            grav = planet [1]
        
    if grav is None:
            return

    #This is where main physic begins
    if initial_height <= 0:
        time_travel = (2 * vy) / grav
        max_height = (vy ** 2) / (2 * grav)

    #if the initial height is greater than 0 meter
    else:
        time_travel = (vy + math.sqrt(vy**2 + 2 * grav * initial_height)) / grav
        max_height = initial_height + (vy**2) / (2 * grav)
    
    final_position = vx * time_travel

    #updating the lables on the result 
    time_label.config(text=f"Time: {time_travel :.2f} s")
    height_label.config(text=f"Maximum Height: {max_height :.2f} m")
    position_label.config(text=f"Final Position: {final_position :.2f} m")

    #the actual trajectory
    t = np.linspace(0, time_travel, 100)
    x_vals = vx * t
    y_vals = initial_height + vy * t - 1/2 * grav * t**2

    



    

         
