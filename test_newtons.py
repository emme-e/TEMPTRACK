"""
1st test for newtons_law_of_cooling.py
"""

from newtons_law_of_cooling import newtons_law_of_cooling

def test_newtons_law_of_cooling():
    """
    Test the newtons_law_of_cooling function with a known case.
    does this for a change of 10 seconds.

    seeing whether the expected temperature is equal to the calculated temperature.

    initial_temp = 100
    enviroment_temp = 60
    h = 10.0 
    area = 0.5 
    dt = 10.0 
    c = 4186 
    m = 2.0
    """
    initial_temp = 100
    enviroment_temp = 60
    h = 10.0 
    area = 0.5 
    dt = 10.0 
    c = 4186 
    m = 2.0 

    expected_temp = initial_temp + ((h * area * (enviroment_temp - initial_temp)) * dt) / (m * c)
    calculated_temp = newtons_law_of_cooling(initial_temp, enviroment_temp, h, area, dt, c, m)
    assert expected_temp == calculated_temp
    
test_newtons_law_of_cooling()