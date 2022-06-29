# Gerador de senha - Ravi Mughal
# Gerar 'n' senhas aleatórias
# Gerar tamanho dessas 'n' senhas aleatórias

import random


n = int(input("Numero de senhas a serem geradas: "))
car = int(input("Quantidade de caracteres da senha: "))

senha = ''
senhas = []

for i in range(n):
    for j in range(car):
        rd = random.randint(33, 128)
        # converter ASCII em char --> char == unico caracter
        rdch = '%s' % (chr(rd))
        senha += rdch
    senhas.append(senha)
    senha = ''

print('\n'.join(map(str, senhas)))
