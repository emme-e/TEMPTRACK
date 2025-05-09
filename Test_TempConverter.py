from TempConverter import temp_converter
from Newtons import calculate_k, temperature_at_time

def k_to_c():
    """
    Test the temp_converter function with Kelvin to Celsius.
    """
    input_scale = "K"
    output_scale = "C"
    temp_env = 300.0
    initial_temp = 350.0
    temp_final = 330.0

    expected = (temp_env - 273.15, initial_temp - 273.15, temp_final - 273.15)
    result = temp_converter(input_scale, output_scale, temp_env, initial_temp, temp_final)

    assert result == expected, f"Expected {expected}, got {result}"

def c_to_k():
    """
    Test the temp_converter function with Celcius to Kelvin.
    """
    input_scale = "C"
    output_scale = "K"
    temp_env = 25.0
    initial_temp = 100.0
    temp_final = 50.0

    expected = (temp_env + 273.15, initial_temp + 273.15, temp_final + 273.15)
    result = temp_converter(input_scale, output_scale, temp_env, initial_temp, temp_final)

    assert result == expected, f"Expected {expected}, got {result}"


def f_to_k():
    """
    Test the temp_converter function with Farenheight to Kelvin.
    """
    input_scale = "F"
    output_scale = "K"
    temp_env = 32.0
    initial_temp = 212.0
    temp_final = 100.0

    expected = ((temp_env + 459.67) * 5/9, (initial_temp + 459.67) * 5/9, (temp_final + 459.67) * 5/9)
    result = temp_converter(input_scale, output_scale, temp_env, initial_temp, temp_final)

    assert result == expected, f"Expected {expected}, got {result}"

def k_to_f():
    """
    Test the temp_converter function with Kelvin to Farenheight.
    """
    input_scale = "K"
    output_scale = "F"
    temp_env = 300.0
    initial_temp = 350.0
    temp_final = 330.0

    expected = ((temp_env * 9/5) - 459.67, (initial_temp * 9/5) - 459.67, (temp_final * 9/5) - 459.67)
    result = temp_converter(input_scale, output_scale, temp_env, initial_temp, temp_final)

    assert result == expected, f"Expected {expected}, got {result}"

def c_to_f():
    """
    Test the temp_converter function with Celcius to Farenheight.
    """
    input_scale = "C"
    output_scale = "F"
    temp_env = 25.0
    initial_temp = 100.0
    temp_final = 50.0

    expected = (temp_env * 9/5 + 32, initial_temp * 9/5 + 32, temp_final * 9/5 + 32)
    result = temp_converter(input_scale, output_scale, temp_env, initial_temp, temp_final)

    assert result == expected, f"Expected {expected}, got {result}"

def f_to_c():
    """
    Test the temp_converter function with Farenheight to Celcius.
    """
    input_scale = "F"
    output_scale = "C"
    temp_env = 32.0
    initial_temp = 212.0
    temp_final = 100.0

    expected = ((temp_env - 32) * 5/9, (initial_temp - 32) * 5/9, (temp_final - 32) * 5/9)
    result = temp_converter(input_scale, output_scale, temp_env, initial_temp, temp_final)

    assert result == expected, f"Expected {expected}, got {result}"


def conv_temp_at_time(input_scale, output_scale, initial_temp, temp_final, temp_env, dt):
    """
    Convert temperatures and calculate temperature at a given time using the cooling constant 'k'.
    """
    temp_env_conv, initial_temp_conv, temp_final_conv = temp_converter(input_scale, output_scale, temp_env, initial_temp, temp_final)
    k = calculate_k(initial_temp_conv, temp_final_conv, temp_env_conv, dt)

    conv_temp_at_time = temperature_at_time(initial_temp_conv, temp_env_conv, k, dt)
    return conv_temp_at_time
    

def conv_rate_of_change(input_scale, output_scale, initial_temp, temp_final, temp_env, dt):
    """
    Convert temperatures and calculate the rate of change using the cooling constant 'k'.
    temp_env_conv isnt required to be converted, as it is the same in both scales, but is included for consistency.
    """
    temp_env_conv, initial_temp_conv, temp_final_conv = temp_converter(input_scale, output_scale, temp_env, initial_temp, temp_final)
    rate = round((initial_temp_conv - temp_final_conv) / dt,2)

    return rate

print(conv_rate_of_change(input_scale = "C", output_scale = "F", initial_temp = 100, temp_final = 70, temp_env = 50, dt = 10))
