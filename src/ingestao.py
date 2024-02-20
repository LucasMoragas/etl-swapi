import requests
import json
import pandas as pd

peoples = []
planets = []
films = []

i = 1

#Buscando dados
def buscaDados():
    request = requests.get("https://swapi.dev/api/people/")
    people_data = json.loads(request.content)
    peoples.extend(people_data['results'][:5]) #Adicionando as 5 primeiras páginas

    request = requests.get("https://swapi.dev/api/planets/")
    planet_data = json.loads(request.content)
    planets.extend(planet_data['results'][:5]) #Adicionando as 5 primeiras páginas

    request = requests.get("https://swapi.dev/api/films/")
    film_data = json.loads(request.content)
    films.extend(film_data['results'][:5]) #Adicionando as 5 primeiras páginas

if __name__ == '__main__': 
    buscaDados()
    #Gerando arquivos csv brutos
    pd.DataFrame.from_records(peoples).to_csv('src/raw/people.csv', index=False)
    pd.DataFrame.from_records(planets).to_csv('src/raw/planets.csv', index=False)
    pd.DataFrame.from_records(films).to_csv('src/raw/films.csv', index=False)



