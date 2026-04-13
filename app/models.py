class Medicamento:
    def __init__(self, nome, dose, horario, dias, tomado=False):
        self.nome = nome
        self.dose = dose
        self.horario = horario
        self.dias = dias
        self.tomado = tomado

    def to_dict(self):
        return {
            "nome": self.nome,
            "dose": self.dose,
            "horario": self.horario,
            "dias": self.dias,
            "tomado": self.tomado
        }