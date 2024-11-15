import models.utils as utils

def correlacion_standing(Rs, gamma_g, T,API):
    """
    Calcular el factor volumetrico del petroleo

    Parameters
    Rs: Solubilidad del gas en scf/bbl.
    gamma_g: Gravedad específica del gas en solución.
    gamma_o: Gravedad especifica del crudo en superficie.
    T: Temperatura del sistema en °R (Rankine).
    ------
    return:
    Bo = factor volumetrico del petroleo BY/BN
    ----------
    """
    gamma_o = 141.5 / (API + 131.5)

    # Ecuación de Standing para Bo
    Bo = 0.9759 + 0.000120 * ((Rs * ((gamma_g / gamma_o) ** 0.5)) + 1.25 * (T - 460)) ** 1.2

    return Bo

def correlacion_VasquezyBeggs (Rs, T, API, gamma_g, T_sep=520.0, p_sep= 114.8):
    """
    Calcular el factor volumetrico del petroleo

    Parameters
    Rs: Solubilidad del gas en scf/bbl.
    gamma_gs: Gravedad específica ajustada del gas.
    API: Gravedad API del crudo
    T: Temperatura del sistema en °R (Rankine).
    ------
    return:
    Bo = factor volumetrico del petroleo
    ----------
    """
    gamma_gs = utils.gravedad_especifica_ajustada(gamma_g, API, T_sep, p_sep)
    # Coeficientes según el rango de API
    if API <= 30:
        C1, C2, C3 = 4.677*10**-4, 1.751*10**-5, -1.811*10**-8
    else:
        C1, C2, C3 = 4.677*10**-4, 1.100*10**-5, 1.337*10**-9

    # Ecuación de Vásquez y Beggs
    Bo = 1.0 + C1*Rs + (T-520)*(API/gamma_gs)*(C2+C3*Rs)

    return Bo