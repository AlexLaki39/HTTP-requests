import requests


class SuperHeroApi:
    base_url = 'https://akabab.github.io/superhero-api/api/'
    our_superheroes = []
    superheroes_intelligence = {}

    def __init__(self, name):
        self.name = name
        if name not in SuperHeroApi.our_superheroes:
            SuperHeroApi.our_superheroes.append(name)
        self._get_heroes_intelligence()

    def _get_heroes_intelligence(self):
        uri_all_json = '/all.json'
        response = requests.get(SuperHeroApi.base_url + uri_all_json)
        list_all_heroes = response.json()
        for items in list_all_heroes:
            if items['name'] in SuperHeroApi.our_superheroes:
                SuperHeroApi.superheroes_intelligence[items['name']] = \
                    items['powerstats']['intelligence']


def most_intelligent_superhero():
    most_intell = max(SuperHeroApi.superheroes_intelligence)
    print(
        f'Самым умным среди {",".join(SuperHeroApi.our_superheroes)} '
        f'оказался {most_intell}')


Thanos = SuperHeroApi('Thanos')
Hulk = SuperHeroApi('Hulk')
Captain_America = SuperHeroApi('Captain America')

most_intelligent_superhero()

