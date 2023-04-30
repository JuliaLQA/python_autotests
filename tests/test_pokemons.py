import requests
import pytest

token = '119a696bfe439c4fd6c12d8e972c3d9b'
prod_url = 'https://pokemonbattle.me:9104/'

def test_status_code():
    response = requests.get(f'{prod_url}trainers')
    assert response.status_code == 200


def test_part_of_body():
    response = requests.get(f'{prod_url}trainers', params={'trainer_id': 4198})
    assert response.json()['trainer_name'] == 'Симона'