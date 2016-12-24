############################################
#   LoginTest.py
#   by Hundredvisions Guy
#   from Kivy with Python tutorial Part 2 -
#           Widgets and Labels
#
#   https://www.youtube.com/watch?v=cJtdb-vPxBo
#
############################################

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

        # Username
        self.add_widget(Label(text="Username:"))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        # Password
        self.add_widget(Label(text="Password:"))
        self.password = TextInput(multiline=False,
                                  password=True)
        self.add_widget(self.password)

        # Password Verification (aka Two-Factor Authentication - tfa)
        self.add_widget(Label(text="Repeat Username:"))
        self.tfa = TextInput(multiline=False,
                                  password=True)
        self.add_widget(self.tfa)


if __name__ == "__main__":
    SampleKivy().run()
