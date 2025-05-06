from fourier_law import fourier_law

class fourier_hypothesis_test:
        """
        This class performs a hypothesis test using fourier's law of heat conduction.
        It checks whether the modeled heat transfer rate is within a changeable significance
        of a real real-world measured value.

        parameters:
            k (float): Thermal conductivity (W/m * k)
            A (float): Cross-sectional area (m^2)
            dT_dx (float): Temperature gradient (K/m)
            real_world_value (float): Measured heat transfer rate (W)
            sig (float): significance level as a decimal)
        """
        def __init__(self):
            print("this tests wether a modeled heat transfer rate using fouriers law is close to a real world value.")
            try:
                self.k = float(input("enter thermal conductivity of object (W/m * K):"))
                self.A = float(input("Enter the cross-sectional area (m^2):"))
                self.dT_dx = float(input("Enter the temperature gradient (K/m):"))
                self.real_world_value = float(input("Enter the real-world heat transfer rate (W):"))
                self.sig = float(input("enter the significance (in decimals)"))
                self.run_test()
            except ValueError:
                print("Please enter numeric values.")    
        def run_test(self):
            modeled_value, _ = fourier_law(self.k, self.A, self.dT_dx)
            margin = self.sig * self.real_world_value
            lower_bound = self.real_world_value - margin
            upper_bound = self.real_world_value + margin

            print(f"Hypothesis Test Results of the Fourier Model:")
            print(f"Modeled value: {modeled_value} W")
            print(f"Real-world value: {self.real_world_value} W")
            print(f"Acceptable range: [{lower_bound}, {upper_bound}]")

            if lower_bound <= modeled_value <= upper_bound:
                print (f'Failed to reject null hypothesis at {self.sig} significance level.')
            else:
                print (f'Reject null hypothesis at {self.sig} significance level.') 
        
if __name__ == "__main__":
    test = fourier_hypothesis_test()

