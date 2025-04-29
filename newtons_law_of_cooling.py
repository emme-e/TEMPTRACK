def newtons_law_of_cooling(initial_temp, enviroment_temp, h, area, dt, c, m):
    """
    Returns the new temperature of the object after time dt using Newton's Law of Cooling.
    ... need to make some parameters... follow the video
    """
    q = h * area * (enviroment_temp - initial_temp)
    delta_T = (q * dt) / (m * c)
    return initial_temp + delta_T
