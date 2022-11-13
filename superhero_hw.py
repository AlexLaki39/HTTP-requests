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


## Второй вариант хотел попробовать с классами, хотя они тут и не нужны
## И ту вопрос можно ли в методе init вызвать другой метод который ниже?(правильно ли так делать?)


# class SuperHeroApi:
#     base_url = 'https://akabab.github.io/superhero-api/api/'
#     our_superheroes = []
#     superheroes_intelligence = {}
#
#     def __init__(self, name: str):
#         self.name = name
#         if name not in SuperHeroApi.our_superheroes:
#             SuperHeroApi.our_superheroes.append(name)
#         self._get_heroes_intelligence()
#
#     def _get_heroes_intelligence(self):
#         '''
#         Получает значение ителлекта героя
#         '''
#         uri_all_json = '/all.json'
#         response = requests.get(SuperHeroApi.base_url + uri_all_json)
#         list_all_heroes = response.json()
#         for items in list_all_heroes:
#             if items['name'] in SuperHeroApi.our_superheroes:
#                 SuperHeroApi.superheroes_intelligence[items['name']] = \
#                     items['powerstats']['intelligence']
#             elif items['name'] in SuperHeroApi.our_superheroes:
#                 break
#
#
# def most_intelligent_superhero():
#     '''
#     Выводит самого умного героя
#     '''
#     most_intell = max(SuperHeroApi.superheroes_intelligence)
#     print(
#         f'Самым умным среди {",".join(SuperHeroApi.our_superheroes)} '
#         f'оказался {most_intell}')
#
#
# Hulk = SuperHeroApi('Hulk')
# Thanos = SuperHeroApi('Thanos')
# Captain_America = SuperHeroApi('Captain America')
#
# most_intelligent_superhero()

