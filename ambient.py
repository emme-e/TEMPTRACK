def newtons_law_of_cooling(temp_object, temp_env, h, area, dt, c, m):
    """
    Returns the new temperature of the object after time dt using Newton's Law of Cooling.
    
    Parameters:
    - temp_object: current temperature of the object (°C)
    - temp_env: ambient temperature (°C)
    - h: heat transfer coefficient (W/m^2·K)
    - area: surface area of the container (m^2)
    - dt: time step (seconds)
    - c: specific heat capacity of the material (J/kg·K)
    - m: mass of the object (kg)
    """
    q = h * area * (temp_env - temp_object)  # Heat transfer rate (W)
    delta_T = (q * dt) / (m * c)             # Temperature change
    return temp_object + delta_T