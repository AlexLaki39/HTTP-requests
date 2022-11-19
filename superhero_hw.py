import requests


base_url = 'https://akabab.github.io/superhero-api/api/'
heroes_list = ['Hulk', 'Captain America', 'Thanos']
superheroes_intelligence = {}
uri_all_json = '/all.json'

requests_url = base_url + uri_all_json
response = requests.get(requests_url)

for items in response.json():
    if items['name'] in heroes_list:
        superheroes_intelligence[items['name']] = \
            items['powerstats']['intelligence']
most_intell = max(superheroes_intelligence, key=superheroes_intelligence.get)
print(f'Самым умным среди {",".join(superheroes_intelligence)} '
    f'оказался {most_intell}')

