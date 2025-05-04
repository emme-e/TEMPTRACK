import matplotlib.pyplot as plt
from Newtons import calculate_k, temperature_at_time

def graphing_newtons(input_scale,initial_temp, temp_final, temp_env, dt, temp_range):
    """
    Plots temperature change over time using Newton's Law of Cooling.

    Parameters:
    - initial_temp (float): Initial temperature of the object.
    - temp_final (float): Final temperature after temp_range time.
    - temp_env (float): Ambient/environment temperature.
    - dt (int): Time step size. in seconds
    - temp_range (int): Total time range to simulate, in minutes

    returns:
    - Displays a plot of temperature change over time.

    Notes:
    Only need to measure 3 real-world values to predict the temperature at any time.
    """
    times = list(range(0, temp_range + 1, dt))
    k = calculate_k(initial_temp, temp_final, temp_env, temp_range)
    temps = [temperature_at_time(initial_temp, temp_env, t, k) for t in times]

    plt.plot(times, temps, label='Temperature')
    plt.xlabel('Time (minutes)')
    if input_scale == "C" or input_scale == "F":
        plt.ylabel(f'Temperature (°{input_scale})')
    else:
        plt.ylabel('Temperature (K)')
    plt.title("Newton's Law of Cooling")
    plt.legend()
    plt.grid(True)
    plt.show()
