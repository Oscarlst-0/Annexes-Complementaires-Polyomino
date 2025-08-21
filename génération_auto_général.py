from fonctions_finale import polyo_dirigés_images
import time

"""
n = 12

for i in range(2, n + 1):
    start = time.time()
    polyo_dirigés_images(i)
    end = time.time()
    print(f"Temps d'exécution : {end - start:.2f} secondes pour n = {i}")"""


start = time.time()
polyo_dirigés_images(13)
end = time.time()
print(f"Temps d'exécution : {end - start:.2f} secondes pour n = {13}")
