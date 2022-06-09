import numpy as np
import scipy.constants as spy
import math



e = spy.m_e
sun_m = 1.989 * 10**30
r = 3000
a_hole = (4 * math.pi) * r**2
c = spy.c
g = spy.G
const_bhole = 6.74*10**26
m_hole = const_bhole * r
bh_x_sun = m_hole / sun_m

def relat(m):
    en= round(m*(c**2),2)
    return en

def Epg():
    f= (g*m_hole*e)/r**2
    return f
e_rp = m_hole * (c**2)
e_pg = -Epg()
black_hole ={'massa':[m_hole],
           'area':[a_hole],
           'massas_solares':[bh_x_sun]}
index = 0.00
while e_rp > 1:
    calc1 = e_rp + e_pg
    index = index + 0.01
    
print(calc1) 
print(index)      
        
        


    
