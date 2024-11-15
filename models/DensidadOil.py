import math
import models.utils as utils

def correlacion_standing(Bo, gamma_o, Rs, gamma_g,Co,p):
    """
    Calcular el factor volumetrico del petroleo

    Parameters
    Bo = factor volumetrico del petroleo BY/BN
    gamma_o: Gravedad especifica del crudo en superficie.
    Rs: Solubilidad del gas en scf/bbl.
    gamma_g: Gravedad específica del gas en solución.
    Co = Compresibilidad del petroleo saturado lpc-1
    p: Presion por encima del punto de burbuja lpc

    ------
    return:
    Do = Densidad del petroleo lb/ft^3
    ----------
    """
    #Densidad del petroleo by Standing
    Do=(62.4*gamma_o+0.0136*Rs*gamma_g)/Bo

    return Do

def correlacion_VasquezyBeggs(Dob, p, pb, Rs, T, gamma_g, API, T_sep=520.0, p_sep= 114.8):
    """
    Calcular el factor volumetrico del petroleo

    Parameters
    Dob: Densidad del petroleo al punto de burbuja BY/BN
    pb: Presión de burbuja en lpc.
    p: Presion por encima del punto de burbuja lpc
    Rs: Solubilidad del gas en scf/bbl.
    gamma_gs: Gravedad específica ajustada del gas.
    API: Gravedad API del crudo
    T: Temperatura del sistema en °R (Rankine).
    ------
    return:
    Do = Densidad del petroleo lb/ft^3
    ----------
    """
    gamma_gs = utils.gravedad_especifica_ajustada(gamma_g, API, T_sep, p_sep)
    #Densidad del petroleo by Standing
    A= (10**-5)*(-1433+5*Rs+17.2*(T-460)-1180*gamma_gs+12.61*API)
    #logaritmo natutal
    log=math.exp(p/pb)-1
    #EXP
    exp= math.exp(-A*log)
    #Densidad del petroleo
    Do=Dob*exp

    return Do