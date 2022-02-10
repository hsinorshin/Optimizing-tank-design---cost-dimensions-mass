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



def buckle(type, t, l,r, p_ext, p_int,v, E, g=9.81 ,R=0.15 ):
   '''block for tank buckling '''

    
   #density of propellent 
   rho=type['density']
   #k_s is buckling coefficient 
   k_s = 0.85((2*l**2/R*t)*(1-v**2))**0.75

   #Buckling strength calculated using Baker's buckling criteria 

   p_cr= (math.pi**2 *k_s*E)/(12(1-v**2))*(t/L)**2 # we only consider the the buckling longitudinally for now
   
   #NOT SURE WHAT IS H IN DOCUMENT PLS CHECK - H is the length here (assuming uniform pressure distribution inside)
  
   A = ((math.pi*(2*r)**2)/4) + (math.pi*2*r*l**2) #replaced H with l 
   hoop_stress= (0.5(p_int*2*r)+(rho*g*l))/t
   axial_stress =((0.5*p_int*2*r) + (rho*g*l))/t - p_int*A

   re_factor =  p_int/E * (2*R/(2*t))**2 # recurring factor in the delta p_cr equation
   del_p_cr = 0.051 * np.log(re_factor) - 0.098*(re_factor) + 0.273 # delta p_cr calculated using bruhn's data - high corelation equation

   p_final = p_cr + del_p_cr # final buckling load

   if hoop_stress>p_final or axial_stress>p_final:
       return False
    
   else:
       return True 


def tank_dimension(type,R,r,p_ext, p_int,v):
    '''block of function to determine R-r depending on stress/buckling analysis , where R is a constant'''
    
    #Volume of propellent
    V_prop=type["liq_volume"]
    #10% ullage 
    V_int=(1.1*V_prop)
    #length of tank based on r
    l= (V_int- math.pi*r**2)/(2*math.pi*r)
    #thickness of tank = R-r 
    t=R-r

    if buckle(fuel,p_ext,p_int,t,l,R,v)==True:
        dimensions={'Tank thickness':t,'tank length':l,'internal radius':r,'external radius':R}
        return dimensions

    else:
        # test w array 
        return ('a different value of r should be chosen')


def tank_mass(type,tank_dimensions): # python will identify tank_dimensions as a function when we input the parameter
    '''tank mass block''' 

    t=tank_dimensions['Tank thickness']
    l=tank_dimensions['tank length']
    r=tank_dimensions['internal radius']
    R=tank_dimensions['external radius']
    density=type['density']

    #Volume of internal tank dimensions = 2*pi*r*l + pi*r**2
    vol_int = 2*math.pi*r*l + math.pi*r**2 
    #Volume of external = 2*pi*R*l + pi*R*2
    vol_ext=2*math.pi*R*l + math.pi*R**2
    tank_mass=density*(vol_ext-vol_int)

    return tank_mass 


def tank_cost(type,limit,tank_mass): # python will identify tank_mass as a function when we input the parameter
    '''cost block'''
    cost_per_unit_mass=type['cost']
    cost=cost_per_unit_mass*tank_mass
    if cost>limit:
        'You have exceeded your cost limit'
        #to edit such that it is a recurring function 
    else:
        'no broke bois'

    





    

    


