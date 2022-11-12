import requests
import datetime as DT

last_date = DT.datetime.today() - DT.timedelta(days=2)

base_host = 'https://api.stackexchange.com/'

uri_requests = '/search'
requests_url = base_host + uri_requests
params = {'tagged': 'python', 'sort': 'creation', 'fromdate': last_date.strftime(''),
          'todate': DT.datetime.today().strftime(''), 'site': 'stackoverflow'}

response = requests.get(requests_url, params=params)
print(response.json())
try:
    for value in response.json().values():
        for item in value:
            print(item['title'])
except TypeError:
    pass