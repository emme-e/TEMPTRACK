def newtons_law_of_cooling(initial_temp, enviroment_temp, h, area, dt, c, m):
    """
    Returns the new temperature of the object after time dt using Newton's Law of Cooling.
    """
    q = h * area * (enviroment_temp - initial_temp)
    delta_T = (q * dt) / (m * c)
    return initial_temp + delta_T

# Example usage
if __name__ == "__main__":
    new_temp = newtons_law_of_cooling(
        initial_temp=80,
        enviroment_temp=25,
        h=10,
        area=0.5,
        dt=60,
        c=4186,
        m=1
    )
    print(f"New temperature: {new_temp:.2f} °C")
