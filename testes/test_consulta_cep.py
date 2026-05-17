from app.consulta_cep import buscar_cep

def test_buscar_cep():
    resultado = buscar_cep("01001000")

    assert resultado["cidade"] == "São Paulo"