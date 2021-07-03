import requests as req
from bs4 import BeautifulSoup as BeS

city = input()
city_url = {
    'Москва': 'https://www.gismeteo.ru/weather-omsk-4578/',
    'Санкт-Петербург': 'https://www.gismeteo.ru/weather-sankt-peterburg-4079/',
     'Екатеринбург': 'https://www.gismeteo.ru/weather-yekaterinburg-4517/',
     'Омск': 'https://www.gismeteo.ru/weather-omsk-4578/',
     'Казань': 'https://www.gismeteo.ru/weather-kazan-4364/',
     'Челябинск': 'https://www.gismeteo.ru/weather-chelyabinsk-4565/',
     'Оренбург': 'https://www.gismeteo.ru/weather-orenburg-5159/',
     'Кемерово': 'https://www.gismeteo.ru/weather-kemerovo-4693/',
     'Сочи': 'https://www.gismeteo.ru/weather-sochi-5233/',
     'Симферополь': 'https://www.gismeteo.ru/weather-simferopol-4995/',
     'Ялта': 'https://www.gismeteo.ru/weather-yalta-5002/',
     'Алушта': 'https://www.gismeteo.ru/weather-alushta-4996/',
     'Владивосток': 'https://www.gismeteo.ru/weather-vladivostok-4877/',
     'Анапа': 'https://www.gismeteo.ru/weather-anapa-5211/'
}

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/91.0.4472.114 Safari/537.36'}
params = None


def get_html(url):
    info = req.get(url, headers=HEADERS, params=None)
    return info


def get_content(html):
    info = {}
    soup = BeS(html, 'html.parser')
    item = soup.find('div', class_='forecast_frame forecast_now')
    info['temp'] = item.find('span', class_='unit unit_temperature_c').get_text(strip=True)
    info['full'] = item.find('span', class_='tip _top _center').get_text(strip=True)
    info['wind'] = item.find('div', class_='nowinfo__value').get_text(strip=True) + ' м/с'
    info['time'] = item.find('time').get_text(strip=True)
    return info


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        return get_content(html.text)
    else:
        print('ERROR')


def changing(my_city):
    url = city_url[my_city] + 'now/'
    return url

URL = changing(city)
print(*parse())