# Remédio em Dia CLI

## Descrição

O Remédio em Dia CLI é uma aplicação desenvolvida em python para auxiliar usuários no controle de medicamentos por meio de uma interface  de linha de comando.

O sistema permite cadastrar medicamentos, consultar informações de endereço através da API ViaCEP, registrar medicamentos tomados e visualizar doses pendentes.

Os dados são armazenados em um banco de dados em nuvem utilizando Supabase.

---

## Problema

Muitas pessoas esquecem de tomar medicamentos nos horários corretos, o que pode comprometer tratamentos médicos e reduzir a eficácia dos medicamentos.

---

## Solução

A aplicação oferece uma forma simples de registrar medicamentos e acompanhar o tratamento diretamente pelo terminal, armazenando os dados de forma segura em um banco de dados na nuvem.

---

## Funcionalidades

* Cadastro de medicamentos
* Listagem de medicamentos
* Marcação de medicamento como tomado
* Visualização de medicamentos pendentes
* Consulta de endereço por CEP utilizando ViaCEP
* Armazenamento de dados em banco de dados Supabase
* Testes automatizados com Pytest
* Verificação de qualidade com Ruff
* Integração contínua com GitHub Actions

---

## Tecnologias Utilizadas

* Python 3.13
* Supabase
* PostgreSQL
* ViaCEP API
* Pytest
* Ruff
* GitHub Actions

---

## Estrutura do Projeto

app/

* main.py
* services.py
* storage.py
* models.py
* consulta_cep.py

testes/

* test_models.py
* test_services.py
* test_consulta_cep.py

---

## Configuração do Ambiente

Instale as dependências:

```bash
pip install -r requirements.txt
```

Crie um arquivo `.env` na raiz do projeto:

```env
SUPABASE_URL=sua_url_do_supabase
SUPABASE_KEY=sua_chave_do_supabase
```

---

## Como Executar

```bash
python -m app.main
```

---

## Executar Testes

```bash
pytest
```

---

## Executar Verificação de Código

```bash
ruff check .
```

---

## Integração Contínua

O projeto utiliza GitHub Actions para executar automaticamente:

* Testes com Pytest
* Verificação de código com Ruff

Sempre que alterações são enviadas para o repositório.

---

## Autor

Nicolas David Lopes Monteiro

Projeto desenvolvido como atividade final do Bootcamp.

Atualizado para entrega final do bootcamp.