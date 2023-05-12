# IDEIA ORIGINAL: CRIAR UM JOGO DA FORCA SIMPLES, ONDE O JOGADOR TENTA ADIVINHAR A PALAVRA, CONFORME ELE ADIVINHA AS LETRAS, ELAS APARECEM NO DISPLAY, NO TOTAL SÃO 6 TENTATIVAS.
# ESTE PROJETO FOI IDEALIZADO NO CURSO DE POO EM PYTHON, POREM, EU DECIDI TENTAR FAZER O PROJETO SEM O CURSO PRA QUEBRAR UM POUCO A CABEÇA
# IREI EXPLICAR O PROJETO NOS PROXIMOS COMENTARIOS.

# random = gerar dados aleatorios / os = manipular pastas, arquivos e dados / time-sleep = da a falsa sensação de um jogo mesmo, apenas para fluidez da gameplay.
import random
import os
from time import sleep as timeDelay

#esta função é feita para gerar uma lista de palavras aleatórias
def lista_De_Palavras(tipo_Escolhido):

    file_path = ''

    if tipo_Escolhido == 1:
        #explicando esta linha:
        file_path = os.path.join(os.path.dirname(__file__), "opcoes", "frutas.txt")
        #os.path.join <-- agregar local de armazenamento de um diretorio com outro, sem muitas complicações (usei essa solução pois colocar o diretorio: opcoes/frutas.txt não funciona, e esse modo de escrever depende do sistema operacional)
        #dentro do os.path.join passamos os diretorios que queremos transformar em um separando por virgula, e o os.path.dirname(__file__) pega o local do nosso arquivo python e depois, juntamos com o resto dos diretorios, ficando assim: C:/Users/NomeDePasta/opcoes/frutas.txt
    
    elif tipo_Escolhido == 2:
        file_path = os.path.join(os.path.dirname(__file__), "opcoes", "cores.txt")

    else:
        print("Ocorreu um erro ao escolher as palavras.")

    #detecta se o arquivo foi encontrado ou não, e retorna um erro
    if not os.path.isfile(file_path):
        return FileNotFoundError(f"File not found: {file_path}")

    #com o arquivo aberto em modo de "R" = leitura
    with open(file_path, 'r') as file:

        #leia o arquivo e joga tudo nessa string
        palavras_Escolhidas = file.read()
    
    #transforma as palavras STRING em listas separadas por pulos de linha, depois pega uma palavra aleatoria da lista para o jogo
    lista = palavras_Escolhidas.split('\n')
    lista = random.choice(lista)
    
    #fecha o arquivo e retorna a lista.
    file.close()
    return lista

def display_Do_Jogo(total_De_Erros, espaco_Forca, palavra_Secreta, letras_Digitadas):

    #O join é usado para juntar itens de uma lista com um separador definido, neste caso, a lista vem: ["a", "b"], com a formatação: a b
    print("letras já digitadas:", " ".join(letras_Digitadas))

    if(total_De_Erros == 0):
        print("+------+")
        print("|       ")
        print("|       ")
        print("|       ")
        print("|       ")
        print("|       ")
        print("|       ")
        print("|       ")
        print("L", " ".join(espaco_Forca))
    
    elif(total_De_Erros == 1):
        print("+------+")
        print("|      O")
        print("|       ")
        print("|       ")
        print("|       ")
        print("|       ")
        print("|       ")
        print("|       ")
        print("L", " ".join(espaco_Forca))
        print("O personagem começou a aparecer!")
    
    elif(total_De_Erros == 2):
        print("+------+")
        print("|      O")
        print("|      |")
        print("|       ")
        print("|       ")
        print("|       ")
        print("|       ")
        print("|       ")
        print("L", " ".join(espaco_Forca))
        print("Cuidado! Não queremos matar nosso amiguinho.")

    elif(total_De_Erros == 3):
        print("+------+")
        print("|      O")
        print("|     /|")
        print("|       ")
        print("|       ")
        print("|       ")
        print("|       ")
        print("|       ")
        print("L", " ".join(espaco_Forca))
        print("Preste mais atenção!")

    elif(total_De_Erros == 4):
        print("+------+ ")
        print("|      O ")
        print("|     /|Z")
        print("|        ")
        print("|        ")
        print("|        ")
        print("|        ")
        print("|        ")
        print("L", " ".join(espaco_Forca))
        print("Pobre boneco de palito...")

    elif(total_De_Erros == 5):
        print("+------+ ")
        print("|      O ")
        print("|     /|Z")
        print("|     /  ")
        print("|        ")
        print("|        ")
        print("|        ")
        print("|        ")
        print("L", " ".join(espaco_Forca))
        print("Você NÃO PODE errar novamente!! Cuidado!!")

    elif(total_De_Erros == 6):
        print("+------+ ")
        print("|      X ")
        print("|     /|Z")
        print("|     / \ ")
        print("|        ")
        print("|        ")
        print("|        ")
        print("|        ")
        print("L", " ".join(espaco_Forca))
        print(f"Você morreu! a palavra certa era: {palavra_Secreta}")
 
def jogar_Forca():
    
    palavra_Escolhida = ""

    while True:

        #Menu Amigavel :D
        print("Escolha a classe das palavras!\n( 1 ) -> nomes de Frutas\n( 2 ) -> nomes de Cores\n( 3 ) -> Fechar o jogo.")
        
        #tratamento de erros para evitar problemas de digitação
        try:
            classe_Escolhida = int(input(">>> "))
            
            print("> Carregando opção...")
            timeDelay(2)

            if(classe_Escolhida < 1 or classe_Escolhida > 3):
                print(">> Digite um numero da LISTA!")
                continue

            elif(classe_Escolhida == 1 or classe_Escolhida == 2):
                #Print para dar sensação de que é reamente um jogo
                print(">> Carregando jogo...")
                timeDelay(2)
                print(">>> Carregando palavra aleatória...")
                timeDelay(2)
                print(">>>> Gerando Forca!")

                palavra_Escolhida = lista_De_Palavras(classe_Escolhida)
                
            elif(classe_Escolhida == 3):
                print(">> fechando jogo...")
                timeDelay(2)
                break

            else:
                print(">> Ocorreu um erro desconhecido, tente novamente...")
                continue    
        except:
            print(">> O que você digitou não é um numero! nem uma opção possivel.")
            continue

        total_De_Erros = 0
        
        #usei um SET, pois não queremos que nosso jogador fique escolhendo a MESMA letra todo o tempo
        letras_Adivinhadas = set()

        #o espaço da forca, tem que ter o mesmo tamanho do total de letras da palavra
        #então vamos ter o "_" para cada letra na palavra escolhida
        espaco_Forca = ["_" for i in range(len(palavra_Escolhida))]
        
        #print(palavra_Escolhida) <-- GAME CHEAT, NÃO REMOVA ESTE COMENTARIO

        while True:

            display_Do_Jogo(total_De_Erros, espaco_Forca, palavra_Escolhida, letras_Adivinhadas)

            #antes de continuar o jogo, vemos se o player ja passou o limite de erros ou se ele acertou a palavra
            if(total_De_Erros == 6):
                print("Infelizmente, você foi de base, sinto muito.")
                break

            #a gente junta as letras do display e compara com a palavra!
            elif("".join(espaco_Forca) == palavra_Escolhida):
                print (f"Parabêns! Você acertou, a palavra era: {palavra_Escolhida}")
                timeDelay(2)
                break
            
            #Definimos a letra pedindo ao jogador, colocando ela em LOWER CASE, pois é a forma que todas as palavras estão no nosso programa 
            letra_Digitada = input("Digite uma letra!\n+--> ")
            letra_Digitada.lower()
            print("Hum... sera que esta correta?")
            timeDelay(2)

            #vemos se a letra é tudo menos uma letra, se não for letra, ele pede para digitar denovo
            if letra_Digitada in ("1234567890!@#$%¨&*()_+=§-¬¢£³²¹\|,.;/~][<>:?}^{`°ºª '"):
                print("digite uma letra do alfabeto!")
                continue
            
            #se a letra ja tiver sido digitada, a gente pede denovo
            elif(letra_Digitada in letras_Adivinhadas):
                print("Letra já digitada! Tente novamente")
                continue
            
            #caso a letra não esteja na palavra escolhida, adicionamos ela a lista de palavras ja digitadas
            elif(letra_Digitada not in palavra_Escolhida ) and (letra_Digitada not in letras_Adivinhadas):
                print("Você errou! Esta letra não esta presente.")
                total_De_Erros += 1
                letras_Adivinhadas.add(letra_Digitada)
                continue
            
            #caso a letra esteja na palavra              e não esteja na lista de letras               e ainda tenha letra faltando
            elif(letra_Digitada in palavra_Escolhida ) and (letra_Digitada not in letras_Adivinhadas) and ("_" in espaco_Forca):
                
                print("Voce acertou! A letra esta na palavra!")
                letras_Adivinhadas.add(letra_Digitada)

                #vamos varrer a palavra
                for i in range (len(palavra_Escolhida)):
                    #comparar a letra com cada letra da palavra até achar a letra que corresponde
                    if letra_Digitada == palavra_Escolhida[i]:
                        #e substituir no mesmo espaço da forca pela letra digitada
                        espaco_Forca[i] = letra_Digitada
                        continue
            
def menu_Do_Jogo():

    print("     _                    _         __                 ")
    print("  _ | |___  __ _ ___   __| |__ _   / _|___ _ _ __ __ _ ")
    print(" | || / _ \/ _` / _ \ / _` / _` | |  _/ _ \ '_/ _/ _` |")
    print("  \__/\___/\__, \___/ \__,_\__,_| |_| \___/_| \__\__,_|")
    print("           |___/                                       \n")
    
    print("Quer iniciar o jogo?\n")
    while True:
        
        print("Digite ( S ) para começar e ( N ) para sair do jogo")

        try: 
            iniciar_Jogo = input(">>> ")
            print(". . .")
            timeDelay(1)
        except: 
            print("Algo digitado esta incorreto, tente novamente...")
            continue

        if(iniciar_Jogo.upper() == "S"):
            print("iniciando jogo!")
            jogar_Forca()
            continue

        elif(iniciar_Jogo.upper() == "N"):
            print("Até a proxima!")
            break
        
        else:
            print("Opção inválida!")
            continue

if (__name__ == "__main__"):
    print("Iniciando jogo...")
    menu_Do_Jogo()