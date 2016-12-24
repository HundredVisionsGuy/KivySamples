############################################
#   Sample1.py
#   by Hundredvisions Guy
#   from Kivy with Python tutorial Part 3 -
#       The Kivy .kv Language
#
#   https://www.youtube.com/watch?v=74zCdYRCtog&t=332s
#
############################################

from kivy.app import App
#kivy.require("1.8.0")

from kivy.uix.label import Label
from kivy.uix.widget import Widget

class Widgets(Widget):
    pass

class SampleKivy2(App):
    def build(self):
        return Widgets()

if __name__ == "__main__":
    SampleKivy2().run()
