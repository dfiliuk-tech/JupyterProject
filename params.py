from scipy import constants
variant_number = 7
G_max = 500 + pow(-1, variant_number) * 5 * variant_number

G_min = (2 * G_max) / 3

n_y_max = 2.1 + 10900 / (G_max + 4536)
n_y_min = -0.4*n_y_max

S_kr = 4 + pow(-1, variant_number) * 0.02 * variant_number  # площа крила

alpha_cy = {
    -4: -0.31,
    -2: -0.11,
    0: 0.10,
    2: 0.31,
    4: 0.51,
    6: 0.72,
    8: 0.93,
    10: 1.12,
    12: 1.29,
    14: 1.44,
    16: 1.50,
    18: 1.47,
    20: 1.35
}

alpha_cx = {
    -4: 0.07,
    -2: 0.06,
    0: 0.05,
    2: 0.05,
    4: 0.06,
    6: 0.07,
    8: 0.08,
    10: 0.09,
    12: 0.11,
    14: 0.15,
    16: 0.17,
    18: 0.16,
    20: 0.12
}
# Знайдемо максимальний коефіцієнт підіймальної сили
c_y_max = max(alpha_cy.values())  # 1.50 при α = 16°
c_y_min = min(alpha_cy.values())
msa = {
    0: {
        "temperature": 289,
        "pressure": 10.1e4,
        "density": 1.225,
        "sound_speed": 340
    },
    500: {
        "temperature": 285,
        "pressure": 9.55e4,
        "density": 1.167,
        "sound_speed": 338
    },
    1000: {
        "temperature": 282,
        "pressure": 8.99e4,
        "density": 1.112,
        "sound_speed": 336
    },
    1500: {
        "temperature": 278,
        "pressure": 8.46e4,
        "density": 1.058,
        "sound_speed": 334
    },
    2000: {
        "temperature": 275,
        "pressure": 7.95e4,
        "density": 1.007,
        "sound_speed": 332
    },
    2500: {
        "temperature": 272,
        "pressure": 7.47e4,
        "density": 0.957,
        "sound_speed": 330
    },
    3000: {
        "temperature": 269,
        "pressure": 7.01e4,
        "density": 0.909,
        "sound_speed": 328
    },
    3500: {
        "temperature": 265,
        "pressure": 6.58e4,
        "density": 0.863,
        "sound_speed": 326
    },
    4000: {
        "temperature": 252,
        "pressure": 6.17e4,
        "density": 0.819,
        "sound_speed": 324
    },
    4500: {
        "temperature": 259,
        "pressure": 5.77e4,
        "density": 0.777,
        "sound_speed": 322
    },
    5000: {
        "temperature": 256,
        "pressure": 5.40e4,
        "density": 0.736,
        "sound_speed": 320
    },
    10000: {
        "temperature": 223,
        "pressure": 2.65e4,
        "density": 0.414,
        "sound_speed": 299
    },
    10500: {
        "temperature": 220,
        "pressure": 2.45e4,
        "density": 0.389,
        "sound_speed": 297
    },
    11000: {
        "temperature": 216,
        "pressure": 2.24e4,
        "density": 0.365,
        "sound_speed": 295
    }
}


# Input parameters
g = constants.g  # м/с²
H = 0  # висота польоту, м

# З таблиці МСА беремо щільність на H=0
rho_0 = msa[H]["density"]  # 1.225 кг/м³
sound_speed = msa[0]["sound_speed"]  # 340 м/с

#розрахунки
# c_y приймаємо як 1/5 від c_y_max
# з таблиці/графіка бачимо що c_y_max ≈ 1.5
 # для крейсерської швидкості
cy_cruise = 0.3