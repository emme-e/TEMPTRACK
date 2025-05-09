def fourier_law(k ,A , dT_dx):
    """
    This function implements Fourier's Law of Heat Conduction.
    It calculates the heat transfer rate (q) through a solid material.

    Fourier's Law states that the heat transfer rate (q) is proportional to the negative gradient of temperature (dT/dx)
    and the area (A) through which the heat is being transferred.

    The formula is given by:
    q = -k * A * (dT/dx)

    parameters:
    k = (float) thermal conductivity (W/m·K)
    A = (float) cross-sectional area (m^2)
    dT/dx = (float) temperature gradient (K/m)

    Returns:
    - q (float): heat transfer rate (W) 
    """
    q = -k * A * dT_dx 
    return round(q,2), f" The Heat transfer rate of q = {q} watts"

import matplotlib.pyplot as plt
import numpy as np

def base_fourier_plot(k, A):
    """
    Plots the heat transfer rate (q) vs temperature gradient (dT/dx)
    using Fourier's law: q = -k * A * dT/dx
    """
    dT_dx = np.linspace(-100, 100, 200)
    q = -k * A * dT_dx

    plt.plot(dT_dx, q)
    plt.title("Heat Transfer Rate vs Temperature Gradient")
    plt.xlabel("Temperature Gradient (dT/dx) [K/m]")
    plt.ylabel("Heat Transfer Rate (q) [W]")
    plt.grid(True)
    plt.show()


def fourier_law(k, A, dT_dx):
    """
    Computes heat transfer rate using Fourier's Law.
    """
    return -k * A * dT_dx

def hypothesis_test_fourier_(k, A, dT_dx, real_value, sig=0.05):
    """
    Compares modeled heat transfer to a real-world value.
    Accepts if it's within the significance of the real-world value.
    """
    modeled = fourier_law(k, A, dT_dx)
    margin = sig * real_value
    lower, upper = real_value - margin, real_value + margin

    print("Fourier Model Hypothesis Test")
    print(f"Modeled: {modeled:.2f} W")
    print(f"Observed: {real_value:.2f} W")
    print(f"Acceptable range: [{lower:.2f}, {upper:.2f}]")

    if lower <= modeled <= upper:
        print(f"Failed to reject at {sig*100:.0f}% significance level")
    else:
        print(f"Rejected at {sig*100:.0f}% significance level")










    
