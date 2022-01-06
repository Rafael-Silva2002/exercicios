print('=-'*10, 'Jogo da Velha', '-='*10)
print()
tab = ['-']*3
lista_verif = []

####Tabuleiro
for i in range(3):
    tab[i] = ['-']*3
    print(*tab[i])

i = cont_col = cont_col2 = cont_diag = cont_diag2 = 0
while i != 9 and cont_col != 3 and cont_col2 != 3 and cont_diag != 3 and cont_diag2 != 3:
    ponto = 'X' if i % 2 == 0 else 'O'
    jogador = 'Jogador1' if i % 2 == 0 else 'Jogador2'
    print(jogador)
    while True:
        lin = int(input('Informe a linha (1-3): '))-1
        col = int(input('Informe a coluna (1-3): '))-1
        verif = str(lin+1)+str(col+1)
        if verif not in lista_verif and lin in range(0, 3) and col in range(0, 3):
            lista_verif.append(verif)
            break
        print('Jogada Inválida!')

    if jogador == 'Jogador1':
        tab[lin][col] = 'X'
    else:
        tab[lin][col] = 'O'
    for a in range(3):
        for b in range(3):
            print(tab[a][b], end=' ')
        print()

    if i > 3:
        cont_col = cont_col2 = cont_diag = cont_diag2 = 0
        for a in range(3):
            for b in range(3):
                if a == lin:
                    if tab[a][b] == ponto:
                        cont_col += 1

                if b == col:
                    if tab[a][b] == ponto:
                        cont_col2 += 1

                if lin+col == a+b:
                    if tab[a][b] == ponto:
                        cont_diag += 1

                if lin-col == a-b:
                    if tab[a][b] == ponto:
                        cont_diag2 += 1
        if cont_col == 3 or cont_col2 == 3 or cont_diag == 3 or cont_diag2 == 3:
            print(f'{jogador} é o Vencedor!')
    i += 1