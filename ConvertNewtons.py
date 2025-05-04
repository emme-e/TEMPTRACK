from Newtons import temperature_at_time, calculate_k, rate_of_change
from TempConverter import temp_converter

def conv_temp_at_time(input_scale, output_scale, initial_temp, temp_final, temp_env, dt):
    """
    Convert temperatures and calculate temperature at a given time using the cooling constant 'k'.
    """
    temp_env_conv, initial_temp_conv, temp_final_conv = temp_converter(input_scale, output_scale, temp_env, initial_temp, temp_final)
    k = calculate_k(initial_temp_conv, temp_final_conv, temp_env_conv, dt)

    conv_temp_at_time = round(temperature_at_time(initial_temp_conv, temp_env_conv, k, dt),2)
    return conv_temp_at_time
    

def conv_rate_of_change(input_scale, output_scale, initial_temp, temp_final, temp_env, dt):
    """
    Convert temperatures and calculate the rate of change using the cooling constant 'k'.
    temp_env_conv isnt required to be converted, as it is the same in both scales, but is included for consistency.
    """
    temp_env_conv, initial_temp_conv, temp_final_conv = temp_converter(input_scale, output_scale, temp_env, initial_temp, temp_final)
    rate = round(rate_of_change(initial_temp_conv, temp_final_conv, dt))

    return rate
