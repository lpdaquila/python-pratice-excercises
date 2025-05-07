perguntas = [
    {
    'pergunta': 'Quanto é 2+2?',
    'opcoes': ['1', '2', '3', '4', '5'],
    'resposta': '4',
    },
    {
    'pergunta': 'Quanto é 5*5?',
    'opcoes': ['15', '25', '33', '40', '50'],
    'resposta': '25',
    },
    {
    'pergunta': 'Quanto é o módulo de 10 % 2 ?',
    'opcoes': ['7', '4', '0', '1', '9'],
    'resposta': '0',
    },
]
qtd_acertos = 0

for pergunta in perguntas:
    print()
    print('Pergunta:', pergunta['pergunta'], end='\n\n')
    
    opcoes = pergunta['opcoes']
    for i, opcao in enumerate(opcoes):
        print('%d)' % i, opcao)
    print()
    
    escolha = input('Escolha uma opcao: ')
    
    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)
    
    if escolha.isdigit():
        escolha_int = int(escolha)
        
    if escolha_int is not None:
        if escolha_int >=0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['resposta']:
                acertou = True
                
    if acertou:
        qtd_acertos += 1
        print('Acertou 👍')
    else:
        print('Errou ❌')
    print()
    
print('Você acertou %d de %d perguntas.' % (qtd_acertos, len(perguntas)))