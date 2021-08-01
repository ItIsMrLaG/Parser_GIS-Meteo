from kivy.config import Config
Config.set("graphics", "resizable", 0)
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from models import *


Builder.load_file('pars_gui.kv')
changer = 1

pars = Parser("mind.txt")


class ScreenMain(Screen, Widget):

    def __init__(self, **kwargs):
        super(ScreenMain, self).__init__(**kwargs)
        self.text_config()

    def info_travel(self, *args):
        """this function change your screen to InfoScreen"""
        self.manager.current = 'second'

    def mind_travel(self, *args):
        """this function change your screen to MindScreen"""
        self.manager.current = 'third'

    def text_config(self):
        """this function contain config information of some widgets"""
        self.temperature.text = 'Temperature'
        self.time.text = 'Time of info taking'
        self.wind.text = 'Strength of wind'
        self.snow.text = 'Fulling things'
        '''-----------------------------'''
        self.city.text = 'Your city'
        self.mind.text = 'Настройки'
        self.info.text = 'Справка'
        self.putter.text = 'Обновить'

    '''def press_func(self):
        global changer
        changer = self.city.text
        print(self.city.text)'''

    def parser_go(self):
        try:
            info = pars.parse(self.city.text)
            self.temperature.text = info['temp']
            self.time.text = info['time']
            self.wind.text = info['wind']
            self.snow.text = info['full']
            self.img_chooser(info['full'], info['time'])
            self.city.text = ''
        except:
            self.image.source = 'pictures/bug.png'
            print("Error")

    def img_chooser(self, info, time):
        time = self.time_chooser(time)
        if ('рад' in info) or ('роза' in info):
            self.image.source = 'pictures/storm.png'
        elif 'сно' in info and time == 'day':
            self.image.source = 'pictures/sun1.png'
        elif 'сно' in info and time == 'night':
            self.image.source = 'pictures/moon1.png'
        elif 'нег' in info:
            self.image.source = 'pictures/snow1.png'
        elif (('ождь' in info) or ('ивень' in info)) and time == 'night':
            self.image.source = 'pictures/rain_n.png'
        elif (('ождь' in info) or ('ивень' in info)) and time == 'day':
            self.image.source = 'pictures/rain_d.png'
        elif (('блачно' in info) or ('смурно' in info)) and time == 'day':
            self.image.source = 'pictures/cloudy_d.png'
        elif (('блачно' in info) or ('смурно' in info)) and time == 'night':
            self.image.source = 'pictures/cloudy_n.png'
        else:
            self.image.source = 'pictures/if_bad.jpg'

    def time_chooser(self, time):
        time = int(time[0:2])
        if 20 <= time or time <= 6:
            return 'night'
        else:
            return 'day'

class ScreenInfo(Screen, Widget):

    def __init__(self, **kwargs):
        super(ScreenInfo, self).__init__(**kwargs)

    def home_travel(self, *args):
        """this function change your screen to MainScreen"""
        self.manager.current = 'first'

class ScreenMind(Screen, Widget):

    def __init__(self, **kwargs):
        super(ScreenMind, self).__init__(**kwargs)

    def home_travel(self, *args):
        """this function change your screen to MainScreen"""
        self.manager.current = 'first'

    def minder(self):
        url = self.url_city.text
        name = self.name_city.text
        pars.minder(name, url)

class ParserApp(App):

    def build(self):
        win = ScreenManager(transition=NoTransition())
        win.add_widget(ScreenMain(name='first'))
        win.add_widget(ScreenInfo(name='second'))
        win.add_widget(ScreenMind(name='third'))
        self.win_config()
        return win

    def win_config(self):
        Window.size = (628, 260)
        self.icon = 'pictures/icon.png'
        self.title = 'Weather'


if __name__ == '__main__':
    ParserApp().run()
