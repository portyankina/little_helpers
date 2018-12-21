from __future__ import print_function
from numpy import arange, power, genfromtxt
from little_helpers.define_my_consts import (
    sigma,
    L_CO2,
    L_CO2_175,
    s_CO2,
    mu_CO2,
    R,
    beta,
    ro_CO2,
    epsilon,
    Cp_Co2ice,
)


def CO2_phase_diagram(Trange):
    Temp = Trange[0] + arange(Trange[-1] - Trange[0] + 1)
    # --- CO2 phase diagram for T<-56.4C ---
    Pres = 0.01316 * power(
        10.0,
        -1354.210 / Temp
        + 8.69903
        + 0.001_588 * Temp
        - (4.5107 * power(10.0, -6)) * Temp * Temp,
    )  # find out where this is from
    return Temp, Pres * 1.01325 * 1000.0  # temperaturer is in K, pressure is in mb


def CO2_phase_diagram_one(T):
    # --- CO2 phase diagram for T<-56.4C ---
    Pres = 0.01316 * power(
        10.0,
        -1354.210 / T + 8.69903 + 0.001_588 * T - (4.5107 * power(10.0, -6)) * T * T,
    )  # find out where this is from
    return Pres * 1.01325 * 1000.0  # pressure is in mb


def CO2_eq_T(P_eq):  # give pressure in Pa
    T, P = CO2_phase_diagram([10, 215])
    from numpy import interp

    T_eq = interp(P_eq / 100.0, P, T)
    return T_eq


def CO2_eq_T_Konrad(Pressure):  # give pressure in Pa
    from math import log

    d1 = 100.0
    d2 = 3148.0
    d3 = 23.102
    Tice = d2 / (d3 - log(Pressure / d1))
    return Tice


def CO2_sublime_mass(Energy, dT):  # energy per unit area per time, say in W/m2
    m_CO2 = Energy / (s_CO2 * dT + L_CO2_175) * mu_CO2  # in kg/m2/time
    # dz_per_m2 = m_CO2/()
    return m_CO2  # in kg/m2/time slot


def CO2_condence_mass(epsilonCO2, Tsurf):
    m_CO2 = sigma * epsilonCO2 * Tsurf ** 4 / L_CO2  # in kg/m2/time
    return m_CO2  # in kg/m2/time slot


def CO2_condence_flux_Konrad(wind_speed, Tsurf, Patm):
    Peq = CO2_phase_diagram_one(Tsurf) * 100.0
    print(f"Eq. vap pressure: {Peq}, Tsurf = {Tsurf}, Patm = {Patm}")
    CO2_flux = wind_speed * beta * (mu_CO2 / R / Tsurf) * (Patm - Peq)
    return CO2_flux  # in kg/m2/s


def Cp_CO2(T):
    if T < 73 or T > 200:
        print("This Cp is out of its T-range for CO2 ice!")
    Cp = 349.0 + 4.8 * T  # from Washburn 1948
    return Cp  # in J kg-1 K-1


def CO2_flux_cond(Tsurf, P):
    Tsub = CO2_eq_T(P)
    dT = Tsurf - Tsub
    dm = dT / L_CO2 * Cp_CO2(Tsub)
    return dm

