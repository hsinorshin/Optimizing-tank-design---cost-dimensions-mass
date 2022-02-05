import math 

#Defining parameters
t =  #tank thickness  
P =  #internal pressure 
D=    #tank diameter
Rho = #density of fluid in tank 
g = 9.81
h = #tank height
l= # what is l 
A = ((math.pi*D**2)/4) + (math.pi*D*l*h) # for a cylinder with hemispherical ends 


hoop_stress= (0.5(P*D)+(Rho*g*h))/t
axial_stress =((0.5*P*D) + (Rho*g*h))/t - P(A)

#buckling coefficient 

E = #youngs modulus
v = #poissons ratio
L= #length of ..obj 
k_s = 0.85((2*L**2/D*t)*(1-v**2))**0.75
def P_cr(k_s,E,v):
#Buckling strength calculated using Baker's buckling criteria 
    p_cr= (math.pi**2 *k_s*E)/(12(1-v**2))*(t/L)**2