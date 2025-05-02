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
Sir Isaac Newton introduced his cooling law which is based on purely empirical measurements in the 1700's due to curiosity over how air and water cools and warms objects replacing the dominant theory at the time: 'caloric theory' which hypothesised heat was a substance that was fluid-like in nature.

Newtons Law of Cooling is defined as the rate at which heat is lost from a body being directly proportional to the temperature difference between a body and its surroundings and is given by the equation:

$\frac{dy}{dx} = -k(T-T_a)$




## References
Frédéric Martin (2009-2025) Newton’s Law Of Cooling, Quadco’ Engineering. 
Available at: https://www.quadco.engineering/en/know-how/newtons-law-of-cooling.htm#:~:text=Historical%20background,convective%20and%20conductive%20heat%20transfer. (Accessed: 2 May 2025) 

Lily Hulatt (2025) Newton’s Law Of Cooling, Study Smarter.
Available at: https://knowledge.carolina.com/discipline/interdisciplinary/math/newtons-law-of-cooling/ (Accessed: 2 May 2025) 
