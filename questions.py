QUESTOES = [
    {
        "id": 1,
        "texto": "Paciente Desempregado",
        "alternativas": {"A": 1, "B": 1, "C": -1},
        "labels": {
            "A": "Não",
            "B": "Sim, mas possui fonte de renda fixa ou variável",
            "C": "Sim e não possui fonte de renda fixa ou variável"
        },
        "barreira_if": ["C"],
        "facilitador_if": ["A", "B"],
        "classificacao_texto": {
            "C": "Desemprego sem fonte de renda",
            "A": "Estabilidade financeira",
            "B": "Fonte de renda apesar do desemprego"
        }
    },
    {
        "id": 2,
        "texto": "Paciente possui diagnóstico de depressão no prontuário de saúde?",
        "alternativas": {"A": 0, "B": 0, "C": -1},
        "labels": {
            "A": "Não",
            "B": "Não há acesso à essa informação",
            "C": "Sim"
        },
        "barreira_if": ["C"],
        "facilitador_if": [],
        "classificacao_texto": {
            "C": "Presença de depressão diagnosticada"
        }
    },
    {
        "id": 3,
        "texto": "Por qual motivo você utiliza o medicamento? (resposta aberta)",
        "open_field": True,
        "requires_judgement": True,
        "barreira_if": ["INCORRETO"],
        "facilitador_if": ["CORRETO"],
        "classificacao_texto": {
            "INCORRETO": "Uso do medicamento sem compreensão do benefício terapêutico",
            "CORRETO": "Reconhecimento do benefício terapêutico"
        }
    },
    {
        "id": 4,
        "texto": "Você convive com pessoas em seu ambiente familiar que te incentivam a utilizar seu(s) medicamento(s)?",
        "alternativas": {"A": -1, "B": 1, "C": -1},
        "labels": {
            "A": "Não, eu moro sozinho.",
            "B": "Sim, eu moro com familiares que me incentivam a utilizar o medicamento.",
            "C": "Não, apesar de morar com familiares eles não me incentivam a utilizar o medicamento."
        },
        "barreira_if": ["A", "C"],
        "facilitador_if": ["B"],
        "classificacao_texto": {
            "A": "Ausência de suporte familiar",
            "C": "Falta de incentivo familiar",
            "B": "Presença de suporte familiar"
        }
    },
    {
        "id": 5,
        "texto": "Você participa de alguma associação (grupos) de pessoas com doenças semelhantes à sua?",
        "alternativas": {"A": 1, "B": -1},
        "labels": {"A": "Sim", "B": "Não"},
        "barreira_if": ["B"],
        "facilitador_if": ["A"],
        "classificacao_texto": {
            "A": "Participação em grupos de apoio",
            "B": "Ausência de apoio social estruturado"
        }
    },
    {
        "id": 6,
        "texto": "Nos últimos sete dias você passou por algum problema que te causou tristeza ou desânimo?",
        "alternativas": {"A": -1, "B": 0},
        "labels": {"A": "Sim", "B": "Não"},
        "barreira_if": ["A"],
        "facilitador_if": [],
        "classificacao_texto": {
            "A": "Sintomas emocionais recentes"
        }
    },
    {
        "id": 7,
        "texto": "Quantos anos você estudou? Sabe ler e escrever?",
        "open_field": True,
        "requires_judgement": True,
        "barreira_if": ["ANALFABETO"],
        "facilitador_if": ["ALFABETIZADO"],
        "classificacao_texto": {
            "ANALFABETO": "Baixa escolaridade / analfabetismo",
            "ALFABETIZADO": "Capacidade de leitura e escrita"
        }
    },
    {
        "id": 8,
        "texto": "Qual a sua idade?",
        "alternativas": {"A": -1, "B": 1},
        "labels": {
            "A": "Paciente com idade inferior a 60 anos",
            "B": "Paciente com idade igual ou superior a 60 anos"
        },
        "barreira_if": ["A"],
        "facilitador_if": ["B"],
        "classificacao_texto": {
            "A": "Faixa etária adulta",
            "B": "Idoso"
        }
    },
    {
        "id": 9,
        "texto": "Você tem alguma complicação ou problema de saúde causado pela sua doença?",
        "alternativas": {"A": 1, "B": 0, "C": 0},
        "labels": {"A": "Sim", "B": "Não", "C": "Não sei"},
        "barreira_if": [],
        "facilitador_if": ["A"],
        "classificacao_texto": {
            "A": "Reconhecimento de complicações da doença"
        }
    },
    {
        "id": 10,
        "texto": "Você é cuidador de um familiar que tenha alguma doença crônica?",
        "alternativas": {"A": -1, "B": 0},
        "labels": {"A": "Sim", "B": "Não"},
        "barreira_if": ["A"],
        "facilitador_if": [],
        "classificacao_texto": {
            "A": "Sobrecarga de cuidado familiar"
        }
    },

    {
        "id": 11,
        "texto": "Nos últimos 7 dias, você deixou de tomar alguma dose do medicamento?",
        "alternativas": {"A": -1, "B": -1, "C": 0, "D": 1, "E": 1},
        "labels": {
            "A": "Quase todos os dias eu esqueço",
            "B": "Esqueci alguns dias",
            "C": "Esqueci apenas um dia",
            "D": "É bem difícil esquecer",
            "E": "Eu nunca esqueço"
        },
        "barreira_if": ["A", "B"],
        "facilitador_if": ["D", "E"],
        "classificacao_texto": {
            "A": "Esquecimento frequente",
            "B": "Esquecimento ocasional",
            "D": "Boa adesão ao tratamento",
            "E": "Excelente adesão ao tratamento"
        }
    },

    {
        "id": 12,
        "texto": "Você tem conhecimento sobre a gravidade da sua doença?",
        "alternativas": {"A": -1, "B": 0, "C": 1},
        "labels": {
            "A": "Não tenho conhecimento",
            "B": "Nunca me preocupei",
            "C": "Tenho conhecimento"
        },
        "barreira_if": ["A"],
        "facilitador_if": ["C"],
        "classificacao_texto": {
            "A": "Desconhecimento da gravidade da doença",
            "C": "Consciência sobre a gravidade da doença"
        }
    },

    {
        "id": 13,
        "texto": "Nos últimos 7 dias, você se sentiu interessado em cuidar da sua doença?",
        "alternativas": {"A": -1, "B": 0, "C": 1},
        "labels": {
            "A": "Não tive interesse",
            "B": "Nunca me preocupei",
            "C": "Tive interesse"
        },
        "barreira_if": ["A"],
        "facilitador_if": ["C"],
        "classificacao_texto": {
            "A": "Baixo interesse no autocuidado",
            "C": "Engajamento no autocuidado"
        }
    },

    {
        "id": 14,
        "texto": "Como tem sido a sua aceitação com relação à sua condição de saúde?",
        "alternativas": {"A": -1, "B": -1, "C": 1},
        "labels": {
            "A": "Dificuldade em aceitar",
            "B": "Eu não sei que tenho essa condição",
            "C": "Eu aceito ter essa condição"
        },
        "barreira_if": ["A", "B"],
        "facilitador_if": ["C"],
        "classificacao_texto": {
            "A": "Dificuldade de aceitação da doença",
            "B": "Negação da condição de saúde",
            "C": "Aceitação da condição de saúde"
        }
    },

    {
        "id": 15,
        "texto": "Em situações fora da rotina, você costuma utilizar o medicamento?",
        "alternativas": {"A": 1, "B": 0, "C": 0},
        "labels": {
            "A": "Costumo utilizar",
            "B": "Não lembro",
            "C": "Não costumo utilizar"
        },
        "barreira_if": [],
        "facilitador_if": ["A"],
        "classificacao_texto": {
            "A": "Manutenção do tratamento fora da rotina"
        }
    },

    {
        "id": 16,
        "texto": "Quando você se sente melhor, costuma parar de utilizar o medicamento?",
        "alternativas": {"A": -1, "B": 1, "C": 0},
        "labels": {
            "A": "Costumo parar",
            "B": "Não lembro se costumo parar",
            "C": "Não costumo parar"
        },
        "barreira_if": ["A"],
        "facilitador_if": ["B"],
        "classificacao_texto": {
            "A": "Interrupção do tratamento ao melhorar",
            "B": "Continuidade do tratamento"
        }
    },

    {
        "id": 17,
        "texto": "Você precisou comprar o medicamento nos últimos 30 dias?",
        "alternativas": {"A": 0, "B": 1, "C": 0, "D": 0},
        "labels": {
            "A": "Não recebi gratuitamente e precisei comprar",
            "B": "Recebi gratuitamente e não precisei comprar",
            "C": "Recebi gratuitamente e também precisei comprar",
            "D": "Não recebi gratuitamente e não comprei"
        },
        "barreira_if": [],
        "facilitador_if": ["B"],
        "classificacao_texto": {
            "B": "Acesso gratuito ao medicamento"
        }
    },

    {
        "id": 18,
        "texto": "Você considera alto o custo com o medicamento?",
        "alternativas": {"A": -1, "B": 0, "C": 1},
        "labels": {
            "A": "Sim",
            "B": "Não sei",
            "C": "Não"
        },
        "barreira_if": ["A"],
        "facilitador_if": ["C"],
        "classificacao_texto": {
            "A": "Alto custo do medicamento",
            "C": "Custo acessível do medicamento"
        }
    },

    {
        "id": 19,
        "texto": "Qual a sua opinião em relação à quantidade de medicamentos que você toma?",
        "alternativas": {"A": -1, "B": 1, "C": -1},
        "labels": {
            "A": "Acho que uso muitos",
            "B": "Acho que uso quantidade suficiente",
            "C": "Acho que uso poucos"
        },
        "barreira_if": ["A", "C"],
        "facilitador_if": ["B"],
        "classificacao_texto": {
            "A": "Percepção de polifarmácia",
            "C": "Percepção de subtratamento",
            "B": "Percepção adequada do tratamento"
        }
    },

    {
        "id": 20,
        "texto": "Você tem dificuldade ou desconforto ao tomar ou aplicar o medicamento?",
        "alternativas": {"A": 0, "B": -1},
        "labels": {
            "A": "Não tenho dificuldades",
            "B": "Tenho dificuldades"
        },
        "barreira_if": ["B"],
        "facilitador_if": [],
        "classificacao_texto": {
            "B": "Dificuldade na administração do medicamento"
        }
    },

    {
        "id": 21,
        "texto": "O que você acha que o medicamento faz para a sua saúde?",
        "alternativas": {"A": 1, "B": 0, "C": -1},
        "labels": {
            "A": "Me faz bem",
            "B": "Não me faz bem nem mal",
            "C": "Me faz mal"
        },
        "barreira_if": ["C"],
        "facilitador_if": ["A"],
        "classificacao_texto": {
            "C": "Percepção negativa do medicamento",
            "A": "Percepção positiva do medicamento"
        }
    },

    {
        "id": 22,
        "texto": "Você considera importante utilizar o medicamento para controlar o seu problema de saúde?",
        "alternativas": {"A": 1, "B": 0, "C": -1},
        "labels": {
            "A": "Importante",
            "B": "Prefiro não opinar",
            "C": "Não é importante"
        },
        "barreira_if": ["C"],
        "facilitador_if": ["A"],
        "classificacao_texto": {
            "C": "Baixa valorização do tratamento",
            "A": "Valorização do tratamento medicamentoso"
        }
    },

    {
        "id": 23,
        "texto": "Utilizar o medicamento atrapalha as suas atividades do dia a dia?",
        "alternativas": {"A": -1, "B": 1},
        "labels": {
            "A": "Sim",
            "B": "Não"
        },
        "barreira_if": ["A"],
        "facilitador_if": ["B"],
        "classificacao_texto": {
            "A": "Interferência do medicamento na rotina",
            "B": "Boa adaptação do medicamento à rotina"
        }
    },

    {
        "id": 24,
        "texto": "Você esteve de acordo com o seu médico quando ele te receitou o medicamento?",
        "alternativas": {"A": 1, "B": 0, "C": -1},
        "labels": {
            "A": "Concordei",
            "B": "Não fui esclarecido",
            "C": "Não concordei"
        },
        "barreira_if": ["C"],
        "facilitador_if": ["A"],
        "classificacao_texto": {
            "C": "Discordância com a prescrição médica",
            "A": "Concordância com a prescrição médica"
        }
    },

    {
        "id": 25,
        "texto": "Você está satisfeito com o atendimento recebido pelo profissional de saúde que te receitou esse medicamento?",
        "alternativas": {"A": 1, "B": 0, "C": 0},
        "labels": {
            "A": "Estou satisfeito",
            "B": "Prefiro não opinar",
            "C": "Não estou satisfeito"
        },
        "barreira_if": [],
        "facilitador_if": ["A"],
        "classificacao_texto": {
            "A": "Satisfação com o atendimento em saúde"
        }
    },

    {
        "id": 26,
        "texto": "Você considera que recebeu todas as informações necessárias sobre o medicamento pelo profissional de saúde?",
        "alternativas": {"A": 1, "B": 0, "C": -1},
        "labels": {
            "A": "Sim",
            "B": "Não sei",
            "C": "Não"
        },
        "barreira_if": ["C"],
        "facilitador_if": ["A"],
        "classificacao_texto": {
            "C": "Informação insuficiente sobre o medicamento",
            "A": "Informação adequada sobre o medicamento"
        }
    },

    {
        "id": 27,
        "texto": "Você confia no profissional de saúde que te receitou o medicamento?",
        "alternativas": {"A": 1, "B": 0, "C": -1},
        "labels": {
            "A": "Confio",
            "B": "Prefiro não opinar",
            "C": "Não confio"
        },
        "barreira_if": ["C"],
        "facilitador_if": ["A"],
        "classificacao_texto": {
            "C": "Baixa confiança no profissional de saúde",
            "A": "Confiança no profissional de saúde"
        }
    },

    {
        "id": 28,
        "texto": "O profissional de saúde que te receitou te motiva a utilizar esse medicamento?",
        "alternativas": {"A": 1, "B": 0, "C": 0},
        "labels": {
            "A": "Sim",
            "B": "Prefiro não opinar",
            "C": "Não"
        },
        "barreira_if": [],
        "facilitador_if": ["A"],
        "classificacao_texto": {
            "A": "Motivação fornecida pelo profissional de saúde"
        }
    },

    {
        "id": 29,
        "texto": "Você considera que está acostumado a utilizar o medicamento?",
        "alternativas": {"A": 1, "B": 0, "C": 0},
        "labels": {
            "A": "Estou acostumado",
            "B": "Não estou acostumado",
            "C": "Prefiro não opinar"
        },
        "barreira_if": [],
        "facilitador_if": ["A"],
        "classificacao_texto": {
            "A": "Familiaridade com o uso do medicamento"
        }
    }
]
