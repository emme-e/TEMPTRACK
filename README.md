# temperature change

A python library for studying (modeling) the temperature 
change of different objects in different conditions

## tutorial

We measure or record data of a specific object in a certain environment.

- 1st measure data of the object
- 1.b can have two cases: a solid object and a container with water
- 2nd change some parameters (ie. temp enviroment, initial temp of the object)
- 3rd model (prediction) what the temperature change is (ie. a graph, and measuring specific values)
- 4th record the real life version of the prediction
- 5th compare to our model (ie. have a null and alternative hypothsis to see if we should accept our model).
  
        - we can use newtons law of cooling for an object containing water.
        - Fourier’s Law of Heat Conduction for solid objects

'''python
>>> import Newtons_law_of_cooling
>>> initial_temp=80,
        enviroment_temp=25,
        h=10,
        area=0.5,
        dt=60,
        c=4186,
        m=1
'''
Now i can use the above to calculate the new temperature after some time

'''python
>>>newtons_law_of_cooling(initial_temp, enviroment_temp, h, area, dt, c, m)


...

## how to guide

## Discussion
### Newton's cooling law
Sir Isaac Newton introduced his cooling law in the 1700's, which is based on purely empirical measurements, due to curiosity over how air and water cools and warms objects replacing the dominant theory at the time: 'caloric theory' which hypothesised heat was a substance that was fluid-like in nature. 

Newtons Law of Cooling is defined as the rate at which heat is lost from a body being directly proportional to the temperature difference between a bodyand its surroundings. This is given by the equation: 

$\frac{dy}{dx} = -k(T-T_a)$

### Fouriers Law of Heat Conduction for Solid Objects:
This is the rate at which heat transfers through an object is directly proportional to the negative gradient of temperature and the cross-sectional area through which the heat flows and is said to be inversely proportional to the materials thickness. 

Joseph Fourier of France put together his equation at the beginning of the 19th century who's heat diffusion model later went on to be used by others when describing ther dynamic physical systems: 

$\frac{dQ}{dt} = -KA (\frac{dT}{dx})$ 




## References
Frédéric Martin (2009-2025) Newton’s Law Of Cooling, Quadco’ Engineering. 
Available at: https://www.quadco.engineering/en/know-how/newtons-law-of-cooling.htm#:~:text=Historical%20background,convective%20and%20conductive%20heat%20transfer. (Accessed: 2 May 2025) 

Lily Hulatt (2025) Newton’s Law Of Cooling, Study Smarter.
Available at: https://knowledge.carolina.com/discipline/interdisciplinary/math/newtons-law-of-cooling/ (Accessed: 2 May 2025) 

T.N.Narasimhan, Reviews of Geophysics Volume 37, Issue 1, The American Geophysical Union, 1999 

ALLEN Career Institute, 2022 Fourier's Law of Heat Conduction, ALLEN. Available at: https://allen.in/jee/physics/fouriers-law-of-heat-conduction (Accessed: 2 May 2025) 
