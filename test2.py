from scipy.stats import t, norm
import numpy as np

# Datos de la muestra
datos = [19, 10, 7, 6, 6, 4, 16, 11, 10, 9, 6, 5, 8, 5, 7, 12, 1]
print("Datos de la muestra: ", sum(datos))
# Tamaño de la muestra
n = len(datos)
print("Tamaño de la muestra: ", n)
# Calcular la media y la desviación estándar muestral
media_muestral = np.mean(datos)
print("Media muestral: ", media_muestral)
desviacion_estandar_muestral = np.std(datos, ddof=1)

# Límites del intervalo de confianza dados
limite_inferior = 6.482055
limite_superior = 12.223827

# Calcular el valor crítico t usando el límite superior (puede usarse cualquiera)
t_critico = (media_muestral - limite_inferior ) / (desviacion_estandar_muestral / np.sqrt(n))

# Encontrar el nivel de confianza
# Dado que es un intervalo de dos colas, calculamos el p-valor y lo duplicamos para obtener el nivel de confianza
p_valor = t.cdf(t_critico, n-1)
nivel_confianza = (p_valor - (1 - p_valor)) * 100

media_muestral, desviacion_estandar_muestral, nivel_confianza

print("Desviación estándar muestral: ", desviacion_estandar_muestral)
print("Nivel de confianza: ", nivel_confianza)
