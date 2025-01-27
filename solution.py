import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1222500908 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    t=44
    n = len(x)
    mu = 1
    sigma = np.exp(1) 
    errorv = np.random.normal(mu, sigma, n)
    alpha = errorv/t
    loc = x.mean()
    scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    return loc - scale * norm.ppf(1 - alpha / 2), \
           loc - scale * norm.ppf(alpha / 2)
