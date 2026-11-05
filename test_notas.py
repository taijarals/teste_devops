from notas import calcular_media, situacao

#• assert significa "garanto que isto é verdade". Se a comparação der falso, o teste falha.


def test_media_simples():
    assert calcular_media(7, 8, 9) == 8.0


def test_media_arredonda():
    assert calcular_media(7, 7, 8) == 7.3


def test_aprovado():
    assert situacao(7.0) == "Aprovado"


def test_recuperacao():
    assert situacao(5.5) == "Recuperação"


def test_reprovado():
    assert situacao(4.9) == "Reprovado"