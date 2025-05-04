from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class Dashboard(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 20
        self.set_black_theme()

        self.add_widget(Label(text='Dashboard B3Prime', font_size=32, color=(1,1,1,1)))
        self.add_widget(Button(text='Opção 1', background_color=(0.2,0.2,0.2,1), color=(1,1,1,1)))
        self.add_widget(Button(text='Opção 2', background_color=(0.2,0.2,0.2,1), color=(1,1,1,1)))
        self.add_widget(Button(text='Opção 3', background_color=(0.2,0.2,0.2,1), color=(1,1,1,1)))

    def set_black_theme(self):
        from kivy.core.window import Window
        Window.clearcolor = (0,0,0,1)  # fundo preto

class B3PrimeApp(App):
    def build(self):
        return Dashboard()

if __name__ == '__main__':
    B3PrimeApp().run()