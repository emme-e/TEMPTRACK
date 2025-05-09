def fourier_law(k ,A , dT_dx):
    """
    This function implements Fourier's Law of Heat Conduction.
    It calculates the heat transfer rate (q) through a solid material.

    Fourier's Law states that the heat transfer rate (q) is proportional to the negative gradient of temperature (dT/dx)
    and the area (A) through which the heat is being transferred.

    The formula is given by:
    q = -k * A * (dT/dx)

    parameters:
    k = (float) thermal conductivity (W/m·K)
    A = (float) cross-sectional area (m^2)
    dT/dx = (float) temperature gradient (K/m)

    Returns:
    - q (float): heat transfer rate (W) 
    """
    q = -k * A * dT_dx 
    return round(q,2), f" The Heat transfer rate of q = {q} watts"

class FourierHypothesisTest:
    """
    This class performs a hypothesis test using Fourier's law of heat conduction.
    """
    def __init__(self, k, A, dT_dx, real_world_value, sig=0.05):
        self.k = k
        self.A = A
        self.dT_dx = dT_dx
        self.real_world_value = real_world_value
        self.sig = sig
            
    def run_test(self):
        modeled_value, _ = fourier_law(self.k, self.A, self.dT_dx)
        margin = self.sig * self.real_world_value
        lower_bound = self.real_world_value - margin
        upper_bound = self.real_world_value + margin

        print("Hypothesis Test Results of the Fourier Model:")
        print(f"Modeled value: {modeled_value} W")
        print(f"Real-world value: {self.real_world_value} W")
        print(f"Acceptable range: [{lower_bound}, {upper_bound}]")

        if lower_bound <= modeled_value <= upper_bound:
            print(f" Failed to reject null hypothesis at {self.sig * 100:.1f}% significance level.")
        else:
            print(f"Reject null hypothesis at {self.sig * 100:.1f}% significance level.")











    