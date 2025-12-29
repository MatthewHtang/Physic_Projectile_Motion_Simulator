#Projectile Motion Simulator

import math
import numpy as np
import matplotlib.pyplot as plt

initial_velocity = float(input ("Enter initial velocity (m/s): "))
initial_height = float(input ("Enter initial height (m): "))
launch_angle = float(input("Enter launch angle (degree): "))
gravity = input("Enter your planet (earth, moon, mars, etc): ").lower()

#converting angle
launch_degree = math.radians(launch_angle)

#velocity components
vx = initial_velocity * math.cos(launch_degree)
vy = initial_velocity * math.sin(launch_degree)

#gravity
planet_gravity = [["earth", 9.8], ["mercury", 3.7], ["venus", 8.9], 
                  ["moon", 1.6], ["mars", 3.7], ["jupiter", 23.1], 
                   ["saturn", 9.0], ["uranus", 8.7], ["neptune", 11.0], 
                   ["pluto", 0.7], ["sun", 274]]

grav = None
for planet in planet_gravity:
    if planet [0] == gravity:
        grav = planet[1]

#if the initial height is 0 meter
if initial_height <= 0:
    time_travel = (2 * vy) / grav
    max_height = (vy ** 2) / (2 * grav)
    final_position = vx * time_travel
#if the initial height is greater than 0 meter
elif initial_height != 0:
    time_travel = (vy + math.sqrt(vy**2 + 2 * grav * initial_height)) / grav
    max_height = initial_height + (vy**2) / (2 * grav)
    final_position = vx * time_travel

print("Time Travel: ", round(time_travel, 2), "s")
print("Maximum Height: ", round(max_height, 2), "m")
print("Final Position: ", round(final_position, 2),  "m")

#graphing the result
t = np.linspace(0, time_travel, 100)

x = vx * t
y = initial_height + vy * t - 0.5 * grav * t**2

plt.plot(x, y)
plt.xlabel("Distance (m)")
plt.ylabel("Height (m)")
plt.title("Projectile Motion")
plt.show()



