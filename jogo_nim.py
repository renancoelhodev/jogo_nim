# *********************************
# *                               *
# *                               *
# *       CÓDIGO FEITO POR        *
# *         RENAN COELHO          *
# *                               *
# *                               *
# *********************************

from sys import exit
import os  # biblioteca para limpar a tela/alterar tamanho do terminal
import opcoes
import jogadas


def iniciar_nim():
    os.system("color 07")  # muda cor do terminal
    escolha = 1

    while(escolha > 0):

        os.system("cls")
        print("*******************************************************************************")
        print("*                                                                             *")
        print("*                            CÓDIGO FEITO POR                                 *")
        print("*                              RENAN COELHO                                   *")
        print("*                                                                             *")
        print("*******************************************************************************")
        print()
        print("Bem-vindo ao jogo do NIM! Escolha: ")
        print()
        print("1 - para jogar uma partida isolada")
        print("2 - para jogar um campeonato")
        print("3 - para ler as instruções")
        print("0 - para SAIR")

        escolha = int(input("Digite: "))

        if escolha == 1:
            os.system("cls")
            opcoes.partida()
            print()
            print("Deseja voltar ao menu? [S/N]")
            escolhasair = input("Escolha: ")

            if escolhasair.lower() == 's':
                iniciar_nim()

            else:
                sys.exit(1)

        elif escolha == 2:
            os.system("cls")
            opcoes.campeonato()
            tela_final()
        elif escolha == 3:
            about()

        elif escolha == 0:
            sys.exit(1)


def about():
    os.system("cls")
    print("*******************************************************************************")
    print("*                                                                             *")
    print("*                               INSTRUÇÕES                                    *")
    print("*                                                                             *")
    print("*******************************************************************************")
    print("Você conhece o jogo do NIM?")
    print()
    print("Nesse jogo, n peças são inicialmente dispostas numa mesa ou tabuleiro.")
    print()
    print("Dois jogadores jogam alternadamente, retirando pelo menos 1 e no máximo m peças cada um. Quem tirar as últimas peças possíveis ganha o jogo.")
    print()
    escolha = input("Digite S para voltar a tela inicial: ")

    if escolha == 'S' or escolha == 's':
        iniciar_nim()


def tela_final():
    print()
    print("**** Final do campeonato! ****")
    print()
    print("Placar: Você 0 X 3 Computador")
    print()
    print("Digite S para voltar a tela inicial: ")
    escolha = input("Digite:")

    if escolha == 'S' or escolha == 's':
        iniciar_nim()

    else:
        sys.exit(1)


def main():

    os.system("mode 80,40")
    iniciar_nim()


main()
