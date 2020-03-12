from time import sleep


def computador_escolhe_jogada(n, m):

    if n > 0:
        if n <= m:  # retira o maior número de peças possíveis se o número de peças no tabuleiro for menor
            print()  # que o número de peças que podem ser retiradas em uma jogada
            sleep(2)
            print("O computador tirou", n, "peças.")
            return n

        elif n == 1:
            print()
            sleep(2)
            print("O computador tirou uma peça.")
            return 1

        else:
            i = m
            # procura uma quantidade de peças para retirar de modo
            # que reste um número de peças múltiplo de m+1
            while i != 1 and (n-i) % (m+1) != 0:
                i = - 1  
            print()
            sleep(2)
            print("O computador tirou", i, "peças.")
            return i


def usuario_escolhe_jogada(n, m):

    if n > 0:
        print()
        jogada_usuario = -1

        while jogada_usuario < 1 or jogada_usuario > m:
            jogada_usuario = int(input("Quantas peças você vai tirar? "))

        print("Você tirou", jogada_usuario, "peças.")
        return jogada_usuario
