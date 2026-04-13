from app.models import Medicamento
from app.storage import carregar_dados, salvar_dados

def validar_horario(horario):
    try:
        partes = horario.split(":")
        if len(partes) != 2:
            return False
        hora = int(partes[0])
        minuto = int(partes[1])
        return 0 <= hora <= 23 and 0 <= minuto <= 59
    except ValueError:
        return False

def cadastrar_medicamento(nome, dose, horario, dias):
    if not validar_horario(horario):
        print("Horário inválido.")
        return

    dados = carregar_dados()
    medicamento = Medicamento(nome, dose, horario, dias)
    dados.append(medicamento.to_dict())
    salvar_dados(dados)
    print("Medicamento cadastrado com sucesso.")

def listar_medicamentos():
    dados = carregar_dados()

    if not dados:
        print("Nenhum medicamento cadastrado.")
        return

    for med in dados:
        status = "Tomado" if med["tomado"] else "Pendente"
        print(f'Nome: {med["nome"]} | Dose: {med["dose"]} | Horário: {med["horario"]} | Dias: {med["dias"]} | Status: {status}')

def marcar_como_tomado(nome):
    dados = carregar_dados()

    for med in dados:
        if med["nome"].lower() == nome.lower():
            med["tomado"] = True
            salvar_dados(dados)
            print("Medicamento marcado como tomado.")
            return

    print("Medicamento não encontrado.")

def ver_pendentes():
    dados = carregar_dados()
    pendentes = [med for med in dados if not med["tomado"]]

    if not pendentes:
        print("Nenhuma dose pendente.")
        return

    for med in pendentes:
        print(f'Nome: {med["nome"]} | Dose: {med["dose"]} | Horário: {med["horario"]}')