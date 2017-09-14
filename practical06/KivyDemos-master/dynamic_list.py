"""
Kivy example for CP1404/CP5632, IT@JCU
Dynamically create buttons based on content of dictionary
Lindsay Ward
Modified from popup_demo, 11/07/2016
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

__author__ = 'Lindsay Ward'


class DynamicWidgetsApp(App):
    """ Main program - Kivy app to demo dynamic widget creation """
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """
        Construct main app
        """
        super().__init__(**kwargs)
        self.phonebook = ["!", "Yes", "8", "#"]

    def build(self):
        """
        Build the Kivy GUI
        :return: reference to the root Kivy widget
        """
        self.title = "Dynamic List"
        self.root = Builder.load_file('dynamic_list.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """
        Create buttons from dictionary entries and add them to the GUI
        :return: None
        """
        for name in self.phonebook:
            temp_button = Button(text=name)
            self.root.ids.entriesBox.add_widget(temp_button)

DynamicWidgetsApp().run()
