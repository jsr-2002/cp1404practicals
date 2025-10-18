"""
Kivy Demo Launcher
Estimate: 10 minutes
Actual:   TODO
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class DemoApp(App):
    status_text = StringProperty("Ready")

    def build(self):
        self.title = "Kivy Demo"
        self.root = Builder.load_file("kivy_layout.kv")
        return self.root


if __name__ == "__main__":
    DemoApp().run()
