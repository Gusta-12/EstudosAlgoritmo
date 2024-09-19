# Pegando as idades
n1 = int(input())
n2 = int(input())
n3 = int(input())

# Achando a idade de Camila
if n2 <= n1 <= n3 or n3 <= n1 <= n2:
    camilaIdade = n1
elif n1 <= n2 <= n3 or n3 <= n2 <= n1:
    camilaIdade = n2
else:
    camilaIdade = n3

#Exibindo na tela
print(f'Camila tem {camilaIdade} anos.')