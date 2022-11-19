import requests


class YaUploader:
    base_host = 'https://cloud-api.yandex.net:443/'

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def upload(self, file_path: str):
        uri = 'v1/disk/resources/upload/'
        requests_url = self.base_host + uri
        params = {'path': file_path, 'overwrite': True}
        response = requests.get(requests_url, headers=self.get_headers(),
                                params=params)
        response1 = requests.put(response.json()['href'],
                                 data=open(file_path, 'rb'),
                                 headers=self.get_headers())
        print(response1.status_code)


if __name__ == '__main__':
    path_to_file = ' '
    token = ' '
    ya = YaUploader(token)
    result = ya.upload(path_to_file)
