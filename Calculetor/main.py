from kivymd.app import MDApp
from kivymd.uix.boxlayout import BoxLayout
from itertools import cycle
from kivy.properties import StringProperty, BooleanProperty
from kivy.clock import Clock


class Timer:
    def __init__(self, time):
        self.time = time * 60

    def decrementar(self):
        self.time -= 1
        return self.time

    def __str__(self):
        return '{:02d}:{:02d}'.format(*divmod(self.time, 60))


class Cycle:
    def __init__(self):
        self.cycle = cycle([
            Timer(1), Timer(2),
            Timer(1), Timer(1),
            Timer(5), Timer(30)
        ])

    def __next__(self):
        return next(self.cycle)

    def __iter__(self):
        return self


class TelaCalculator(BoxLayout):
    time_string = StringProperty('25:00')
    button_string = StringProperty('Iniciar')
    running = BooleanProperty(False)
    cycle = Cycle()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._time = next(self.cycle)
        self.time_string = str(self._time)

    def start(self):
        self.button_string = 'Pausar'
        if not self.running:
            self.running = True
            Clock.schedule_interval(self.update, 1)

    def stop(self):
        self.button_string = 'Reiniciar'
        if self.running:
            self.running = False

    def click(self):
        if self.running:
            self.stop()
        else:
            self.start()

    def update(self, *args):
        time = self._time.decrementar()
        if time == 0:
        	self.stop()
        	self._time = next(self.cycle)
        self.time_string = str(self._time)
        


class Main(MDApp):
    def charge_color(self):
    	theme = self.theme_cls.theme_style
    	if theme == "Dark":
    		self.theme_cls.theme_style = "Light"
    	else:
    		self.theme_cls.theme_style="Dark"
    		
    def build(self):
        self.theme_cls.primary_palette= "DeepPurple"
        self.theme_cls.primary_hue = '700'
        return TelaCalculator()


if __name__ == '__main__':
    Main().run()
  