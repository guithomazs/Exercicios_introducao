# Fazer um programa para ler o nome de um(a) funcionário(a), o valor que ele(a)
# recebe por hora, e a quantidade de horas trabalhadas por ele(a). Ao final, mostrar
# o valor do pagamento do funcionário com uma mensagem explicativa, conforme exemplo.

nome = str(input("Nome: "))
vhora = float(input("Valor por hora:"))
horas_trab = int(input("Horas trabalhadas: "))
print(f"O pagamento de {nome} deve ser {vhora * horas_trab:.2f} R$")