def test_hypothesis_test():
    """
    Test the hypothesis test function.
    """
    initial_temp = 100
    temp_final = 70
    temp_env = 60
    dt = 10
    real_world_value = 75

    k = calculate_k(initial_temp, temp_final, temp_env, dt)
    modeled_value = temperature_at_time(initial_temp, temp_env, dt, k)
    margin_of_error = 0.05 * real_world_value
    lower_bound = real_world_value - margin_of_error
    upper_bound = real_world_value + margin_of_error
    
    result = hypothesis_test(initial_temp, temp_final, temp_env, dt, real_world_value)
    
    assert (
        ("Failed to reject null hypothesis" in result and lower_bound <= modeled_value <= upper_bound)
        or
        ("Reject null hypothesis" in result and not (lower_bound <= modeled_value <= upper_bound))
    ), f"Expected {result} to be within bounds [{lower_bound}, {upper_bound}]."