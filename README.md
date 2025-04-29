# temperature change

A pthon library for studying (modeling) the temperature 
change of different objects in different conditions

## tutorial

We measure or record data of a specific object in a certain enviorment.

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

## Reference
