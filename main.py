from kivy.app import App
from kivy.uix.button import Button

class HelloWorld(App):
    def build(self):
        return Button(text='Hello Mobile World!', 
                      font_size='20sp',
                      background_color=(0, 1, 0, 0.7))

if __name__ == '__main__':
    HelloWorld().run()
