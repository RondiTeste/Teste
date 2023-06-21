from kivymd.uix.floatlayout import FloatLayout
from kivymd.app import MDApp

class Tela(FloatLayout):
	...
class MainApp(MDApp):
	def build(self):
		return Tela()
if __name__ == '__main__':
  MainApp().run()