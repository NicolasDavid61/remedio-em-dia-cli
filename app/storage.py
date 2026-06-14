from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


def carregar_dados():
    resposta = supabase.table("medicamentos").select("*").execute()
    return resposta.data


def inserir_medicamento(medicamento):
    supabase.table("medicamentos").insert(medicamento).execute()


def atualizar_medicamento(nome):
    supabase.table("medicamentos")\
        .update({"tomado": True})\
        .eq("nome", nome)\
        .execute()