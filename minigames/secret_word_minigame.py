palavra_secreta = 'python'
letras_acertadas = ''
tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ').lower()
    tentativas += 1
    
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue
    
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
    
    palavra_formada = ''
    for letra in palavra_secreta:
        if letra in letras_acertadas:
            palavra_formada += letra
            # print(letra, end=' ')
        else:
            palavra_formada += '*'
    print(palavra_formada)
    
    if palavra_formada == palavra_secreta:
        print('Parabéns! Você acertou a palavra secreta.')
        print('Você precisou de %d tentativas para acertar a palavra "%s"' % (tentativas, palavra_secreta))
        letras_acertadas = ''
        tentativas = 0
        break
    

status = input('Deseja continuar jogando? (s/n): ').lower()
match status:
    case 's':
        print('Continuando o jogo...')
    case 'n':
        print('Obrigado por jogar!')
    case _:
        print('Opção inválida. Encerrando o jogo.')