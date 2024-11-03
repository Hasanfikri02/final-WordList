import requests

api_key = '9dacdb96-746f-439e-979b-e96900bece5a'
word = 'potato'
root_url = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json'
final_url = f'{root_url}/{word}?key={api_key}'
r = requests.get(final_url)
result = r.json()
print(result)