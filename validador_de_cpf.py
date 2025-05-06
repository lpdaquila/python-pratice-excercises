import sys

cpf = '212.252.348-40'
cpf_limpo = cpf.translate(str.maketrans('', '', ' .-()'))
# print(cpf_limpo)
# exit()

cpf_eh_sequencial = cpf == cpf[0] * len(cpf)
if cpf_eh_sequencial:
    print('CPF Inválido')
    sys.exit()
    
nove_digitos = cpf_limpo[:9]
contador_regressivo_1 = 10
resultado_digito_1 = 0
# Primeiro dígito
for digito_1 in nove_digitos:
    # print(digito_1, type(digito_1))
    resultado_digito_1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1
    
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

# Segundo dígito
dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11
resultado_digito_2 = 0

for digito_2 in dez_digitos:
    resultado_digito_2 += int(digito_2) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0
    
# print('Digito 1: %d' % digito_1)
# print('Digito 2: %d' % digito_2)

novo_cpf = '%s digito 1: %s digito 2: %s' % (nove_digitos, str(digito_1), str(digito_2))

if cpf_limpo == novo_cpf:
    print('CPF Válido')
else:
    print('CPF Inválido')
    
print('Novo CPF: %s' % novo_cpf)