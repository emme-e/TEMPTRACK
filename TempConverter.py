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
        - Raises ValueError if the input scale is invalid or if the conversion results
          in a temperature below absolute zero.
        """
        if input_scale == output_scale:
            return temp_env, initial_temp, temp_final

        if input_scale == "K":
            if output_scale == "C":
                temp_env_conv = temp_env - 273.15
                initial_temp_conv = initial_temp - 273.15
                temp_final_conv = temp_final - 273.15
                if temp_env_conv < -273.15 or initial_temp_conv < -273.15 or temp_final_conv < -273.15:
                    raise ValueError("Temperature below absolute zero in Celsius.")
                return temp_env_conv, initial_temp_conv, temp_final_conv
            
            elif output_scale == "F":
                temp_env_conv, initial_temp_conv, temp_final_conv = (temp_env * 9/5) - 459.67, (initial_temp * 9/5) - 459.67, (temp_final * 9/5) - 459.67
                if temp_env_conv < -459.67 or initial_temp_conv < -459.67 or temp_final_conv < -459.67:
                    raise ValueError("Temperature below absolute zero in Fahrenheit.")
                return temp_env_conv, initial_temp_conv, temp_final_conv
            
        elif input_scale == "C":
            if output_scale == "K":
                temp_env, initial_temp, temp_final = temp_env + 273.15, initial_temp + 273.15, temp_final + 273.15
                if temp_env < 0 or initial_temp < 0 or temp_final < 0:
                    raise ValueError("Temperature below absolute zero in Kelvin.")
                return temp_env, initial_temp, temp_final
            
            elif output_scale == "F":
                temp_env, initial_temp, temp_final = (temp_env * 9/5) + 32, (initial_temp * 9/5) + 32, (temp_final * 9/5) + 32
                if temp_env < -459.67 or initial_temp < -459.67 or temp_final < -459.67:
                    raise ValueError("Temperature below absolute zero in Fahrenheit.")
                return temp_env, initial_temp, temp_final
            
        elif input_scale == "F":
            if output_scale == "C":
                temp_env, initial_temp, temp_final = (temp_env - 32) * 5/9, (initial_temp - 32) * 5/9, (temp_final - 32) * 5/9
                if temp_env < -273.15 or initial_temp < -273.15 or temp_final < -273.15:    
                    raise ValueError("Temperature below absolute zero in Celsius.")
                return temp_env, initial_temp, temp_final
            
            elif output_scale == "K":
                temp_env, initial_temp, temp_final = (temp_env + 459.67) * 5/9, (initial_temp + 459.67) * 5/9, (temp_final + 459.67) * 5/9
                if temp_env < 0 or initial_temp < 0 or temp_final < 0:
                    raise ValueError("Temperature below absolute zero in Kelvin.")
                return temp_env, initial_temp, temp_final

        raise ValueError("Invalid temperature scale conversion.")
