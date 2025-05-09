def run_hypothesis_test(k, A, dT_dx, real_value, sig=0.05):
    """
    Compare modeled value to real-world value within a given significance level.
    """
    modeled = fourier_law(k, A, dT_dx)
    margin = sig * real_value
    lower = real_value - margin
    upper = real_value + margin

    print("\nHypothesis Test:")
    print(f"Modeled: {modeled:.2f} W")
    print(f"Measured: {real_value:.2f} W")
    print(f"Acceptable range: [{lower:.2f}, {upper:.2f}]")

    if lower <= modeled <= upper:
        print(f"Model acceptable at {sig*100:.1f}% significance level.")
    else:
        print(f"Model rejected at {sig*100:.1f}% significance level.")

def main():
    try:
        k = float(input("Thermal conductivity k (W/m·K): "))
        A = float(input("Cross-sectional area A (m²): "))
        dT_dx = float(input("Temperature gradient (K/m): "))
        real_value = float(input("Measured heat transfer rate (W): "))
        sig_input = input("Significance level (default 0.05): ")
        sig = float(sig_input) if sig_input else 0.05

        run_hypothesis_test(k, A, dT_dx, real_value, sig)
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()




    
