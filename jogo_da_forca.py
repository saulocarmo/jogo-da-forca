
print('Jogo da Forca')
print('Adivinhe a qual a palavra secreta')
print()
print('Mas calma, você só tem 5 chances.')
print()
print('dica... é algo que tem em casa e usamos no corpo.')
print()
secreto = 'perfume'
digitadas = []
chances = 5

while True:
    if chances <= 0 :
        print('Lamento, mas suas chances acabaram, infelizmente você PERDEU !!!')
        break


    letra =input('Digite uma letra: ')

    if len(letra) > 1 :
        print('Opaa, nada de trapaça ! Digite apenas uma letra por vez.')
        continue
    
    digitadas.append(letra)

    if letra in secreto:
        print(f'Aeee.. a letra {letra}, EXISTE na palavra secreta')
    else:
        print(f'Humm, a letra {letra}, NÃO existe na palavra secreta')
        digitadas.pop()
    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'    

    if secreto_temporario == secreto:
        print(f'AEEE, você acertou, MEUS PARABÉNS ! A palavra secreta é {secreto}')
        break
    else:
        print(f'Olha, a palavra secreta está assim : {secreto_temporario}')  

    if letra not in secreto_temporario:
        chances -= 1     
    print(f'Você ainda tem {chances} chances')     



    

    
   
   


