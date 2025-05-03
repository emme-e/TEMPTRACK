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
