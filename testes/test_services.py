from app.services import validar_horario

def test_validar_horario_valido():
    assert validar_horario("08:30") is True

def test_validar_horario_invalido():
    assert validar_horario("25:99") is False

def test_validar_horario_formato_errado():
    assert validar_horario("8h30") is False