# temperature change

A python library for studying (modeling) the temperature 
change and conductivity of different objects in different conditions

## tutorial


```python
>>> from Newtons import rate_of_change, calculate_k, temperature_at_time
>>> from TempConverter import temp_converter
>>> from ConvertNewtons import conv_temp_at_time, conv_rate_of_change
>>> from GraphNewtons import graphing_newtons
>>> from HypothesisTestingNewtons import hypothesis_test
>>> ex_initial_temp = 100
>>> ex_temp_final = 70
>>> ex_temp_env = 60
>>> ex_dt = 10
>>> ex_k = 0.14
>>> ex_input_scale = "C"
>>> ex_output_scale = "K"
>>> ex_temp_range = 100
>>> ex_real_world_value = 75

```
Now i can use the above to calculate the rate of change, the cooling constant(k) and the temperature at some time. 

```python
>>> rate_of_change(initial_temp = ex_initial_temp, temp_final=ex_temp_final, dt=ex_dt)
3.0
>>> calculate_k(initial_temp= ex_initial_temp, temp_final=ex_temp_final, temp_env=ex_temp_env, dt=ex_dt)
0.14
>>> temperature_at_time(initial_temp=ex_initial_temp, temp_env=ex_temp_env, dt=ex_dt, k=ex_k)
69.86

```
I can also convert between Farenheight, Celcuis and Kelvin 

```python 
>>> temp_converter(input_scale = ex_input_scale, output_scale = ex_output_scale, temp_env=ex_temp_env, initial_temp=ex_initial_temp, temp_final=ex_temp_final)
(333.15, 373.15, 343.15)

```
I can also directly calculate the calculate the rate of change, the cooling constant(k) and the temperature at some time, with converted temperature scales

``` python
>>> conv_temp_at_time(input_scale = ex_input_scale, output_scale = ex_output_scale, initial_temp = ex_initial_temp, temp_final = ex_temp_final ,temp_env = ex_temp_env, dt = ex_dt)
343.01
>>> rate_of_change(initial_temp = ex_initial_temp, temp_final = ex_temp_final ,dt = ex_dt)
3.0

```
A graph can be shown to display the rate of temperature change with time
```python
>>> graphing_newtons(input_scale = ex_input_scale ,initial_temp = ex_initial_temp, temp_final = ex_temp_final, temp_env = ex_temp_env , dt = ex_dt, temp_range = ex_temp_range)

```
a hypothesis can be run to compare the modeled tempature at some time to the real-world value

```python
>>> hypothesis_test(initial_temp = ex_initial_temp, temp_final = ex_temp_final, temp_env = ex_temp_env, dt = ex_dt, real_world_value = ex_real_world_value)
'Reject null hypothesis: Modeled value is outside 5% of real-world value. Modeled value:[69.86] Bounded by:[71.25,78.75].'

```

You can also use the coded fourier model to measure the heat transfer rate of an object 

```python
>>> from fourier_law import fourier_law
>>> ex_k = 50
>>> ex_A = 100
>>> ex_dT_dx = 3
>>> fourier_law(k= ex_k, A = ex_A, dT_dx = ex_dT_dx)
-15000

```

I can also make a hypothesis test comparing the model against real world data and plot the rate of heat transfer

```python
>>> from Hypothesis_test_fourier import run_hypothesis_test
>>> from plot_fourier import fourier_plot
>>> run_hypothesis_test(k = 50, A = 1000, dT_dx = 1, real_value = 1000, sig=0.05)
'Model rejected at 5.0% significance level. Modeled: -50000.00 W Acceptable range: [950.00, 1050.00] '
>>> fourier_plot(k_value=50, A_value=1000)

```
### how to guide

To compute the rate of change, the cooling constant, and temperature at some time

```python
>>> import Newtons
>>> import TempConverter
>>> import ConvertNewtons
>>> import GraphNewtons
>>> import HypothesisTestingNewtons
>>> Newtons.rate_of_change(initial_temp = 100, temp_final=70, dt=10)
3.0
>>> Newtons.calculate_k(initial_temp= 100, temp_final=70, temp_env=60, dt=10)
0.14
>>> Newtons.temperature_at_time(initial_temp = 100, temp_env = 60, dt = 10, k= 0.14)
69.86

```
Convert the enviorment temperature, the initial temperature, and the final temperature between any: "C","K" and "F"
```python
>>> TempConverter.temp_converter(input_scale = "C", output_scale = "K", temp_env=60, initial_temp=100, temp_final=70)
(333.15, 373.15, 343.15)

```
Directly calculate the temperature at a given time and convert the temperature
```python
>>> ConvertNewtons.conv_temp_at_time(input_scale = "C", output_scale = "K", initial_temp = 100, temp_final = 70 ,temp_env = 60, dt = 10)
343.01

```
Display a graph modeling newtons law of cooling
```python
>>> GraphNewtons.graphing_newtons(input_scale = "C" ,initial_temp = 100, temp_final = 70, temp_env = 60 , dt = 10, temp_range = 100)

```
A hypothsis test to see whether the modeled prediction is close to the real world value
```python
>>> HypothesisTestingNewtons.hypothesis_test(initial_temp = 100, temp_final = 70, temp_env = 60, dt = 10, real_world_value = 75)
'Reject null hypothesis: Modeled value is outside 5% of real-world value. Modeled value:[69.86] Bounded by:[71.25,78.75].'

```
To compute the fourier model of heat conduction after given '-k', 'A', 'dT_dx'

```python
>>> import math
>>> from fourier_law import fourier_law
>>> fourier_law(k = 50, A = 100, dT_dx = 3)
-15000

```
We can also plot a graph 

```python
>>> from plot_fourier import fourier_plot
>>> fourier_plot(k_value=50, A_value=1000)

```
In our fourier_law library use fourier_hypothesis_test

```python 
>>> from Hypothesis_test_fourier import run_hypothesis_test
>>> run_hypothesis_test(k = 50, A = 1000, dT_dx = 1, real_value = 1000, sig=0.05) 
'Model rejected at 5.0% significance level. Modeled: -50000.00 W Acceptable range: [950.00, 1050.00] '

```

## Discussion
This code allows you to take minimal real world values and calculate a wealth of information from it.

By using newtons law of cooling you can model the temperature at any time of some object (eg. a mug of hot water), just by measuring two temperatures, the time difference between them and the temperature of the enviorment.

These values are then used to calculate; first the rate of temperature change of the object, The cooling constant of that object and the temperature of the object at any time. 
This is done by using newtons law of cooling.

The temperatures can be changed between Celcius, Kelvin and Farenheight for just the initial temperature, the final temperature and the enviorment temperature. Or you can directly calculate the temperature of the object at some time with a different temperature scale.

A graph can then be modeled to show this and a hypothsis test can be drawm to see whether the model is close to a real life value. 


### Newton's cooling law
Sir Isaac Newton introduced his cooling law in the 1700's, which is based on purely empirical measurements, due to curiosity over how air and water cools and warms objects replacing the dominant theory at the time: 'caloric theory' which hypothesised heat was a substance that was fluid-like in nature. 

Newtons Law of Cooling is defined as the rate at which heat is lost from a body being directly proportional to the temperature difference between a bodyand its surroundings. This is given by the equation: 

$\frac{dy}{dx} = -k(T-T_a)$

### Fouriers Law of Heat Conduction for Solid Objects:
This is the rate at which heat transfers through an object is directly proportional to the negative gradient of temperature and the cross-sectional area through which the heat flows and is said to be inversely proportional to the materials thickness. 

Joseph Fourier of France put together his equation at the beginning of the 19th century who's heat diffusion model later went on to be used by others when describing ther dynamic physical systems: 

$\frac{dQ}{dt} = -KA (\frac{dT}{dx})$ 



## References

### list of functionality

A list of functionality in this library is:

- 'rate_of_change'
- 'calculate_k'
- 'temperature_at_time'
- 'temp_converter'
- 'conv_temp_at_time'
- 'graphing_newtons'

A list of functionionallity in this fourier model library is:
'fourier_law'

### Bibliography
Frédéric Martin (2009-2025) Newton’s Law Of Cooling, Quadco’ Engineering. 
Available at: https://www.quadco.engineering/en/know-how/newtons-law-of-cooling.htm#:~:text=Historical%20background,convective%20and%20conductive%20heat%20transfer. (Accessed: 2 May 2025) 

Lily Hulatt (2025) Newton’s Law Of Cooling, Study Smarter.
Available at: https://knowledge.carolina.com/discipline/interdisciplinary/math/newtons-law-of-cooling/ (Accessed: 2 May 2025) 

T.N.Narasimhan, Reviews of Geophysics Volume 37, Issue 1, The American Geophysical Union, 1999 

ALLEN Career Institute, 2022 Fourier's Law of Heat Conduction, ALLEN. Available at: https://allen.in/jee/physics/fouriers-law-of-heat-conduction (Accessed: 2 May 2025) 

### Testing the Software
to test the code:

```
$ python Test_ConvertNewtons.py
$ python Test_HypothesisTestingNewtons.py
$ python Test_Newtons.py
$ python Test_TempConverter.py
$ python Test_Fourier.py
```
To test the documentation:

```
$ python -m doctest README.md
```

### Creators
Emerson Earl, Kirsten Lonsdale, James Baum and Harry Addington


