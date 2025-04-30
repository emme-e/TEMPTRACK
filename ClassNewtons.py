import math

class class_newtons:
    """
    Implements Newton's Law of Cooling.

    This law states that the rate of change of temperature of an object is proportional
    to the difference between its own temperature and the ambient temperature.
    """
    def __init__(self, k=None):
        self.k = k

    def rate_of_change(self, initial_temp, temp_final, time_interval):
        """
        Calculates the rate of temperature change (dy/dt).
        Parameters:
        - initial_temp (float): Initial temperature of the object
        - final_temp (float): Final temperature after the time interval
        - time_interval (float): Time over which cooling occurs

        Returns:
        - float: Rate of temperature change

        Raises:
        - ValueError: If time_interval is zero
        """
        if time_interval == 0:
            raise ValueError("Time final cannot be zero.")
        rate = (initial_temp - temp_final) / time_interval
        return rate

    def calculate_k(self, initial_temp, temp_final, temp_env, dt):
        """
        Calculates the cooling constant 'k' using Newton's Law of Cooling.
        Parameters:
        - initial_temp(float): Initial temperature of the object
        - final_temp(float): Final temperature after time dt
        - ambient_temp(float): Ambient/environment temperature
        - dt(float): Time interval in seconds

        Returns:
        - float: Cooling constant k

        Raises:
        - ValueError: If temperatures are invalid for the formula
        """
        if temp_final == temp_env:
            raise ValueError("final temperature cannot equal enviorment temperature, as ln(0) is undefined .")
        if initial_temp == temp_env:
            raise ValueError("Initial temperature cannot equal environment temperature, as it causes division by zero.")
        self.k = -math.log((temp_final - temp_env) / (initial_temp - temp_env)) / dt
        return self.k

    def temperature_at_time(self, initial_temp, temp_env, dt):
        """
        Calculates the temperature of an object at a given time using the cooling constant 'k'.
        This is based on the formula:
        T(t) = T_env + (T_initial - T_env) * e^(-k * t)

        Parameters:
        - initial_temp (float): Initial temperature of the object
        - ambient_temp (float): Ambient/environment temperature
        - dt (float): Time in seconds

        Returns:
        - float: Temperature at time t

        Raises:
        - ValueError: If cooling constant k has not been set
        """
        if self.k is None:
            raise ValueError("Cooling constant k is not set. Run calculate_k() first.")
        return temp_env + (initial_temp - temp_env) * math.exp(-self.k * dt)
