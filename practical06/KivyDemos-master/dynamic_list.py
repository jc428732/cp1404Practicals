from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label
from kivy.properties import StringProperty


class DynamicList(App):
    def build(self):
        Window.size = (1200, 400)
        self.title = "Dynamic List"
        self.root = Builder.load_file('dynamic_list.kv')
        return self.root

    def create_widgets(self):
        for entry in self.entries:
            temp_label = Label(text=str(entry))
            self.root.ids.box.add_widget(temp_label)

DynamicList().run()
