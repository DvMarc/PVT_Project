import math

def correlacion_standing(p, T, gamma_g, API):
    """
    Calcula la solubilidad del gas (Rs) utilizando la correlación de Standing.

    Parámetros:
    - p: Presión del sistema en lpc (libra por pulgada cuadrada).
    - T: Temperatura del sistema en °R (Rankine).
    - gamma_g: Gravedad específica del gas en solución.
    - API: Gravedad API del crudo.

    Retorna:
    - Rs: Solubilidad del gas en pies cúbicos por barril (scf/bbl).
    """
    # Constantes de la fórmula
    x = 0.0125 * API - 0.000091 * (T - 460)

    # Ecuación de Standing
    Rs = gamma_g * ((p / 18.2) + 1.4) * (10 ** x) ** 1.2048

    return Rs

def gravedad_especifica_ajustada(gamma_g, API, T_sep, p_sep):
    """
    Ajusta la gravedad específica del gas (gamma_gs) basada en las condiciones del separador.

    Parámetros:
    - gamma_g: Gravedad específica del gas.
    - API: Gravedad API del crudo.
    - T_sep: Temperatura del separador en °R.
    - p_sep: Presión del separador en lpc.

    Retorna:
    - gamma_gs: Gravedad específica ajustada.
    """
    gamma_gs = gamma_g * (1 + 5.912 * (10 ** -5) * (API) * (T_sep - 460) * math.log(p_sep / 114.7))
    return gamma_gs

def correlacion_vasquez_beggs(API, T, p, gamma_gs):
    """
    Calcula la solubilidad del gas (Rs) utilizando la correlación de Vásquez y Beggs.

    Parámetros:
    - API: Gravedad API del crudo.
    - T: Temperatura del sistema en °R (Rankine).
    - p: Presión del sistema en lpc (libra por pulgada cuadrada).
    - gamma_gs: Gravedad específica ajustada del gas.

    Retorna:
    - Rs: Solubilidad del gas en pies cúbicos por barril (scf/bbl).
    """
    # Coeficientes según el rango de API
    if API <= 30:
        C1, C2, C3 = 0.0362, 1.0937, 25.7240
    else:
        C1, C2, C3 = 0.0178, 1.1870, 23.9310

    # Ecuación de Vásquez y Beggs
    Rs = C1 * gamma_gs * (p ** C2) * math.exp(C3 * (API / T))
    return Rs