import random

def main():
    print("Adivinhe o número!")
    print("Pense em um número entre 1 e 100")
    print("E eu tentarei adivinhá-lo em 7 tentativas ou menos")

    # gerar um número aleatório para ser adivinhado
    numero_secreto = random.randint(1, 100)
    total_de_tentativas = 0
    tentativas_restantes = 7

    while total_de_tentativas < 7:
        print("Tentativa {0} de {1}".format(total_de_tentativas + 1, 7))
        chute = int(input("Digite o seu número: "))
        
        if chute < numero_secreto:
            print("O seu número é menor do que o número secreto.")
        elif chute > numero_secreto:
            print("O seu número é maior do que o número secreto.")
        else:
            print("Parabéns! Você adivinhou o número em {0} tentativas".format(total_de_tentativas + 1))
            break
        
        total_de_tentativas += 1
        tentativas_restantes -= 1
        print("Você ainda tem {0} tentativas.".format(tentativas_restantes))
        
    print("Fim de jogo!")

if __name__ == "__main__":
    main()
