from fourier_law import fourier_law

class FourierHypothesisTest:
    """
    This class performs a hypothesis test using fourier's law of heat conduction.
    It checks whether the modeled heat transfer rate is within an acceptable 
    margin of a measured real-world value.
    """

    def __init__(self, k, A, dT_dx, real_world_value, sig=0.05):
        """
        Sets up the hypothesis test using real-world measurements and details about the material.

        Parameters:
            k (float): Thermal conductivity (W/m * K)
            A(float): Cross-sectional area (m²)
            dT_dx (float): Temperature gradient (K/m)
            real_world_value (float): Measured heat transfer rate (W)
            sig (float): Significance level (default is 0.05)
        """
        
        self.k = k
        self.A = A
        self.dT_dx = dT_dx
        self.real_world_value = real_world_value
        self.sig = sig
            
    def run_test(self):
        """
        user will run the hypothesis test and print the result.
        """
        modeled_value, _ = fourier_law(self.k, self.A, self.dT_dx)
        margin = self.sig * self.real_world_value
        lower_bound = self.real_world_value - margin
        upper_bound = self.real_world_value + margin

        print(f"Hypothesis Test Results of the Fourier Model:")
        print(f"Modeled value: {modeled_value} W")
        print(f"Real-world value: {self.real_world_value} W")
        print(f"Acceptable range: [{lower_bound}, {upper_bound}]")

        if lower_bound <= modeled_value <= upper_bound:
            print (f'Failed to reject null hypothesis at {self.sig * 100:.1f}% significance level.')
        else:
            print (f'Reject null hypothesis at {self.sig * 100:.1f}% significance level.') 

def main():
    try:
        k = float(input("Thermal conductivity k (W/m·K): "))
        A = float(input("Cross-sectional area A (m²): "))
        dT_dx = float(input("Temperature gradient (K/m): "))
        real_value = float(input("Measured heat transfer rate (W): "))
        sig = float(input("Significance level (e.g., 0.05): "))

        test = FourierHypothesisTest(k, A, dT_dx, real_value, sig)
        test.run_test()
    except ValueError:
        print("Please enter valid numeric values.")

if __name__ == "__main__":
    main()




    
