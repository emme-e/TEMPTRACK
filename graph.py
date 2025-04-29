import temp_converter
import matplotlib.pyplot as plt
from newtons_law_of_cooling import newtons_law_of_cooling
import matplotlib.pyplot as plt

def plot_temperature(time_series, temperatures, output_scale):
    """
    Plots the temperature vs time graph.
    """
    plt.figure(figsize=(10, 5))
    plt.plot(time_series, temperatures, marker='o', linestyle='-', color='teal')
    plt.title("Cooling of an Object Over Time (Newton's Law of Cooling)")
    plt.xlabel("Time (seconds)")
    plt.ylabel(f"Temperature ({output_scale})")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
