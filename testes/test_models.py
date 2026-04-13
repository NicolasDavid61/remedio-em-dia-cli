from app.models import Medicamento

def test_medicamento_to_dict():
    med = Medicamento("Dipirona", "500mg", "08:00", "5")
    resultado = med.to_dict()

    assert resultado["nome"] == "Dipirona"
    assert resultado["dose"] == "500mg"
    assert resultado["horario"] == "08:00"
    assert resultado["dias"] == "5"
    assert resultado["tomado"] is False