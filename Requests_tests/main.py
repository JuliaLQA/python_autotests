import requests

token = '119a696bfe439c4fd6c12d8e972c3d9b'
prod_url = 'https://pokemonbattle.me:9104/'

response_add_pokemon = requests.post(f'{prod_url}pokemons', headers={"trainer_token": token}, json={
    "name": "Уайли",
    "photo": "https://dolnikov.ru/pokemons/albums/122.png"
})
print(response_add_pokemon.text)


response_change_pokemon = requests.put(f'{prod_url}pokemons', headers={"trainer_token": token}, json={
    "pokemon_id": "9705",
    "name": "Ганс",
    "photo": "https://dolnikov.ru/pokemons/albums/122.png"
})
print(response_change_pokemon.text)


response_add_pokeboll = requests.post(f'{prod_url}trainers/add_pokeball', headers={"trainer_token": token}, json={
    "pokemon_id": "9705"
})
print(response_add_pokeboll.text)