import sympy as sym
'''
added another heat modelling to solids to extend our library
q - heat transfer rate (in watts)
k - stands for the thermal conductivity
A - this equates for the cross sectional area of the solid
T(x) - temperature
dT/dx - temperature gradient. rate fo change of temperature

'''

k, A, x, q= sym.symbols("k A x q")
T = sym.Function("T")(x)  

k_value = float(input("Enter thermal conductivity k (W/m . k): "))
A_value = float(input("Enter the cross-sectional area A (m^2): "))
dTdx_value = float(input("Enter temperature gradient dT/dx (K/m): "))
"""
allows the use to now input values into the equation to workout the heat transfer rate of the object there testing
"""
q_expression = -k * A * sym.diff(T, x)
q_value = q_expression.subs({k: k_value, A: A_value, sym.diff(T, x): dTdx_value})
q_value_numeric = sym.N(q_value)
print(f" The Heat transfer rate of q = {q_value_numeric} watts")
