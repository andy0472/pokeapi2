import requests
from flask import Flask, request
from flask import app, render_template

from Pokemon import Pokemon
from siguientePagina import SiguientePagina
import pandas as pd

app = Flask(__name__)

if __name__ == '__main__':
    url = 'http://pokeapi.co/api/v2/pokemon/'


def pokemonInfo(url='http://pokeapi.co/api/v2/pokemon/', offset=0):
    args = {'offset': offset} if offset else {}
    response = requests.get(url, args)
    response_json = response.json()
    results = response_json['results']
    pokemones = []
    if results:
        for pokemon in results:
            url = pokemon['url']
            response = requests.get(url)
            pokemon = response.json()
            foto = pokemon['sprites']['front_default']
            id = pokemon['id']
            name = (pokemon['name'])

            for i in range(len(pokemon['abilities'])):
                ability = (pokemon['abilities'][i]['ability']['name'])
                if i == 0:
                    break
            for i in range(len(pokemon['types'])):
                type = (pokemon['types'][i]['type']['name'])
                if i == 0:
                    break
            moves = []
            for i in range(len(pokemon['moves'])):
                moves.append(pokemon['moves'][i]['move']['name'])
                if i == 4:
                    break
            pokemones.append(Pokemon(foto, id, name, ability, type, moves))

    return pokemones


def pokemonDetalle(id):
    url = 'https://pokeapi.co/api/v2/pokemon/' + str(id)
    response = requests.get(url)
    pokemon = response.json()
    foto = pokemon['sprites']['front_default']
    id = pokemon['id']
    name = (pokemon['name'])

    for i in range(len(pokemon['abilities'])):
        ability = (pokemon['abilities'][i]['ability']['name'])
        if i == 0:
            break
    for i in range(len(pokemon['types'])):
        type = (pokemon['types'][i]['type']['name'])
        if i == 0:
            break
    moves = []
    for i in range(len(pokemon['moves'])):
        moves.append(pokemon['moves'][i]['move']['name'])
        if i == 4:
            break
    return Pokemon(foto, id, name, ability, type, moves)


@app.route('/detallePokemon/<int:id>')
def detallePokemon(id):
    pokemon = pokemonDetalle(id)
    print(type(pokemon.get_moves()))
    return render_template('detallePokemon.html', pokemon=pokemon)


@app.route('/', methods=['GET', 'POST'])
def inicio():
    next = SiguientePagina()
    pokemons = pokemonInfo()
    # pokemons = nombreFoto(defaultList)
    if (request.method == 'POST'): #and (request.form['next']=='next'):
        pokemons = pokemonInfo(offset=next.get_pokemon_next())

    return render_template('inicio.html', pokemons=pokemons)
