# O programa deve ler um valor inteiro X indefinidas vezes. (O programa irá parar quando o valor de X
# for igual a 0). Para cada X lido, imprima a soma dos 5 pares consecutivos a partir de X, inclusive o X
# , se for par. Se o valor de entrada for 4, por exemplo, a saída deve ser 40, que é o resultado da operação:
# 4+6+8+10+12, enquanto que se o valor de entrada for 11, por exemplo, a saída deve ser 80, que é a
# soma de 12+14+16+18+20.
x = int(input("Digite um número inteiro: "))
soma: int = 0
while x != 0:
    cont = 0
    soma = 0
    if x % 2 == 0:
        for i in range(0, 5):
            soma = soma + x
            cont += 1
            x += 2
    else:
        x += 1
        for i in range (0, 5):
            soma = soma + x
            cont += 1
            x += 2
    print(f'SOMA = {soma}')
    x = int(input("Digite um número inteiro: "))