import os
os.system("cls || clear")

n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))

print("media: ", (n1+n2)/2)
print("soma: ", (n1+n2))
print("produto: ", (n1*n2))

if n1 > n2:
    print("maior: ", n1)
    print("menor: ", n2)
    
else:
    print("maior: ", n2)
    print("menor: ", n1)
    