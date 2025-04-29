from newtons_law_of_cooling import newtons_law_of_cooling
from graph import plot_temperature

class CoolingSimulation:
    def __init__(self, initial_temp, env_temp, temp_scale="C", output_scale="C",
                 h=10, area=0.1, dt=100, c=4186, m=0.5, total_time=600):
        self.initial_temp = initial_temp
        self.env_temp = env_temp
        self.temp_scale = temp_scale
        self.output_scale = output_scale
        self.h = h
        self.area = area
        self.dt = dt
        self.c = c
        self.m = m
        self.total_time = total_time
        
        # Convert temperatures if needed
        self.env_temp, self.initial_temp = self.temp_converter(
            temp_scale, output_scale, env_temp, initial_temp
        )
        
        self.time_series = list(range(0, total_time + dt, dt))
        self.temperatures = []
        
    def temp_converter(self, temp_scale, output_scale, env_temp, start_temp):
        if temp_scale == output_scale:
            return env_temp, start_temp
        
        if temp_scale == "K":
            if output_scale == "C":
                return env_temp - 273.15, start_temp - 273.15
            elif output_scale == "F":
                return (env_temp * 9/5) - 459.67, (start_temp * 9/5) - 459.67
        elif temp_scale == "C":
            if output_scale == "K":
                return env_temp + 273.15, start_temp + 273.15
            elif output_scale == "F":
                return (env_temp * 9/5) + 32, (start_temp * 9/5) + 32
        elif temp_scale == "F":
            if output_scale == "C":
                return (env_temp - 32) * 5/9, (start_temp - 32) * 5/9
            elif output_scale == "K":
                return (env_temp + 459.67) * 5/9, (start_temp + 459.67) * 5/9
        
        raise ValueError("Invalid temperature scale conversion.")

    def update_temperature(self, temperature, unit):
        if unit == "C" and temperature < -273.15:
            temperature = -273.15
        elif unit == "F" and temperature < -459.67:
            temperature = -459.67
        elif unit == "K" and temperature < 0:
            temperature = 0
        elif unit not in ("C", "F", "K"):
            raise ValueError("Invalid unit. Use 'C', 'F', or 'K'.")
        return temperature

    def run_simulation(self):
        temp = self.initial_temp
        
        for t in self.time_series:
            self.temperatures.append(temp)
            temp = newtons_law_of_cooling(temp, self.env_temp, self.h, self.area, self.dt, self.c, self.m)
            temp = self.update_temperature(temp, self.output_scale)

    def plot(self):
        plot_temperature(self.time_series, self.temperatures, self.output_scale)