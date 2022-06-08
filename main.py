import emoji 

print(emoji.emojize("Olá seja bem-vindo! :hand_with_fingers_splayed:\n "))
print(emoji.emojize("Iremos jogar um quiz de Geografia, ok? :globe_showing_Americas:\n "))
nome = input("Certo, mas antes de começarmos, qual o seu nome? ")
print("\nTemos três dificuldades! 1, 2 e 3.\n\nA dificuldade 1 é para iniciantes\nA dificuldade 2 é para bons entendedores\nA dificuldade 3 para Geógrafos")
dificuldade = int(input(f'\nNovamente bem-vindo {nome}. Qual o nível de dificuldade você deseja, digite em forma de número: '))

def perguntas():

    count = 0

    if dificuldade == 1:
        print(emoji.emojize("\nPara sermos bons, precisamos começar de baixo! Bela escolha. :1st_place_medal: "))
        print("\nVamos começar!\n")

    if dificuldade == 2:
        print(emoji.emojize("\nEvoluir sempre, treine seus conhecimentos! :beaming_face_with_smiling_eyes:"))
        print("\nVamos começar!\n")
        

    if dificuldade == 3:
        print(emoji.emojize("\nSerá que você entende mesmo? :exploding_head:"))
        print("\nVamos começar!\n")


perguntas()
