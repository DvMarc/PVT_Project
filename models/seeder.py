import pandas as pd
import numpy as np
from scipy.stats import norm, lognorm, uniform

def generate_data_with_scipy(num_samples=100, seed=None):
    """
    Genera datos sintéticos usando distribuciones de scipy.stats
    para Rs, T, API y gamma_gs.

    Parámetros:
    - num_samples: Número de muestras a generar.
    - seed: Semilla para asegurar reproducibilidad.

    Retorna:
    - Un DataFrame con datos generados aleatoriamente.
    """
    if seed:
        np.random.seed(seed)

    data = {
        "Rs": lognorm.rvs(s=0.5, scale=300, size=num_samples, random_state=seed),  # Log-Normal para Rs
        "T": uniform.rvs(loc=150, scale=200, size=num_samples, random_state=seed), # Uniform para T
        "API": uniform.rvs(loc=20, scale=20, size=num_samples, random_state=seed),  # Uniforme para API
        "SG_g": norm.rvs(loc=0.75, scale=0.05, size=num_samples, random_state=seed),  # Normal para gamma_gs
    }

    # Limitar valores dentro de un rango si es necesario
    data["Rs"] = np.clip(data["Rs"], 100, 800)          # Limitar Rs entre 100 y 800
    data["SG_g"] = np.clip(data["SG_g"], 0.6, 0.9)  # Limitar gamma_gs entre 0.6 y 0.9

    return pd.DataFrame(data)
