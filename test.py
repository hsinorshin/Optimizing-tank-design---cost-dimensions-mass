from .tank_opt import buckle,tank_dimension,tank_mass,tank_cost
import numpy as np 

#using fuel 

r=np.linspace(0.05,0.15,100) #array of inner radius 
p_int=3.5e+6 #design pressure 
p_ext=1e+5 #assume atmospheric pressure of 1 bar 
v=0.333 # poisson ratio of Aluminium 7075
E=6.79e10 #youngs modulus for Al7075 

def run(r):
    list=[]
    for r in r:

        result=tank_dimension(fuel,R=0.15,r=r,p_ext=p_ext,p_int=p_int,v=v)
        list.append((r,result))

    print(list)

run(r)
