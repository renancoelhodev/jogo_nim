import os
from time import sleep
import jogadas


def partida():
    os.system("color 07")
    print("*******************************************************************************")
    print("*                                                                             *")
    print("*                              JOGO INICIADO                                  *")
    print("*                                                                             *")
    print("*******************************************************************************")

    n = int(input("Quantas peças?  "))
    m = int(input("Limite de peças por jogada? "))

    if n % (m + 1) == 0:
        print("Você começa")

        while n > 0:

            n = n - jogadas.usuario_escolhe_jogada(n, m)
            print("Agora restam", n, "peças no tabuleiro")

            if n != 0:
                n = n - jogadas.computador_escolhe_jogada(n, m)
                print("Agora restam", n, "peças no tabuleiro")

        sleep(2)
        os.system("color 04")
        print("O computador venceu!")

    else:
        print()
        print("Computador começa")

        while n > 0:
            n = n - jogadas.computador_escolhe_jogada(n, m)
            print("Agora restam", n, "peças no tabuleiro")

            if n != 0:
                n = n - jogadas.usuario_escolhe_jogada(n, m)
                print("Agora restam", n, "peças no tabuleiro")

        print()
        sleep(2)
        os.system("color 04")
        print("O computador venceu!")


def campeonato():
    cont = 0
    while cont < 3:

        print("                    #####################################")
        print("                    #              RODADA %d             #" % (cont+1))
        print("                    #####################################")
        print("                    #               PLACAR              #")
        print("                    #           VOCÊ 0 X %d PC           #" % (cont))
        print("                    #####################################")
        print()
        partida()
        print()

        if cont < 2:
            os.system("color 04")
            print("Você perdeu :( !! Mas não desista!")
            print("Aguarde para uma nova partida ser iniciada.")
            sleep(4)
            os.system("cls")

        else:
            print("Calculando placar...")
            sleep(3)

        cont += 1
