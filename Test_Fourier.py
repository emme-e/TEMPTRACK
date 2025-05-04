from fourier_law import fourier_law 
import math
def test_fourier_law(k ,A , dT_dx):
    """ testing the heat transfer rate through a solid

    Args:
        k (float): this is the thermal conductivity and treated as the constant
        A (float): this represents the cross sectional area of the solid we are testing
        dT_dx (float): this is the temperature gradient measuring the rate of heat transfer
    """
    k = 50
    A = 100
    dT_dx = 3

    expected_q = -k * A * dT_dx
    result_q, _ = fourier_law(k, A, dT_dx)
    assert math.isclose(expected_q, result_q, rel_tol=1e-5), f"Expected {expected_q}, but got {result_q}"
    print("test_fourier_law passed")
   

if __name__ == "__main__":
    test_fourier_law(50,100,3)


