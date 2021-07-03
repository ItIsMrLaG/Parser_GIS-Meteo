import requests as req
from bs4 import BeautifulSoup as BeS


class FileReader:
    def __init__(self, file=None):
        self.file = file
        self.write_f = open(file, 'a', encoding='utf8')
        self.read_f = open(file, 'r', encoding='utf8')

    def check_info(self):
        lines = self.read_f.readlines()
        cities = {}
        for i in range(len(lines)):
            lines[i] = lines[i].strip()
            flag = lines[i].split(" -- ")
            cities[flag[0]] = flag[1]
        return cities

    def minder(self, name, url):
        file = self.write_f
        print(f'{name} -- {url}', file=file)
        self.write_f.close()


class Parser(FileReader):
    def __init__(self, file, headers=None):
        super().__init__(file)
        if headers is None:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                     'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
        self.HEADERS = headers

    def get_html(self, url):
        info = req.get(url, headers=self.HEADERS, params=None)
        return info

    def get_content(self, html):
        info = {}
        soup = BeS(html, 'html.parser')
        item = soup.find('div', class_='forecast_frame forecast_now')
        info['temp'] = item.find('span', class_='unit unit_temperature_c').get_text(strip=True)
        info['full'] = item.find('span', class_='tip _top _center').get_text(strip=True)
        info['wind'] = item.find('div', class_='nowinfo__value').get_text(strip=True) + ' м/с'
        info['time'] = item.find('time').get_text(strip=True)
        return info

    def parse(self, town):
        html = self.get_html(self.choose_url(town))
        if html.status_code == 200:
            return self.get_content(html.text)
        else:
            print('ERROR')

    def choose_url(self, town):
        cities = self.check_info()
        return cities[town] + 'now/'


d = Parser('mind.txt')
print(d.parse('Анапа'))
