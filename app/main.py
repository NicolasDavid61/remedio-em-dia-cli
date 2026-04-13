from app.services import (
    cadastrar_medicamento,
    listar_medicamentos,
    marcar_como_tomado,
    ver_pendentes
)

def menu():
    while True:
        print("\n=== REMÉDIO EM DIA CLI ===")
        print("1 - Cadastrar medicamento")
        print("2 - Listar medicamentos")
        print("3 - Marcar dose como tomada")
        print("4 - Ver doses pendentes")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do medicamento: ")
            dose = input("Dose: ")
            horario = input("Horário (HH:MM): ")
            dias = input("Quantidade de dias: ")
            cadastrar_medicamento(nome, dose, horario, dias)

        elif opcao == "2":
            listar_medicamentos()

        elif opcao == "3":
            nome = input("Nome do medicamento para marcar como tomado: ")
            marcar_como_tomado(nome)

        elif opcao == "4":
            ver_pendentes()

        elif opcao == "0":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()