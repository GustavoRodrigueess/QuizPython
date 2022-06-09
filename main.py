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
                'pergunta':'Um dos principais tipos de migrações internacionais existentes é a chamada “fuga de cérebros”, que consiste:',
                'resposta':{
                    'A(c)':'no deslocamento em massa de profissionais especializados e de grande conhecimento para outros países.',
                    'B':'na perda de trabalhadores com baixa qualificação técnica para países estrangeiros, geralmente mais desenvolvidos',
                    'C':'na migração sazonal de pesquisadores universitários e estudantes, como em intercâmbios e cursos de capacitação'
                }
            },

            'Pergunta 2':{
                'pergunta':'Um dos principais traços da dinâmica demográfica mundial é a migração internacional, que recria conflitos espaciais de diferentes ordens. Esse tipo de migração é explicado',
                'resposta':{
                    'A':'pela facilidade do fluxo de trabalhadores condicionados pelos novos meios de comunicação e transportes',
                    'B':'pela incorporação de valores ocidentais no Oriente e de valores orientais no Ocidente, diminuindo as fronteiras simbólicas.',
                    'C(c)':'pelo aumento global do desemprego, que gera miséria nas nações de baixo índice de desenvolvimento humano'
                }
            },

            'Pergunta 3':{
                'pergunta':'“O desenvolvimento e o maior acesso ao transporte intercontinental, somados à facilidade de obtenção de informações sobre outros países por meio dos veículos de comunicação, impulsionaram o movimento de pessoas que buscam melhores condições de vida – nem sempre alcançadas fora do país de origem. Ao contrário do que se verifica com os fluxos econômicos, as fronteiras nacionais são reforçadas por governos de muitos países, principalmente dos desenvolvidos, para a entrada de imigrantes”. Um exemplo mundialmente reconhecido de restrição à entrada de imigrantes conforme mencionado no trecho entre aspas é:',
                'resposta':{
                    'A':'pela incorporação de valores ocidentais no Oriente e de valores orientais no Ocidente, diminuindo as fronteiras simbólicas',
                    'B':'pela aprendizagem de idiomas dos países ricos como forma de incorporação às novas demandas da indústria',
                    'C(c)':'pela facilidade do fluxo de trabalhadores condicionados pelos novos meios de comunicação e transportes'
                }
            }
        }

    if dificuldade == 2:
        print(emoji.emojize("\nEvoluir sempre, treine seus conhecimentos! :beaming_face_with_smiling_eyes:"))
        print("\nVamos começar!\n")

        perguntas = {
            'Pergunta 1':{
                'pergunta':'Os nomes científicos são extremamente importantes para a ciência, uma vez que permitem a identificação de um organismo independentemente da língua utilizada em um país. Isso é possível porque os nomes científicos:',
                'resposta':{
                    'A':'sempre são escritos em grego ou em palavras derivadas dessa língua',
                    'B':'sempre são escritos em português.',
                    'C(c)':'sempre são escritos em latim ou os termos são latinizados.'
                }
            },

            'Pergunta 2':{
                'pergunta':'Os nomes científicos apresentam algumas regras que devem ser seguidas no momento da escrita em um texto. Observe a seguir o nome científico do cajueiro e marque a alternativa em que todas as regras são obedecidas',
                'resposta':{
                    'A':'Anacardium Occidentale.',
                    'B(c)':'Anacardium occidentale/italico. ',
                    'C':'Anacardium Occidentale/italico.'
                }
            },

            'Pergunta 3':{
                'pergunta':'Quando escrevemos o nome de uma espécie, utilizamos normalmente dois termos: o gênero e o epíteto específico. Algumas vezes, no entanto, observamos a nomenclatura trinomial, como é o caso da ave: Haematopus ostralegus occidentalis. Nesse caso, temos um exemplo de:',
                'resposta':{
                    'A(c)':'subgênero.',
                    'B':'subreino.',
                    'C':'subespécie.'
                }
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
                    'B(c)':'conclusão da transição demográfica.',
                    'C':'contenção da entrada de imigrantes.',
                }
            },

            'Pergunta 2':{
                'pergunta':'Em Beirute, no Líbano, quando perguntado sobre onde se encontram os refugiados sírios, a resposta do homem é imediata: “em todos os lugares e em lugar nenhum”. Andando ao acaso, não é raro ver, sob um prédio ou num canto de calçada, ao abrigo do vento, uma família refugiada em volta de uma refeição frugal posta sobre jornais como se fossem guardanapos. Também se vê de vez em quando uma tenda com a sigla ACNUR (Alto Comissariado das Nações Unidas para Refugiados), erguida em um dos raros terrenos vagos da capital. O cenário descrito aponta para uma crise humanitária que é explicada pelo processo de: ',
                'resposta':{
                    'A':'desmobilização voluntária de militantes cooptados por seitas extremistas',
                    'B':'migração massiva de pessoas atingidas por catástrofe natural',
                    'C(c)':'desterritorialização forçada de populações afetadas por conflitos armados'
                }
            },

            'Pergunta 3':{
                'pergunta':'O desgaste acelerado sempre existirá se o agricultor não tiver o devido cuidado de combater as causas, relacionadas a vários processos, tais como: empobrecimento químico e lixiviação provocados pelo esgotamento causado pelas colheitas e pela lavagem vertical de nutrientes da água que se infiltra no solo, bem como pela retirada de elementos nutritivos com as colheitas. Os nutrientes retirados, quando não repostos, são comumente substituídos por elementos tóxicos, como, por exemplo, o alumínio. A dinâmica ambiental exemplificada no texto gera a seguinte consequência para o solo agricultável',
                'resposta':{
                    'A(c)':'Elevação da acidez',
                    'B':'Ampliação da salinidade',
                    'C':'Formação de voçorocas',
                }
            }
        }

    for pk, pv in perguntas.items():
        print(f'{pk}: {pv["pergunta"]}')

        print('Respostas: ')
        for rk, rv in pv['resposta'].items():
            print(f'[{rk}]: {rv}')

        print()


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

