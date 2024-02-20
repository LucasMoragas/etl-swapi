import pandas as pd
import re

#Função de remoção de caracteres especiais
def removeCaracteres(text):
    if isinstance(text, str):
        return re.sub(r'[^\w\s]', '', text)
    return text

#Gerando os DataFrames
peopleDataFrame = pd.read_csv('src/raw/people.csv')
planetsDataFrame = pd.read_csv('src/raw/planets.csv')
filmsDataFrame = pd.read_csv('src/raw/films.csv')

#Aplicando a função de remoção em todos os itens dos DataFrames
peopleWork = peopleDataFrame.applymap(removeCaracteres)
planetsWork = planetsDataFrame.applymap(removeCaracteres)
filmsWork = filmsDataFrame.applymap(removeCaracteres)

#Gerando os novos DataFrames com dados padronizados
peopleWork.to_csv('src/work/people_work.csv', index=False)
planetsWork.to_csv('src/work/planets_work.csv', index=False)
filmsWork.to_csv('src/work/films_work.csv', index=False)