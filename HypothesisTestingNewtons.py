from Newtons import calculate_k, temperature_at_time

def hypothesis_test(initial_temp, temp_final, temp_env, dt, real_world_value):
    """
    Performs a hypothesis test to compare modeled values with real-world values.
    testing to see if the modeled value at the temperature at some time is within 5 percent of the real world value.
    The null hypothesis is that the modeled value is within 5 percent of the real world value.
    
    Parameters:
    - initial_temp (float): Initial temperature of the object.
    - temp_final (float): Final temperature after temp_range time.
    - temp_env (float): Ambient/environment temperature.
    - dt (int): Time step size in seconds.
    - temp_range (int): Total time range to simulate, in minutes.
    - real_world_values (list): List of real-world temperature values for comparison.

    Returns:
    - str: Result of the hypothesis test ("Fail to reject null hypothesis" or "Reject null hypothesis").
    """
    k = calculate_k(initial_temp, temp_final, temp_env, dt)
    modeled_value = temperature_at_time(initial_temp, temp_env, dt, k)
    margin_of_error = 0.05 * real_world_value
    lower_bound = real_world_value - margin_of_error
    upper_bound = real_world_value + margin_of_error
    if lower_bound <= modeled_value <= upper_bound:
        return f'Failed to reject null hypothesis: Modeled value is within 5% of real-world value. Bounded by: [{lower_bound},{upper_bound}].'
    else:
        return f'Reject null hypothesis: Modeled value is outside 5% of real-world value. Bounded by:[{lower_bound},{upper_bound}].'




    