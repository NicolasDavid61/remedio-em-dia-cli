import requests

def buscar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    
    try:
        resposta = requests.get(url)

        if resposta.status_code == 200:
            dados = resposta.json()

            if "erro" in dados:
                return "CEP não encontrado."

            return {
                "rua": dados.get("logradouro"),
                "bairro": dados.get("bairro"),
                "cidade": dados.get("localidade"),
                "estado": dados.get("uf")
            }

        return "Erro na API."

    except:
        return "Erro na requisição."