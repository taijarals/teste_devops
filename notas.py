def calcular_media(av1, av2, av3):
    #Calcula a média das três avaliações, com uma casa decimal.
    return round((av1 + av2 + av3) / 3, 1)


def situacao(media):
    #Diz a situação do aluno a partir da média.
    if media > 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"