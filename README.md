# Remédio em Dia CLI

## Descrição
Aplicação em Python com interface de linha de comando para ajudar no controle de medicamentos.

## Problema
Muitas pessoas esquecem de tomar medicamentos nos horários corretos, o que pode comprometer tratamentos de saúde.

## Solução
O sistema permite cadastrar medicamentos, listar itens cadastrados, marcar doses como tomadas e visualizar doses pendentes.

## Funcionalidades
- Cadastro de medicamentos
- Listagem de medicamentos
- Marcação de dose como tomada
- Visualização de doses pendentes
- Armazenamento em JSON
- Testes automatizados
- Linting
- Integração contínua com GitHub Actions

## Tecnologias utilizadas
- Python
- JSON
- Pytest
- Ruff
- GitHub Actions

## Como executar
```bash
python -m app.main

## Entrega Intermediária

Nesta etapa do projeto foi implementada integração com API pública.

### API utilizada
ViaCEP

### Funcionalidades adicionadas

- Consulta de endereço por CEP
- Retorno automático de rua, bairro, cidade e estado
- Teste automatizado com pytest

### Como executar

Instalar dependências:

pip install -r requirements.txt

Executar aplicação:

python app/main.py

Executar testes:

pytest