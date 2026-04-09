# import math
from math import sqrt

num = 17
raiz = (sqrt(num))
print(f"A raiz de {num} é {raiz: .2f}")     # ".2f" limitando o número de casas decimais

import random

num_rand = random.random()      # Números aleátorios de 0 a 1 (nunca vai dar 1)
print(num_rand*10)

num_rand_int = random.randint(1, 60)        #sortear de 1 ao 60
print(num_rand_int)