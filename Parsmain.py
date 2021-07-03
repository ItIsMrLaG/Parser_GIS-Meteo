from kivy.config import Config
Config.set("graphics", "resizable", 0)
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition


Builder.load_file('pars_gui.kv')
changer = 1



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
        self.icon = None
        self.title = 'Parser'


if __name__ == '__main__':
    ParserApp().run()