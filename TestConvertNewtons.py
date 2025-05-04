from Newtons import temperature_at_time, calculate_k, rate_of_change
from TempConverter import temp_converter
from ConvertNewtons import conv_temp_at_time, conv_rate_of_change

def test_conv_temp_at_time():
    """
    Test the conv_temp_at_time function with Celcius to Farenheight.
    """
    input_scale = "C"
    output_scale = "F"
    temp_env = 60.0
    initial_temp = 100.0
    temp_final = 70.0
    dt = 10.0

    temp_env_conv, initial_temp_conv, temp_final_conv = temp_converter(input_scale, output_scale, temp_env, initial_temp, temp_final)

    k = calculate_k(initial_temp_conv, temp_final_conv, temp_env_conv, dt)
    ex_conv_temp_at_time = temperature_at_time(initial_temp_conv, temp_env_conv, k, dt)

    result = conv_temp_at_time(input_scale, output_scale, initial_temp, temp_final ,temp_env, dt)

    assert result == ex_conv_temp_at_time, f"Expected {conv_temp_at_time}, got {result}"

test_conv_temp_at_time()

def test_conv_rate_of_change():
    """
    Test the conv_rate_of_change function with Celcius to Farenheight.
    """
    input_scale = "C"
    output_scale = "F"
    temp_env = 60.0
    initial_temp = 100.0
    temp_final = 70.0
    dt = 10.0

    temp_env_conv, initial_temp_conv, temp_final_conv = temp_converter(input_scale, output_scale, temp_env, initial_temp, temp_final)
    result = rate_of_change(initial_temp_conv, temp_final_conv, dt)

    ex_conv_rate_of_change = conv_rate_of_change(input_scale, output_scale, initial_temp, temp_final, dt)

    assert result == ex_conv_rate_of_change, f"Expected {ex_conv_rate_of_change}, got {result}"

test_conv_rate_of_change()
