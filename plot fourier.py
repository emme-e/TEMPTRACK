import sympy as sym
import matplotlib.pyplot as plt
import numpy as np

def fourier_plot(k_value, A_value):
    """
    shows how the modeled heat transfer rate (q) responds to changes in the temperature gradient (dT/dx)
    based on Fourier's law. 

    Parameters:
        k_value (float): Thermal conductivity (W/m * K)
        A_value (float): Cross_sectional area (m^2)
    """
    k, A, x = sym.symbols("k A x")
    T = sym.Function("T")(x)  
    q_expression = -k * A * sym.diff(T, x)

    temp_gradients = np.linspace(-100, 100, 100)
    heat_transfer_rates = []

    for dTdx_value in temp_gradients:
        q_value = q_expression.subs({k: k_value, A: A_value, sym.diff(T, x): dTdx_value})
        q_value_numeric = sym.N(q_value)
        heat_transfer_rates.append(q_value_numeric)

    plt.plot(temp_gradients, heat_transfer_rates)
    plt.title("Heat Transfer Rate vs Temperature Gradient")
    plt.xlabel("Temperature Gradient (dT/dx) in K/m")
    plt.ylabel("Heat Transfer Rate (q) in Watts")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    try:
        k = float(input("Enter thermal conductivity k (W/m·K): "))
        A = float(input("Enter cross-sectional area A (m^2): "))
        fourier_plot(k, A)
    except ValueError:
        print("please enter valid numeric values for k and A.")


