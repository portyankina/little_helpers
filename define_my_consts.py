# ---- define some conversions ---
# ---- use: ----
# from define_my_consts import mb2Pa
import numpy as np

mb2Pa = 100.0				# convert mb to Pa
Pa2mb = 0.01				# and back
cal2J = 4.18400             # convert cal to J
Angstr2m = 1e-10            # Angstrom to m
# ---- define my constants ----
avogadro  = 6.022142e23		# 
boltzmann = 1.380650e-23 	# J/K
R = 8.3144621 				# gas constant in J/mol/K
GravConst = 6.67e-11        # in m3/kg/s2

mu_CO2 = 44.010e-3          # molar mass of CO2 in kg/mol
H_CO2 = 635.0e3 		    # latent heat of sublimation of CO2 in J/kg 574
sigma = 5.6704e-8 	        # Stefan-Boltzmann constant in kg s^-3  K^-4
Aice = 0.6
epsilon = 1 - Aice          # emissivity of CO2???

kings_factor_CO2 = 1.145 #  1.1364+25.3e-12 cm2

gMars =3.711 # in m/s2
Ns_CO2_at_15C = 2.546899e19    # number density of CO2 gas used for scattering cross-section calculations; in molecules per cm3

B = 1e-2
d1 =100.0
d2 =3148.0
d3 =23.102
Cp_Co2gas_15 = 2.534           # CO2 gas specific heat in J/(mol K) at 15.52 K
Cp_Co2gas_146 = 147.11         # CO2 gas specific heat in J/(mol K) at 146.48 K
Cp_Co2gas_189 = 54.55          # CO2 gas specific heat in J/(mol K) at 189.78 K 
s_reg = 0.4*4.184              # regolith specific heat in J/g/K 

Cp_Co2ice = 349.0 + 4.8*160.   # in  the specific heat of CO2 ice (349 + 4.8T in J kg-1 K-1, with 73 K < T < 200 K, from Washburn 1948)

L_CO2 = 5.74e5                  # CO2 latent heat of sublimation 5.9e5 in J/kg from Pilorget et al, 2011
                               # OR: 709 in J/g at T=175K; 635 J/g in my thesis; 574 kJ/kg at wiki, 
L_CO2_175 = 26408              # CO2 ice latent heat 26408 J/mol Azreg-Ainou, M., 2005. Low-temperature Data for Carbon Dioxide. Monatshefte fuer Chemie - Chemical Monthly, 136(12), pp.2017-2027.; 
s_CO2 = 11.27*cal2J                  # CO2 heat capacity in cal/K/mol at T = 146 K by Giauque, W.F. & Egan, C.J., 1936. Carbon Dioxide. The heat capacity and vapor pressure of the solid. The heat of sublimation. Thermodynamic and Spectroscopic values of antripy., pp.1-10.;  0.205*4.184 in J/g/K was in my thesis

A_ice = 0.7
A_reg = 0.3

ro_CO2 = 1.56e3             # CO2 ice density in kg/m3
ro_reg = 3.0e3              # regolith density in kg/m3

beta = 0.002                # drag force  Paterson (1994)

# Enceladus
M_Enc = 1.1e20 # mass Enceladus in kg; 1.08022e20 kg
r_Enc = 2.52e5 # radius Enceladus in m
Enc_axes = np.array([256.6, 251.4, 248.3]) # ellipsoid semi-axes in km
GM_Enc = GravConst*M_Enc

# orbit 
D_Sat_Enc = 2.38e8 # semimajor axis of Enceladus orbit 237948 km = 2.38e5 km = 2.38e8 m = 2.38e10 cm
omega = 2*np.pi/1.37/24/3600. # angular velocity of Enceladus on the orbit, in rad/s; Period_Enc = 1.370218 d 
omega2 = omega**2
omega2vec =[omega**2, omega**2, 0] 
omega_vec = [0, 0, omega]

# water gas
T_top = 30
m_H2O = 1.67e-27*18  # atomic mass unit 1.66053892e-27 kg * H2O 
T0 = 180
n0 = 1e17		        # assumed surface number density 1e11 in 1/cm3 = 1e17 1/m3 or 1e10 in 1/cm3 = 1e17 1/m3
x_sec = 1e-22	        # collisional cross section of H2O in m2 = 1e-15 cm2 Fillion (2004), High resolution photoabsorption and                          # photofragment fluorescence spectroscopy of water between 10.9 and 12 eV, J. Chem. Phys., 120
dl = 1./(n0*x_sec)

# Saturn's gravity field
M_Sat = 568.3e24 # kg or 5.7e29 g
GM_Sat = GravConst * M_Sat
g_Sat0 = GM_Sat/(D_Sat_Enc**2)

# initial velocity distribution
sigma0 = np.sqrt(boltzmann*T0/m_H2O)	# sigma to be used in the Boltzmann distribution
V_th0 = np.sqrt(2*boltzmann/m_H2O*T0) # thermal velocity


r2_Enc = r_Enc**2	# surface of Enceladus
r2_away = 25*r2_Enc	# outer boundary
r_away = 10*r_Enc
nz02 = n0*r2_away
T_slope = (T0 - T_top)/(np.sqrt(r2_away)-r_Enc)
T_h = (np.sqrt(r2_away)-r_Enc)/np.log(T0/T_top)

#Vz0 = 300			                    # initial wind velocity 300 m/s
#r_expansion = 2e6*V_th0/(Vz0 + V_th0)    
#c = 1.5e16/r_expansion/2	# density derived from an estimate of the plume size

escape_Larry = 230/m_H2O # molecules per s ?
escape_Larry_jets = 50/m_H2O # 50 kg/s 
