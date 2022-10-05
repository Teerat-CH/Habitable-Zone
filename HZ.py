import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

st.write("""

## Habitable zone
**Star's mass** : Star mass has a direct relationship with the energy it emits per unit of time, therefore affecting planet temperature.

**Albedo** : Albedo number refers to how reflective a planet is : 1 is a perfect reflector whereas 0 is a perfect absorber.

**Circle green band** represents the Habitable zone (Temperature range from 0-100 Celsius)

For finer adjustment, both star's mass and albedo were multiply by the factor of 10 and 100 respectively.

-----------------------------------------------------------------------------------------

""")
 
#Constant list
pi = 3.1415926
SBC = 5.67*(10**-8) #Stefan-Boltzmann Constant
M = st.slider('Star Mass', 1, 100)
L = (M/10)**3.5

#adjustable constants
temp1 = 0 #0 celcius
temp2 = 100 #100 celcius
AB = st.slider('Albedo', 1, 100)
albedo = AB/100

INB = (((((1-albedo)*L)/(16*pi*SBC))**(1/2))/((temp1+273.5)**2))*130
OUB = (((((1-albedo)*L)/(16*pi*SBC))**(1/2))/((temp2+273.5)**2))*130

circle1 = plt.Circle((0, 0), INB, color='g',alpha=0.5, ls = '')
circle2 = plt.Circle((0, 0), OUB, color='w',alpha=1, ls = '')
circle3 = plt.Circle((0, 0), 1.2, color='r',alpha=0.8, ls = '')

fig, ax = plt.subplots()
ax.set_xlim((-50, 50))
ax.set_ylim((-50, 50))
ax.add_patch(circle1)
ax.add_patch(circle2)
ax.add_patch(circle3)
ax.set_aspect('equal', adjustable='box')

 
plt.grid(color='grey',linestyle=':',linewidth=0.3)
plt.ylabel("")
plt.xlabel("")
st.pyplot(fig)