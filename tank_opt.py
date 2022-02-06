import math 
import os
os.system('cls' if os.name == 'nt' else 'clear')
import json
with open('tanks_specifications.json') as f:
   data = json.load(f)

import numpy as np
fuel=data['fuel']
oxidiser=data['oxidiser']
material=data['material']
other=data['other']



def buckle(type, p_ext, p_int, g=9.81,t, l,R=0.15,v,E):
   '''block for tank buckling '''

   #density of propellent 
   rho=type['density']
   #k_s is buckling coefficient 
   k_s = 0.85((2*l**2/R*t)*(1-v**2))**0.75
   #Buckling strength calculated using Baker's buckling criteria 
   p_cr= (math.pi**2 *k_s*E)/(12(1-v**2))*(t/L)**2 ##what is L , is it l or l+2R?
   #A for cylinder with hemispherical ends 
   #NOT SURE WHAT IS H IN DOCUMENT PLS CHECK
   A = ((math.pi*(2*r)**2)/4) + (math.pi*2*r*l**2) #replaced H with l 
   hoop_stress= (0.5(p_int*2*r)+(rho*g*l))/t
   axial_stress =((0.5*p_int*2*r) + (rho*g*l))/t - p_int*A


   if hoop_stress>p_cr or axial_stress>p_cr:
       return False
    
   else:
       return True 


def tank_dimension(type,p,T,R,r ):
    '''block of function to determine R-r depending on stress/buckling analysis , where R is a constant'''
    
    #assume ideal gas law PV=nR_gT , validity should be checked
    n=type['n']
    R_g=8.31
    P=p
    V_int = (n*R_g*T)/P
    #length of tank based on r
    l= (V_int- math.pi*r**2)/(2*math.pi*r)
    #thickness of tank = R-r 
    t=R-r

    if buckle(fuel,p_ext,p_int,t,l,R,v)==True:
        dimensions={'Tank thickness':t,'tank length':l,'internal radius':r,'external radius':R}
        return dimensions
    else:
        return ('a different value of r should be chosen')


def tank_mass(type,tank_dimensions(type,p,T,R,r)):
    '''tank mass block''' 

    t=dimensions['Tank thickness']
    l=dimensions['tank length']
    r=dimensions['internal radius']
    R=dimensions['external radius']
    density=type['density']

    #Volume of internal tank dimensions = 2*pi*r*l + pi*r**2
    vol_int = 2*math.pi*r*l + math.pi*r**2 
    #Volume of external = 2*pi*R*l + pi*R*2
    vol_ext=2*math.pi*R*l + math.pi*R**2
    tank_mass=density*(vol_ext-vol_int)

    return tank_mass 


def tank_cost (type,limit,tank_mass(type,tank_dimensions(type,p,T,R,r))):
    '''cost block'''
    cost_per_unit_mass=type['cost']
    cost=cost_per_unit_mass*tank_mass
    if cost>limit:
        'You have exceeded your cost limit'
        #to edit such that it is a recurring function 
    else:
        'no broke bois'

    





    

    


