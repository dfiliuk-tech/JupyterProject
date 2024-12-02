import params
from math import sqrt
import numpy as np


def calculate_VTAS(V_EAS, rho, rho_0):
    """
    Розрахунок істинної швидкості через індикаторну
    """
    return V_EAS * sqrt(rho_0 / rho)


def calculate_V(G, rho, c_y):
  return  sqrt((2 * G * params.g) / (rho * params.S_kr * c_y))



def calculate_n_v_curve(V, cy, G, S, rho):
    """
    Розрахунок перевантаження для заданої швидкості та cy
    """
    q = 0.5 * rho * (V**2)  # швидкісний напір
    Y = cy * q * S  # підйомна сила
    n = Y/G  # перевантаження

    return n

def calculate_cy_alpha():
    # Беремо точки на лінійній ділянці графіка
    alpha1_deg = 0  # градуси
    alpha2_deg = 8  # градуси

    # Переводимо кути в радіани
    alpha1_rad = np.radians(alpha1_deg)
    alpha2_rad = np.radians(alpha2_deg)

    # Беремо відповідні значення c_y
    cy1 = params.alpha_cy[alpha1_deg]  # 0.10
    cy2 = params.alpha_cy[alpha2_deg]  # 0.93

    # Розраховуємо похідну
    c_y_alpha = (cy2 - cy1)/(alpha2_rad - alpha1_rad)

    return c_y_alpha


def calculate_mean_aerodynamic_chord():
    L_kr = 6 + pow(-1, params.variant_number) * 0.05 * params.variant_number
    eta = 2
    # Розрахунок кінцевої хорди
    # b_к = 2S_кр/(L_кр * (1 + η))
    b_k = 2 * params.S_kr / (L_kr * (1 + eta))

    # Розрахунок кореневої хорди
    # b_0 = b_к * η
    b_0 = b_k * eta

    # Розрахунок САХ
    # b = (2/3)(b_0 + b_к - (b_0 * b_к)/(b_0 + b_к))
    b = (2 / 3) * (b_0 + b_k - (b_0 * b_k) / (b_0 + b_k))

    return b

