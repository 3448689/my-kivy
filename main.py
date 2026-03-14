from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
	def build(self):
		# Использую табуляцию, как ты любишь!
		return Button(text='Привет из GitHub Actions!')

if __name__ == '__main__':
	TestApp().run()
