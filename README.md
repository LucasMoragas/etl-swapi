# ETL SWAPI

## Ingestão e Tratamento de Dados da API

O objetivo geral deste script é realizar a ingestão de dados de uma API, criar arquivos CSV com os dados brutos e, em seguida, padronizar e salvar os dados tratados em outro diretório.

### Passos:

1. **Ingestão de Dados da API:**
   - A API é paginada, e para este exercício, vamos fazer a ingestão das 5 primeiras páginas.
   - As bases de dados (people, planets, films) devem ser salvas na pasta "raw" em formato CSV.

2. **Tratamento dos Dados:**
   - Para cada base de dados (people, planets, films), realizar os seguintes tratamentos:
     a. Padronização de strings para lower case.
     b. Remoção de caracteres especiais.

3. **Salvamento dos Dados Tratados:**
   - As bases finais, após a aplicação dos tratamentos do item 2, devem ser salvas na pasta "work" em formato CSV.
