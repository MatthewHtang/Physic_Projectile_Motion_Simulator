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

# ---------------- SIMULATION ----------------
def launch():
    global x_vals, y_vals, index

    initial_velocity = velocity_slider.get()
    initial_height = height_slider.get()
    launch_angle = angle_slider.get()
    gravity = planet_var.get()

    # converting angle
    launch_degree = math.radians(launch_angle)

    # velocity components
    vx = initial_velocity * math.cos(launch_degree)
    vy = initial_velocity * math.sin(launch_degree)

    grav = None
    for planet in planet_gravity:
        if planet[0] == gravity:
            grav = planet[1]

    if grav is None:
        return

    # physics
    if initial_height <= 0:
        time_travel = (2 * vy) / grav
        max_height = (vy ** 2) / (2 * grav)
    else:
        time_travel = (vy + math.sqrt(vy**2 + 2 * grav * initial_height)) / grav
        max_height = initial_height + (vy**2) / (2 * grav)

    final_position = vx * time_travel

    # update labels
    time_label.config(text=f"Time: {time_travel:.2f} s")
    height_label.config(text=f"Max Height: {max_height:.2f} m")
    range_label.config(text=f"Range: {final_position:.2f} m")

    # trajectory
    t = np.linspace(0, time_travel, 100)
    x_vals = vx * t
    y_vals = initial_height + vy * t - 0.5 * grav * t**2

    ax.clear()
    ax.set_xlabel("Distance (m)")
    ax.set_ylabel("Height (m)")
    ax.set_title("Projectile Motion")
    ax.grid(True)

    index = 0
    animate()

# ---------------- MANUAL ANIMATION ----------------
def animate():
    global index
    if index < len(x_vals):
        ax.plot(x_vals[index], y_vals[index], "ro")
        canvas.draw()
        index += 1
        root.after(30, animate)

# ---------------- GUI ----------------
root = tk.Tk()
root.title("Projectile Motion Simulator")

# Graph
fig, ax = plt.subplots(figsize=(6, 4))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.LEFT, padx=10)

# Controls
controls = tk.Frame(root)
controls.pack(side=tk.RIGHT, padx=10)

tk.Label(controls, text="Initial Velocity (m/s)").pack()
velocity_slider = tk.Scale(controls, from_=0, to=100, orient=tk.HORIZONTAL)
velocity_slider.set(25)
velocity_slider.pack()

tk.Label(controls, text="Launch Angle (degrees)").pack()
angle_slider = tk.Scale(controls, from_=0, to=90, orient=tk.HORIZONTAL)
angle_slider.set(45)
angle_slider.pack()

tk.Label(controls, text="Initial Height (m)").pack()
height_slider = tk.Scale(controls, from_=0, to=50, orient=tk.HORIZONTAL)
height_slider.set(0)
height_slider.pack()

tk.Label(controls, text="Planet").pack()
planet_var = tk.StringVar(value="earth")
planet_menu = tk.OptionMenu(controls, planet_var, "earth", "moon", "mars")
planet_menu.pack()

tk.Button(controls, text="Launch", command=launch).pack(pady=10)

# Results
tk.Label(controls, text="Results", font=("Arial", 10, "bold")).pack()
time_label = tk.Label(controls, text="Time: 0.00 s")
time_label.pack()
height_label = tk.Label(controls, text="Max Height: 0.00 m")
height_label.pack()
range_label = tk.Label(controls, text="Range: 0.00 m")
range_label.pack()

# ---------------- START ----------------
x_vals = []
y_vals = []
index = 0

root.mainloop()
