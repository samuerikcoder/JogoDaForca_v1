import random

try:
    import emoji
except ModuleNotFoundError:
    pass

palavras = ['python', 'programacao', 'computador', 'algoritmo', 'tecnologia',
            'good-vibes', 'amor', 'github', 'sapo', 'gato', 'game', 'backend']

palavra_secreta = random.choice(palavras)

palavra_lista = list(palavra_secreta)

letras_adivinhadas = []

vidas = 6

print('-' * 50)
print('                   JOGO DA FORCA')
print('-' * 50)

while vidas > 0:
    palavra_mostrada = ""
    for letra in palavra_secreta:
        if letra in letras_adivinhadas:
            palavra_mostrada += letra
        else:
            palavra_mostrada += '_'
    print('Palavra: ', palavra_mostrada)

    try:
      print('Vidas : ', emoji.emojize(':red_heart: ', variant='emoji_type') * vidas)
    except (ModuleNotFoundError, NameError):
      print('Vidas: ','<3 ' * vidas)
      
    letra = input('Digite uma letra: ').strip().lower()[0]

    if letra in letras_adivinhadas:
        print('Você já adivinhou essa letra antes!')
    else:
        letras_adivinhadas.append(letra)

        if letra in palavra_secreta:
            print('Você adivinhou uma letra!')
        else:
            print('Essa letra não está na palavra secreta')
            letras_adivinhadas.remove(letra)
            vidas -= 1

    if set(palavra_lista) == set(letras_adivinhadas):
        print('\nParabéns! Você venceu!')
        break

if vidas == 0:
    print('\nVocê perdeu! A palavra secreta era', palavra_secreta)

print('-' * 50)