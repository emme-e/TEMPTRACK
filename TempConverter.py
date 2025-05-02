def temp_converter(input_scale, output_scale, temp_env, initial_temp, temp_final):
        """
        Convert temperatures between Celsius, Fahrenheit, and Kelvin.
        uses the formulas:
        - C to F: (C * 9/5) + 32
        - F to C: (F - 32) * 5/9
        - C to K: C + 273.15
        - K to C: K - 273.15
        - F to K: (F + 459.67) * 5/9
        - K to F: (K * 9/5) - 459.67

        Parameters: 
        - input_scale (str): The scale of the input temperatures ('C', 'F', 'K')
        - output_scale (str): The desired output scale ('C', 'F', 'K')
        - temp_env (float): Ambient temperature
        - initial_temp (float): Initial temperature
        - temp_final (float): Final temperature

        Returns:
        - tuple: Converted temperatures in the specified output scale
        """
        if input_scale == output_scale:
            return temp_env, initial_temp, temp_final

        if input_scale == "K":
            if output_scale == "C":
                return temp_env - 273.15, initial_temp - 273.15, temp_final - 273.15
            elif output_scale == "F":
                return (temp_env * 9/5) - 459.67, (initial_temp * 9/5) - 459.67, (temp_final * 9/5) - 459.67
        elif input_scale == "C":
            if output_scale == "K":
                return temp_env + 273.15, initial_temp + 273.15, temp_final + 273.15
            elif output_scale == "F":
                return (temp_env * 9/5) + 32, (initial_temp * 9/5) + 32, (temp_final * 9/5) + 32
        elif input_scale == "F":
            if output_scale == "C":
                return (temp_env - 32) * 5/9, (initial_temp - 32) * 5/9, (temp_final - 32) * 5/9
            elif output_scale == "K":
                return (temp_env + 459.67) * 5/9, (initial_temp + 459.67) * 5/9, (temp_final + 459.67) * 5/9

        raise ValueError("Invalid temperature scale conversion.")

def update_temperature(temp_env_conv, initial_temp_conv, temp_final_conv, output_scale):
    """
    assigning names to the converted temperatures, and ensuring no temperature is below absolute zero.
    """
    temp_env_conv, initial_temp_conv, temp_final_conv = temp_converter(temp_env_conv, initial_temp_conv, temp_final_conv)
    
    if output_scale == "K" and temp_env_conv < -273.15:
        raise ValueError("Temperature below absolute zero in Celsius.")
    elif output_scale == "F" and temp_env_conv < -459.67:
        raise ValueError("Temperature below absolute zero in Fahrenheit.")
    elif output_scale == "K" and temp_env_conv < 0:
        raise ValueError("Temperature below absolute zero in Kelvin.")
    elif output_scale not in ("C", "F", "K"):
        raise ValueError("Invalid temperature scale.")
    
    return temp_env_conv, initial_temp_conv, temp_final_conv
