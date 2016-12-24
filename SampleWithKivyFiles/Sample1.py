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

class SampleKivy(App):
    def build(self):
        return Label()

if __name__ == "__main__":
    SampleKivy().run()
