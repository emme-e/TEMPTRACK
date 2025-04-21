"""
import TemperatureConverter
import newtons_law_of_cooling
"""

import matplotlib.pyplot as plt

#below are just example values
initial_temp = 90    
enviroment_temp = 25  
h = 10                 
area = 0.1             
dt = 100                
c = 4186                
m = 0.5                 
total_time = 600        

time_series = list(range(0, total_time + dt, dt))
temperatures = []

temp = initial_temp
for t in time_series:
    temperatures.append(temp)
    temp = newtons_law_of_cooling(initial_temp, enviroment_temp, h, area, dt, c, m)

plt.figure(figsize=(10, 5))
plt.plot(time_series, temperatures, marker='o', linestyle='-', color='teal')
plt.title("Cooling of an Object Over Time (Newton's Law of Cooling)")
plt.xlabel("Time (seconds)")
plt.ylabel(f"Temperature {temp_converter.output_scale}")
plt.grid(True)
plt.tight_layout()
plt.show()