import os
import time
os.system('cls')

numero = int(input('Insira o numero: '))

for i in range(1, 11): 
    print(f'{numero} x {i} = {numero * i}')
    time.sleep(0.5)
    
