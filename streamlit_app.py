import streamlit as st
from app.storage import carregar_dados, inserir_medicamento

st.title("Remédio em Dia")

st.header("Cadastrar medicamento")

nome = st.text_input("Nome")
dose = st.text_input("Dose")
horario = st.text_input("Horário")
dias = st.number_input("Dias", min_value=1, step=1)

if st.button("Cadastrar"):
    medicamento = {
        "nome": nome,
        "dose": dose,
        "horario": horario,
        "dias": dias,
        "tomado": False
    }

    inserir_medicamento(medicamento)
    st.success("Medicamento cadastrado!")

st.header("Medicamentos cadastrados")

dados = carregar_dados()

if dados:
    st.dataframe(dados)
else:
    st.info("Nenhum medicamento cadastrado.")