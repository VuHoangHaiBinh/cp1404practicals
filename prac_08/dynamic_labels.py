from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelApp(App):
    """DydamicLabelApp is a Kivy App for creating labels from a string list."""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Kato", "Jake", "Bob", "Chong"]

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Dynamic Label Generator"
        self.root = Builder.load_file('dynamic_labels.kv')
        for name in self.names:
            self.root.ids.main.add_widget(Label(text=name))
        return self.root


DynamicLabelApp().run()
