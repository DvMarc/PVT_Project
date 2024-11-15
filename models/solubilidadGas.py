import math
import models.utils as utils

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

def lpc_to_psi(p_lpc):
    """
    Convierte la presión de lpc a psi.

    Parámetros:
    - p_lpc: Presión en lpc (libras por centímetro cuadrado).

    Retorna:
    - Presión en psi (libras por pulgada cuadrada).
    """
    if p_lpc <= 0:
        raise ValueError("La presión en lpc debe ser mayor que 0.")
    return p_lpc * 14.2233

def correlacion_vasquez_beggs(API, T, p_lpc, gamma_g, T_sep=520.0, p_sep= 114.8):
    """
    Calcula la solubilidad del gas (Rs) utilizando la correlación de Vásquez y Beggs.

    Parámetros:
    - API: Gravedad API del crudo.
    - T: Temperatura del sistema en °R (Rankine).
    - p_lpc: Presión del sistema en lpc (libras por centímetro cuadrado).
    - gamma_g: Gravedad específica del gas en condiciones estándar.
    - T_sep: Temperatura del separador en °R (Rankine). Por defecto, 520 °R.
    - p_sep: Presión del separador en psi. Por defecto, 100 psi.

    Retorna:
    - Rs: Solubilidad del gas en pies cúbicos por barril (scf/bbl).
    """
    if T <= 0:
        raise ValueError("La temperatura (T) debe ser mayor que 0.")
    if API <= 0:
        raise ValueError("El API debe ser mayor que 0.")

    # Convertir presión de lpc a psi
    p_psi = lpc_to_psi(p_lpc)

    # Ajustar la gravedad específica del gas basada en el separador
    gamma_gs = utils.gravedad_especifica_ajustada(gamma_g, API, T_sep, p_sep)

    # Coeficientes según el rango de API
    if API <= 30:
        C1, C2, C3 = 0.0362, 1.0937, 25.7240
    else:
        C1, C2, C3 = 0.0178, 1.1870, 23.9310

    # Ecuación de Vásquez y Beggs
    Rs = C1 * gamma_gs * (p_psi ** C2) * math.exp(C3 * (API / T))

    if Rs < 0:
        raise ValueError("El valor calculado de Rs es negativo. Verifique los parámetros de entrada.")
    return Rs

