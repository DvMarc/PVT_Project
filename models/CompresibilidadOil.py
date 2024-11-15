import models.utils as utils

def correlacion_VasquezyBeggs(Rs, T, gamma_gs, API, p):
    """
    Calcular el factor volumetrico del petroleo

    Parameters
    Rs: Solubilidad del gas en scf/bbl.
    T: Temperatura del sistema en °R (Rankine).
    gamma_gs: Gravedad específica ajustada del gas.
    API: Gravedad API del crudo.
    p: Presion por encima del punto de burbuja lpc
    ------
    return:
    Co = Compresibilidad del petroleo saturado lpc-1
    ----------
    """

    #Compresibilidad de petroleo saturado
    Co = (-1433+(5*Rs)+17.2*(T-460)-(1180*gamma_gs)+12.61*API)/((10**5)*p)

    return Co

def correlacion_PetroskyyFarshd(Rs, gamma_g, API, T, p):
    """
    Calcular el factor volumetrico del petroleo

    Parameters
    Rs: Solubilidad del gas en scf/bbl.
    T: Temperatura del sistema en °R (Rankine).
    gamma_gs: Gravedad específica ajustada del gas.
    API: Gravedad API del crudo.
    p: Presion por encima del punto de burbuja lpc
    ------
    return:
    Co = Compresibilidad del petroleo saturado lpc-1
    ----------
    """

    Rs=Rs**0.69357
    gamma_g=gamma_g**0.1885
    API=API**0.3272
    T=(T-460)**0.6729
    p=p**-0.5906
    #Compresibilidad del petroleo subsaturado
    Co = (1.705*10**-7)*Rs*gamma_g*API*T*p

    return Co

