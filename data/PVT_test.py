def presion_burbuja_standing(Rs, T, API):
    """
    Calcula la presión de burbuja (pb) utilizando la correlación de Standing.

    Parámetros:
    - Rs: Solubilidad del gas en scf/bbl.
    - T: Temperatura del sistema en °R (Rankine).
    - API: Gravedad API del crudo.

    Retorna:
    - pb: Presión de burbuja en lpc.
    """
    # Cálculo del término 'a' en la fórmula
    a = 0.00091 * (T - 460) - 0.0125 * API

    # Ecuación de Standing
    pb = 18.2 * ((Rs / (10 ** a)) ** 0.83) - 1.4
    return pb


def presion_burbuja_vasquez_beggs(Rs, T, gamma_gs, API):
    """
    Calcula la presión de burbuja (pb) utilizando la correlación de Vásquez y Beggs.

    Parámetros:
    - Rs: Solubilidad del gas en scf/bbl.
    - T: Temperatura del sistema en °R (Rankine).
    - gamma_gs: Gravedad específica ajustada del gas.
    - API: Gravedad API del crudo.

    Retorna:
    - pb: Presión de burbuja en lpc.
    """
    # Coeficientes según el rango de API
    if API <= 30:
        C1, C2, C3 = 27.624, 0.914328, 11.172
    else:
        C1, C2, C3 = 56.18, 0.84246, 10.393

    # Cálculo del término 'a'
    a = -C3 * (API / T)

    # Ecuación de Vásquez y Beggs
    pb = C1 * (Rs / gamma_gs) ** C2 * (10 ** a)
    return pb