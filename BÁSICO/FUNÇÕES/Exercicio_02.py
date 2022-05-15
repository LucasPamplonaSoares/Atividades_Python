def numero(n):
    return n % 2 == 0
    
n = int(input('Informe um número inteiro qualquer: ')) 

if numero(n):
    print(f'O número {n} é par')
else:
    print(f'O número {n} é impar')
