# questions.py
# Estrutura: lista de dicionários com "id", "texto", "alternativas" (map alternativa->valor),
# e flags indicando se precisa campo aberto ou julgamento profissional.

QUESTOES = [
    {
        "id": 1,
        "texto": "1 - Paciente Desempregado",
        "alternativas": {"A": 1, "B": 1, "C": -1},
        "labels": {"A": "Não", "B": "Sim, mas possui fonte de renda fixa ou variável", "C": "Sim e não possui fonte de renda fixa ou variável"},
        "barreira_if": ["C"],
        "facilitador_if": ["A", "B"]
    },
    {
        "id": 2,
        "texto": "2 - Paciente possui diagnóstico de depressão no prontuário de saúde?",
        "alternativas": {"A": 0, "B": 0, "C": -1},
        "labels": {"A": "Não", "B": "Não há acesso à essa informação", "C": "Sim"},
        "barreira_if": ["C"],
        "facilitador_if": []
    },
    {
        "id": 3,
        "texto": "3 - Por qual motivo você utiliza o medicamento? (resposta aberta)",
        "alternativas": {},  # pontuação depende do julgamento do profissional
        "open_field": True,
        "requires_judgement": True,  # profissional deve marcar correto/incorreto
        "barreira_if": ["INCORRETO"],
        "facilitador_if": ["CORRETO"]
    },
    {
        "id": 4,
        "texto": "4 - Você convive com pessoas em seu ambiente familiar que te incentivam a utilizar seu(s) medicamento(s)?",
        "alternativas": {"A": -1, "B": 1, "C": -1},
        "labels": {"A": "Não, eu moro sozinho.", "B": "Sim, eu moro com familiares que me incentivam a utilizar o medicamento.", "C": "Não, apesar de morar com familiares eles não me incentivam a utilizar o medicamento."},
        "barreira_if": ["A", "C"],
        "facilitador_if": ["B"]
    },
    {
        "id": 5,
        "texto": "5 - Você participa de alguma associação (grupos) de pessoas com doenças semelhantes à sua?",
        "alternativas": {"A": 1, "B": -1},
        "labels": {"A": "Sim", "B": "Não"},
        "barreira_if": ["B"],
        "facilitador_if": ["A"]
    },
    {
        "id": 6,
        "texto": "6 - Nos últimos sete dias você passou por algum problema que te causou tristeza ou desanimo?",
        "alternativas": {"A": -1, "B": 0},
        "labels": {"A": "Sim", "B": "Não"},
        "barreira_if": ["A"],
        "facilitador_if": []
    },
    {
        "id": 7,
        "texto": "7 - Quantos anos você estudou? Sabe ler e escrever? (campo aberto + julgamento)",
        "alternativas": {},  # depende do input e do julgamento profissional
        "open_field": True,
        "requires_judgement": True,
        "barreira_if": ["ANALFABETO"],
        "facilitador_if": ["ALFABETIZADO"]
    },
    {
        "id": 8,
        "texto": "8 - Qual a sua idade? (campo aberto + escolha <60 ou >=60)",
        "alternativas": {"A": -1, "B": 1},
        "labels": {"A": "Paciente com idade inferior a 60 anos.", "B": "Paciente com idade igual ou superior a 60 anos"},
        "open_field": True,
        "barreira_if": ["A"],
        "facilitador_if": ["B"]
    },
    {
        "id": 9,
        "texto": "9 - Você tem alguma complicação ou problema de saúde causado pela sua doença?",
        "alternativas": {"A": 1, "B": 0, "C": 0},
        "labels": {"A": "Sim", "B": "Não", "C": "Não sei"},
        "barreira_if": [],
        "facilitador_if": ["A"]
    },
    {
        "id": 10,
        "texto": "10 - Você é cuidador de um familiar que tenha alguma doença crônica?",
        "alternativas": {"A": -1, "B": 0},
        "labels": {"A": "Sim", "B": "Não"},
        "barreira_if": ["A"],
        "facilitador_if": []
    },
    {
        "id": 11,
        "texto": "11 - Nos últimos 7 dias, você deixou de tomar alguma dose do medicamento?",
        "alternativas": {"A": -1, "B": -1, "C": 0, "D": 1, "E": 1},
        "labels": {"A": "Quase todos os dias eu esqueço", "B": "Esqueci alguns dias", "C": "Esqueci apenas um dia", "D": "É bem difícil esquecer", "E": "Eu nunca esqueço"},
        "barreira_if": ["A", "B"],
        "facilitador_if": ["D", "E"]
    },
    {
        "id": 12,
        "texto": "12 - Você tem conhecimento sobre a gravidade da sua doença?",
        "alternativas": {"A": -1, "B": 0, "C": 1},
        "labels": {"A": "Não tenho conhecimento", "B": "Nunca me preocupei", "C": "Tenho conhecimento"},
        "barreira_if": ["A"],
        "facilitador_if": ["C"]
    },
    {
        "id": 13,
        "texto": "13 - Nos últimos 7 dias, você se sentiu interessado em cuidar da sua doença?",
        "alternativas": {"A": -1, "B": 0, "C": 1},
        "labels": {"A": "Não tive interesse", "B": "Nunca me preocupei", "C": "Tive interesse"},
        "barreira_if": ["A"],
        "facilitador_if": ["C"]
    },
    {
        "id": 14,
        "texto": "14 - Como tem sido a sua aceitação com relação à sua condição de saúde?",
        "alternativas": {"A": -1, "B": -1, "C": 1},
        "labels": {"A": "Dificuldade em aceitar", "B": "Eu não sei que tenho essa condição", "C": "Eu aceito ter essa condição"},
        "barreira_if": ["A", "B"],
        "facilitador_if": ["C"]
    },
    {
        "id": 15,
        "texto": "15 - Em situações fora da rotina, você costuma utilizar o medicamento?",
        "alternativas": {"A": 1, "B": 0, "C": 0},
        "labels": {"A": "Costumo utilizar", "B": "Não lembro", "C": "Não costumo utilizar"},
        "barreira_if": [],
        "facilitador_if": ["A"]
    },
    {
        "id": 16,
        "texto": "16 - Quando você se sente melhor, costuma parar de utilizar o medicamento?",
        "alternativas": {"A": -1, "B": 1, "C": 0},
        "labels": {"A": "Costumo parar", "B": "Não lembro se costumo parar", "C": "Não costumo parar"},
        "barreira_if": ["A"],
        "facilitador_if": ["B"]
    },
    {
        "id": 17,
        "texto": "17 - Você precisou comprar o medicamento nos últimos 30 dias?",
        "alternativas": {"A": 0, "B": 1, "C": 0, "D": 0},
        "labels": {"A": "Não recebi gratuitamente e precisei comprar", "B": "Recebi gratuitamente e não precisei comprar", "C": "Recebi gratuitamente e também precisei comprar", "D": "Não recebi gratuitamente e não comprei"},
        "barreira_if": [],
        "facilitador_if": ["B"]
    },
    {
        "id": 18,
        "texto": "18 - Você considera alto o custo com o medicamento?",
        "alternativas": {"A": -1, "B": 0, "C": 1},
        "labels": {"A": "Sim", "B": "Não sei", "C": "Não"},
        "barreira_if": ["A"],
        "facilitador_if": ["C"]
    },
    {
        "id": 19,
        "texto": "19 - Qual a sua opinião em relação a quantidade de medicamentos que você toma?",
        "alternativas": {"A": -1, "B": 1, "C": -1},
        "labels": {"A": "Acho que uso muitos", "B": "Acho que uso quantidade suficiente", "C": "Acho que uso poucos"},
        "barreira_if": ["A", "C"],
        "facilitador_if": ["B"]
    },
    {
        "id": 20,
        "texto": "20 - Você tem dificuldade ou desconforto ao tomar ou aplicar o medicamento?",
        "alternativas": {"A": 0, "B": -1},
        "labels": {"A": "Não tenho dificuldades", "B": "Tenho dificuldades"},
        "barreira_if": ["B"],
        "facilitador_if": []
    },
    {
        "id": 21,
        "texto": "21 - O que você acha que o medicamento faz para a sua saúde?",
        "alternativas": {"A": 1, "B": 0, "C": -1},
        "labels": {"A": "Me faz bem", "B": "Não me faz bem nem mal", "C": "Me faz mal"},
        "barreira_if": ["C"],
        "facilitador_if": ["A"]
    },
    {
        "id": 22,
        "texto": "22 - Você considera importante utilizar o medicamento para controlar o seu problema de saúde?",
        "alternativas": {"A": 1, "B": 0, "C": -1},
        "labels": {"A": "Importante", "B": "Prefiro não opinar", "C": "Não é importante"},
        "barreira_if": ["C"],
        "facilitador_if": ["A"]
    },
    {
        "id": 23,
        "texto": "23 - Utilizar o medicamento atrapalha as suas atividades do dia a dia?",
        "alternativas": {"A": -1, "B": 1},
        "labels": {"A": "Sim", "B": "Não"},
        "barreira_if": ["A"],
        "facilitador_if": ["B"]
    },
    {
        "id": 24,
        "texto": "24 - Você esteve de acordo com o seu médico quando ele te receitou o medicamento?",
        "alternativas": {"A": 1, "B": 0, "C": -1},
        "labels": {"A": "Concordei", "B": "Não fui esclarecido", "C": "Não concordei"},
        "barreira_if": ["C"],
        "facilitador_if": ["A"]
    },
    {
        "id": 25,
        "texto": "25 - Você está satisfeito com o atendimento recebido pelo profissional de saúde que te receitou esse medicamento?",
        "alternativas": {"A": 1, "B": 0, "C": 0},
        "labels": {"A": "Estou satisfeito", "B": "Prefiro não opinar", "C": "Não estou satisfeito"},
        "barreira_if": [],
        "facilitador_if": ["A"]
    },
    {
        "id": 26,
        "texto": "26 - Você considera que recebeu todas as informações necessárias sobre o medicamento pelo profissional de saúde?",
        "alternativas": {"A": 1, "B": 0, "C": -1},
        "labels": {"A": "Sim", "B": "Não sei", "C": "Não"},
        "barreira_if": ["C"],
        "facilitador_if": ["A"]
    },
    {
        "id": 27,
        "texto": "27 - Você confia no profissional de saúde que te receitou o medicamento?",
        "alternativas": {"A": 1, "B": 0, "C": -1},
        "labels": {"A": "Confio", "B": "Prefiro não opinar", "C": "Não confio"},
        "barreira_if": ["C"],
        "facilitador_if": ["A"]
    },
    {
        "id": 28,
        "texto": "28 - O profissional de saúde que te receitou te motiva a utilizar esse medicamento?",
        "alternatives_note": "a/b/c",
        "alternativas": {"A": 1, "B": 0, "C": 0},
        "labels": {"A": "Sim", "B": "Prefiro não opinar", "C": "Não"},
        "barreira_if": [],
        "facilitador_if": ["A"]
    },
    {
        "id": 29,
        "texto": "29 - Você considera que está acostumado a utilizar o medicamento?",
        "alternativas": {"A": 1, "B": 0, "C": 0},
        "labels": {"A": "Estou acostumado", "B": "Não estou acostumado", "C": "Prefiro não opinar"},
        "barreira_if": [],
        "facilitador_if": ["A"]
    }
]

# Observação: use QUESTOES como fonte única para gerar formulários e calcular escores.
