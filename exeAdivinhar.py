# Jogo de advinhação
# -> entrar ou sair do jogo 
# -> escolher o numero para ver se é o correto
# -> o Bot escolhe um numero
# -> se o numero estiver correto, você ganha, se você errar, perde uma vida
# -> finalizar o jogo ao passar do limite de vida

# Biblioteca TIME, usei para dar delay entre as execuções das funções para dar um ar organico ao jogo
# Bibliotecla RANDOM = gerador aleatório de dados pré existentes
import random as random_number
from time import sleep as delayOf

# função que define tudo com relação ao JOGO
def fazerSuaJogada(dificuldadeDeJogo):

    # Faz a escolha do computador, com um delay de 1.5 segundos para dar a sensação de que ele esta realmente pensando
    print("o computador irá escolher um numero...")
    delayOf(2)
        
    # Define as configurações do jogo segundo a dificuldade escolhida
    if (dificuldadeDeJogo == 1):

        numero_escolhido_pelo_bot = random_number.randint(1,10)
        total_de_tentativas = 6
        limite_jogada = 10

    elif (dificuldadeDeJogo == 2):
        
        numero_escolhido_pelo_bot = random_number.randint(1,15)
        total_de_tentativas = 5
        limite_jogada = 15

    elif (dificuldadeDeJogo == 3):

        numero_escolhido_pelo_bot = random_number.randint(1,20)
        total_de_tentativas = 3
        limite_jogada = 20

    else:
        print("Opção digitada inexistente ou incorreta, tente novamente.")
        return

    print("O computador escolheu um numero...")
    delayOf(1)

    # inicia o jogo segunto a quantidade de tentativas existentes
    while (total_de_tentativas > 0):

        # caso o usuario não digite um NUMERO, ele repete a pergunta
        try:
            numero_escolhido_pelo_player = int(input("Me diga, qual numero você acha que o bot escolheu?\n>>> "))
        except:
            print("Digite um NUMERO INTEIRO")
            continue
        
        #Caso o numero escolhido seja diferente do limite de numeros, ele cancela a tentativa, e repete a pergunta 
        if (numero_escolhido_pelo_player < 1 or numero_escolhido_pelo_player > limite_jogada):

            print("Numero fora dos limites... tente novamente\nnumero limite: ", limite_jogada)
            continue

        elif (numero_escolhido_pelo_player == numero_escolhido_pelo_bot):

            print('Meus parabens, você esta correto, o numero escolhido pelo bot era {}'.format(numero_escolhido_pelo_bot))
            return
        
        total_de_tentativas -= 1

        if (numero_escolhido_pelo_bot > numero_escolhido_pelo_player):

            print('Você errou, o numero é maior... Voce tem: {} vidas restantes.'.format(total_de_tentativas))

        else:
            print('o numero era menor... você tem {} vidas restantes'.format(total_de_tentativas))

    print("Sinto muito, o numero esta errado... o correto era: ", numero_escolhido_pelo_bot)

# função que define tudo com relação a INICIAR O JOGO
def iniciarJogo():

    print(" +----------------------+ ")
    print(" | ADIVINHE OS NUMEROS! | ")
    print(" +----------------------+ ")

    while True:

        iniciar_jogo = input("Deseja jogar o jogo da adivinhação? S para SIM e N para NÃO \n>>> ")

        if (iniciar_jogo.lower() == "s"):       
            try:
                dificuldade_escolhida = int(input("Escolha o nivel de dificuldade:\n 1 - Facil\n --> Numeros entre 1 e 10 \n 2 - Médio \n --> Numeros entre 1 e 15 \n 3 - Dificil \n --> Numeros entre 1 e 20 \n \n>>> ")) 
            except:
                print("Digite um numero INTEIRO")
                continue

            fazerSuaJogada(dificuldade_escolhida)
            continue

        elif (iniciar_jogo.lower() == "n"):
            print("Até a proxima!\n")
            break

        else:
            print("Opção inválida, por favor, digite S para SIM e N para NÃO\n")
            continue

if (__name__ == "__main__"):
    print("\nJogo iniciado em regime padrão. (Não POO)\n")
    iniciarJogo()
