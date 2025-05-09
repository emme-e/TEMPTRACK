import numpy as np
import matplotlib.pyplot as plt

def fourier_plot(k_value, A_value):
    """
    Plots how the modeled heat transfer rate (q) responds to changes
    in the temperature gradient (dT/dx) using Fourier's Law:
    
    q = -k * A * (dT/dx)

    Parameters:
        k_value (float): Thermal conductivity (W/m·K)
        A_value (float): Cross-sectional area (m²)
    """
    temp_gradients = np.linspace(-100, 100, 200)  
    heat_transfer_rates = -k_value * A_value * temp_gradients  

    plt.plot(temp_gradients, heat_transfer_rates)
    plt.title("Heat Transfer Rate vs Temperature Gradient")
    plt.xlabel("Temperature Gradient (dT/dx) [K/m]")
    plt.ylabel("Heat Transfer Rate (q) [W]")
    plt.grid(True)
    plt.show()

k = float(input("Enter thermal conductivity k (W/m·K): "))
A = float(input("Enter cross-sectional area A (m²): "))
fourier_plot(k, A)


