from kivy.app import App
#kivy.require("1.8.0")

from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class SampleKivy(App):
    def build(self):
        return LoginScreen()

class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="Username:"))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        
if __name__ == "__main__":
    SampleKivy().run()
