from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class ConvertMilesToKilometres(App):
    def build(self):
        Window.size = (1200, 400)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('Convert Miles To Kilometres.kv')
        return self.root

    def handle_convert(self, value):
        try:
            self.root.ids.output_label.text = str(float(value) * 1.668)
        except ValueError:
            self.root.ids.output_label.text = str(0.0)

    def handle_increment(self, value, counter):
        try:
            self.root.ids.input_number.text = str(float(value) + counter)
        except ValueError:
            self.root.ids.input_number.text = str(counter)

ConvertMilesToKilometres().run()
