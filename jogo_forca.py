print('=-'*10, 'Jogo da Forca', 10*'-=')

palavra = input("Informe a palavra: ").upper()
dica = input("Dica: ")
test_pal = ['_'] * len(palavra)
letra_usada = []

if ' ' in palavra:
    for p, v in enumerate(palavra):
        if v == ' ':
            test_pal[p] = '-'

# Contando hífen, qtd tentativas
hifen = test_pal.count('-')
tent = len(palavra) - hifen

print(f'Dica: {dica}, {tent} letras')
print(*test_pal)
print('-='*15)

i = 1
while i <= tent and '_' in test_pal:
    print(f'Tentativas = {tent - i + 1}')
    while True:
        letra = input(f'Informe a letra: ').upper()
        if letra not in letra_usada and len(letra) == 1:
            letra_usada.append(letra)
            break
        print('Tente Novamente!')
    for j, v in enumerate(palavra):
        if letra == v:
            test_pal[j] = letra
    print(*test_pal)
    print('-=' * 15)
    i += 1

if '_' not in test_pal:
    print('Venceu!')
else:
    print('Perdeu!')
print('Palavra: ', palavra)