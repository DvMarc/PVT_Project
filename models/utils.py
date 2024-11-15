import math

def gravedad_especifica_ajustada(gamma_g, API, T_sep, p_sep):
    """
    Ajusta la gravedad específica del gas (gamma_gs) basada en las condiciones del separador.

    Parámetros:
    - gamma_g: Gravedad específica del gas en condiciones estándar.
    - API: Gravedad API del crudo.
    - T_sep: Temperatura del separador en °R (Rankine).
    - p_sep: Presión del separador en psi.

    Retorna:
    - gamma_gs: Gravedad específica ajustada en condiciones del separador.
    """
    if p_sep <= 114.7:
        raise ValueError("La presión del separador (p_sep) debe ser mayor que 114.7 psi.")
    if T_sep <= 0:
        raise ValueError("La temperatura del separador (T_sep) debe ser mayor que 0.")

    gamma_gs = gamma_g * (1 + 5.912 * (10 ** -5) * API * (T_sep - 460) * math.log(p_sep / 114.7))
    return gamma_gs
