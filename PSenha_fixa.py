# Escreva um programa que repita a leitura de uma senha até que ela seja válida. Para cada leitura de
# senha incorreta informada, escrever a mensagem "Senha Invalida! Tente novamente:". Quando a senha
# for informada corretamente deve ser impressa a mensagem "Acesso Permitido" e o algoritmo
# encerrado. Considere que a senha correta é o valor 2002.
senha = 2002
senha_digitada = int(input("Digite a senha: "))
while senha_digitada != senha:
    senha_digitada = int(input("SENHA INCORRETA, TENTE NOVAMENTE: "))
print("Acesso Permitido!")