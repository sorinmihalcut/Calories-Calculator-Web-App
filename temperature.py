import requests
from selectorlib import Extractor

class Temperature:
    """
    Represents a temperature value extracted from
    the timeanddate.com/weather webpage
    """
    headers = {
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    base_url = 'https://www.timeanddate.com/weather'
    yaml_path = 'intTemp.yaml'

    def __init__(self, country, city):

        self.country = country.replace(" ", "-")
        self.city = city.replace(" ", "-")

    def create_url(self):
        url = self.base_url + '/' + self.country + '/' + self.city
        return url

    def scrape(self):
        url = self.create_url()
        r = requests.get(url, headers=self.headers)
        content = r.text
        ext = Extractor.from_yaml_file(self.yaml_path)
        raw_result = ext.extract(content)
        return raw_result

    def get(self):
        raw_content = self.scrape()

        return float(raw_content['temp'].replace('\xa0°C', '').strip())


if __name__ == '__main__':
    temperature = Temperature(country='usa', city='san francisco')
    print(temperature.get())