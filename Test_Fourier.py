from fourier_law import fourier_law 
import math
def test_fourier_law(k ,A , dT_dx):
    """ testing the heat transfer rate through a solid

    Args:
        k (float): this is the thermal conductivity and treated as the constant
        A (float): this represents the cross sectional area of the solid we are testing
        dT_dx (float): this is the temperature gradient measuring the rate of heat transfer
    """
    k = 200
    A = 0.01
    dT_dx = 75

    expected_q = -k * A * dT_dx
    result_q, _ = fourier_law(k, A, dT_dx)

    assert math.isclose(expected_q, result_q, rel_tol=1e-5), f"Expected {expected_q}, but got {result_q}"
   
def test_hypothesis_test():
    """ testing the hypothesis test of the fourier law wether the modeled value is within the acceptable range of the real world value
    Args: 
        k (float): this is the thermal conductivity and treated as the constant
        A (float): this represents the cross sectional area of the solid we are testing
        dT_dx (float): this is the temperature gradient measuring the rate of heat transfer
        real_world_value (float): this is the measured heat transfer rate
        sig (float): this is the significance level
    """
    k = 200
    A = 0.01
    dT_dx = 75
    real_world_value = -160
    sig = 0.05

    modeled_value, _ = fourier_law(k, A, dT_dx)
    margin = sig * abs(real_world_value)
    lower_bound = real_world_value - margin
    upper_bound = real_world_value + margin

    assert lower_bound <= modeled_value <= upper_bound, f"Modeled value {modeled_value} is outside the acceptable range [{lower_bound}, {upper_bound}]"

test_fourier_law()
test_hypothesis_test()
   



