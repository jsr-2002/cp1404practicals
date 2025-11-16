from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.label import Label


class KivyDemoApp(App):
    message = StringProperty("Welcome! Add a name below.")

    def build(self):
        return Builder.load_file("interface.kv")

    def add_name(self):
        name = self.root.ids.name_input.text.strip()
        if name:
            new_label = Label(text=name, font_size=20)
            self.root.ids.list_box.add_widget(new_label)
            self.root.ids.name_input.text = ""
            self.message = f"Added: {name}"
        else:
            self.message = "Please enter a name first!"

    def clear_list(self):
        self.root.ids.list_box.clear_widgets()
        self.message = "List cleared."


if __name__ == "__main__":
    KivyDemoApp().run()
