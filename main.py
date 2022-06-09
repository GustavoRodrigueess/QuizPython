import emoji 

def intro():
    print(emoji.emojize("Olá seja bem-vindo! :hand_with_fingers_splayed:\n "))
    print(emoji.emojize("Iremos jogar um quiz de Geografia, ok? :globe_showing_Americas:\n "))
    nome = input("Certo, mas antes de começarmos, qual o seu nome? ")
    print("\nTemos três dificuldades! 1, 2 e 3.\n\nA dificuldade 1 é para iniciantes\nA dificuldade 2 é para bons entendedores\nA dificuldade 3 para Geógrafos")

    return nome

def nivel(nome):

    dificuldade = int(input(f'\nNovamente bem-vindo {nome}. Qual o nível de dificuldade você deseja, digite em forma de número: '))

    return dificuldade

# Função para criar sistema de perguntas e respostas com dicionário.

def perguntas(dificuldade):

    pontos = 0

    if dificuldade == 1:
        print(emoji.emojize("\nPara sermos bons, precisamos começar de baixo! Bela escolha. :1st_place_medal: "))
        print("\nVamos começar!\n")

        perguntas = {
            'Pergunta 1':{

            },

            'Pergunta 2':{

            },

            'Pergunta 3':{

            }
        }

    if dificuldade == 2:
        print(emoji.emojize("\nEvoluir sempre, treine seus conhecimentos! :beaming_face_with_smiling_eyes:"))
        print("\nVamos começar!\n")

        perguntas = {
            'Pergunta 1':{

            },

            'Pergunta 2':{

            },

            'Pergunta 3':{


            }

       }

    if dificuldade == 3:
        print(emoji.emojize("\nSerá que você entende mesmo? :exploding_head:"))
        print("\nVamos começar!\n")

        perguntas = {
            'Pergunta 1':{
                'pergunta':'Os países industriais adotaram uma concepção diferente das relações familiares e do lugar da fecundidade na vida familiar e social. A preocupação de garantir uma transmissão integral das vantagens econômicas e sociais adquiridas tem como resultado uma ação voluntária de limitação do número de nascimentos. Em meados do século XX, o fenômeno social descrito contribuiu para o processo europeu de: ',
                'resposta':{
                    'A':'estabilização da pirâmide etária.',
                    'B':'conclusão da transição demográfica.',
                    'C':'contenção da entrada de imigrantes.'
                }
            },

            'Pergunta 2':{
                'pergunta':'Em Beirute, no Líbano, quando perguntado sobre onde se encontram os refugiados sírios, a resposta do homem é imediata: “em todos os lugares e em lugar nenhum”. Andando ao acaso, não é raro ver, sob um prédio ou num canto de calçada, ao abrigo do vento, uma família refugiada em volta de uma refeição frugal posta sobre jornais como se fossem guardanapos. Também se vê de vez em quando uma tenda com a sigla ACNUR (Alto Comissariado das Nações Unidas para Refugiados), erguida em um dos raros terrenos vagos da capital. O cenário descrito aponta para uma crise humanitária que é explicada pelo processo de: ',
                'resposta':{
                    
                }
            },

            'Pergunta 3':{

            }
        }

    return pontos

def pontuacao_final(pontos):

    if pontos == 0:
        print(emoji.emojize('Você foi muito mal :loudly_crying_face:'))

    if pontos == 1:
        print(emoji.emojize('Você está se familiarizando :confused_face:'))

    if pontos == 2:
        print(emoji.emojize('Na traveee :beaming_face_with_smiling_eyes:'))

    if pontos == 3:
        print(emoji.emojize('Parabéns, você merece estar em um nível maior! :nerd_face:'))


name = intro()
screen = nivel(name)
question = perguntas(screen)

