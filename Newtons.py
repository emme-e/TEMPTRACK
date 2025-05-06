import math

def rate_of_change(initial_temp, temp_final, dt):
    """
    Calculates the rate of temperature change (dy/dt).

    Parameters:
    - initial_temp (float): Initial temperature of the object
    - final_temp (float): Final temperature after the time interval
    - dt (float): Time over which cooling occurs (in seconds)

    Returns:
    - float: Rate of temperature change

    Raises:
    - ValueError: If time_interval is zero
    """
    if dt == 0:
        raise ValueError("Time final cannot be zero.")
    rate = round((initial_temp - temp_final) / dt,2)
    return rate


def calculate_k(initial_temp, temp_final, temp_env, dt):
    """
    Calculates the cooling constant 'k' using Newton's Law of Cooling.
    
    Parameters:
    - initial_temp(float): Initial temperature of the object
    - final_temp(float): Final temperature after time dt
    - ambient_temp(float): Ambient/environment temperature
    - dt(float): Time interval in minutes

    Returns:
    - float: Cooling constant k

    Raises:
    - ValueError: If temperatures are invalid for the formula
    """
    if temp_final == temp_env:
        raise ValueError("final temperature cannot equal environment temperature, as ln(0) is undefined .")
    if initial_temp == temp_env:
        raise ValueError("Initial temperature cannot equal environment temperature, as it causes division by zero.")
    
    ratio = (temp_final - temp_env) / (initial_temp - temp_env)
    if ratio <= 0:
       raise ValueError("The ratio of temperatures must be positive for the logarithm to be defined.")
    if dt <= 0:
        raise ValueError("Time interval must be positive.")
    k = round(-math.log((temp_final - temp_env) / (initial_temp - temp_env)) /dt, 2)
    return k


def temperature_at_time(initial_temp, temp_env, dt, k):
    """
    Calculates the temperature of an object at a given time using the cooling constant 'k'.
    This is based on the formula:
    T(t) = T_env + (T_initial - T_env) * e^(-k * t)

    Parameters:
    - initial_temp (float): Initial temperature of the object
    - ambient_temp (float): Ambient/environment temperature
    - dt (float): Time in minutes
    - k (float): Cooling constant

    Returns:
    - float: Temperature at time t

    Raises:
    - ValueError: If cooling constant k has not been set
    """
    if k is None:
        raise ValueError("Cooling constant k is not set. Run calculate_k() first.")
    return round(temp_env + (initial_temp - temp_env) * math.exp(-k * dt), 2)
