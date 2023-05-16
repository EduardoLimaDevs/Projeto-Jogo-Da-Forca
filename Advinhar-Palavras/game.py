import random


def jogar():    
        def teste(a):
            c=[]
            for i in a:
                if i != ' ':
                    c.append('_')
                else:
                    c.append(' ')
            return ''.join(c)



        palavra_secreta = carregar_palavra_secreta()

        letra_acertadas = teste(palavra_secreta)
        print(letra_acertadas)
        enforcou = False
        acertou = False
        erros = 0


#imagem da forca 
            
        while(not enforcou and not acertou):
            chute = input("Digite uma letra: ")
            chute = chute.strip().upper()
            if chute in palavra_secreta:
                letra_acertadas = marcar_chute_correto(palavra_secreta, chute, letra_acertadas)
                print(letra_acertadas)
            else:
                erros += 1
                print(f'Voce errou {erros} de 7 tentativas')

            enforcou = erros == 7
            acertou = "_" not in letra_acertadas
            print(acertou)


        if(acertou):
            print("Parabens voce ganhou! ")
        else:
            print("Voce perdeu !")


def carregar_palavra_secreta():
            arquivo = open('comidas.txt', 'r')
            palavras = []

            for linha in arquivo:
                linha = linha.strip()
                palavras.append(linha)
            arquivo.close()
            numero = random.randrange(0, len(palavras))
            palavra_secreta = palavras[numero].upper()
            
            return palavra_secreta


def marcar_chute_correto(palavra_secreta, chute, letras_acertadas):
            
            b = list(letras_acertadas)
            for i,letra in enumerate(palavra_secreta):
                if chute == letra :
                    b[i] = letra
            print(b)
            return ''.join(b)
            
jogar()
