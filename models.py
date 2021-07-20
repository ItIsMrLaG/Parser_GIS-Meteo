import requests as req
from bs4 import BeautifulSoup as BeS


class FileReader:
    """This is class handler of the file with information about available cities and their url"""
    def __init__(self, file=None):
        self.file = file
        # self.write_f = open(self.file, 'a', encoding='utf8')
        # self.read_f = open(self.file, 'r', encoding='utf8')

    def check_info(self):
        """OUT-function for getting dict with information in format {'city': 'url'}"""
        read_f = open(self.file, 'r', encoding='utf8')
        lines = read_f.readlines()
        cities = {}
        for i in range(len(lines)):
            lines[i] = lines[i].strip()
            flag = lines[i].split(" -- ")
            cities[flag[0]] = flag[1]
        read_f.seek(0)
        # self.read_f.close()
        return cities

    def minder(self, name, url):
        """OUT-function which is can be used for adding optional information in format {'city': 'url'}"""
        file = open(self.file, 'a', encoding='utf8')
        print(f'{name} -- {url}', file=file)
        file.close()


class Parser(FileReader):
    """This is parser class of Gismeteo website (https://www.gismeteo.ru/)"""
    def __init__(self, file, headers=None):
        """HEADERS - user-agent, file - file with information about cities and their url"""
        super().__init__(file)
        if headers is None:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                     'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
        self.HEADERS = headers

    def get_html(self, url):
        """Inner function for getting html"""
        info = req.get(url, headers=self.HEADERS, params=None)
        return info

    def get_content(self, html):
        """Inner function for that used for creation the dict with information from the html file"""
        info = {}
        soup = BeS(html, 'html.parser')
        item = soup.find('div', class_='forecast_frame forecast_now')
        info['temp'] = item.find('span', class_='unit unit_temperature_c').get_text(strip=True)
        info['full'] = item.find('span', class_='tip _top _center').get_text(strip=True)
        info['wind'] = item.find('div', class_='nowinfo__value').get_text(strip=True) + ' м/с'
        info['time'] = item.find('time').get_text(strip=True)
        return info

    def parse(self, town):
        """OUT-function which is can be used for getting dict with information from Gismeteo"""
        html = self.get_html(self.choose_url(town))
        if html.status_code == 200:
            return self.get_content(html.text)
        else:
            print('ERROR')
            return {"error": None}

    def choose_url(self, town):
        """Inner function for getting and changing city url"""
        cities = self.check_info()
        return cities[town] + 'now/'


# d = Parser('mind.txt')
# print(d.parse('Анапа'))
# print(d.parse('Екатеринбург'))
