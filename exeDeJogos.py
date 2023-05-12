import exeAdivinhar as executar_Jogo_Da_Adivinhacao
import exeForca as executar_Jogo_Da_Forca
from time import sleep as loading

def carregarJogo():
    print("Carregando jogo...")
    loading(2)
    print("iniciando jogo!")
    loading(0.8)
    print("\nJogo iniciado em regime de POO (PROGRAMAÇÃO ORIENTADA A OBJETOS)\n")

def menuDeOpcoes():

    print("       _                             _         _    _       _   _    ")
    print("      | |                           | |       |  \/  |     | | | |   ")
    print("      | | ___   __ _  ___  ___    __| | ___   | \  / | __ _| |_| |_  ")
    print("  _   | |/ _ \ / _` |/ _ \/ __|  / _` |/ _ \  | |\/| |/ _` | __| __| ")
    print(" | |__| | (_) | (_| | (_) \__ \ | (_| | (_) | | |  | | (_| | |_| |_  ")
    print("  \____/ \___/ \__, |\___/|___/  \__,_|\___/  |_|  |_|\__,_|\__|\__| ")
    print("                __/ |                                                ")
    print("               |___/                                               \n")

    print("Biblioteca de jogos feita por Matheus Willians\n")

    while True:
        try:
            jogo_Escolhido = int(input("Qual desses jogos deseja jogar?\nJOGO DA FORCA --> DIGITE 1\nJOGO DA ADIVINHAÇÃO --> DIGITE 2\nFECHAR O PROGRAMA --> DIGITE 3\n>>> "))
        
        except ValueError:
            print("O valor digitado não é um numero")
            continue         

        if(jogo_Escolhido == 1):
            carregarJogo()
            executar_Jogo_Da_Forca.menu_Do_Jogo()
            continue

        elif(jogo_Escolhido == 2):
            carregarJogo()
            executar_Jogo_Da_Adivinhacao.iniciarJogo()
            continue
        
        elif(jogo_Escolhido == 3):
            print("Obrigado por jogar na minha biblioteca!")
            print("          _                                                          ")
            print("     /\  | |                                                         ")
            print("    /  \ | |_ ___     __ _    _ __  _ __ _____  ___ _ __ ___   __ _  ")
            print("   / /\ \| __/ _ \   / _` |  | '_ \| '__/ _ \ \/ / | '_ ` _ \ / _` | ")
            print("  / ____ \ ||  __/  | (_| |  | |_) | | | (_) >  <| | | | | | | (_| | ")
            print(" /_/    \_\__\___|   \__,_|  | .__/|_|  \___/_/\_\_|_| |_| |_|\__,_| ")
            print("                             | |                                     ")
            print("                             |_|                                     \n")
            break

        else:
            print("Opção não existe, tente novamente.")
            continue

if(__name__ == "__main__"):
    menuDeOpcoes()