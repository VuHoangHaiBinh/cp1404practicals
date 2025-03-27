from kivy.app import App, StringProperty
from kivy.lang import Builder

MILE_TO_KILOMETER_RATE = 1.60934 

class MileKMConverter(App):
    """MileKMConverter is a Kivy App for converting miles to kilometers."""
    output_text = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Miles to Kilometers Converter"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_conversion(self):
        """Convert input_number value from miles to kilometers."""
        try:
            mile = float(self.root.ids.input_number.text)
            kilometer = mile * MILE_TO_KILOMETER_RATE
            self.output_text = str(kilometer) 
        except ValueError:
            self.root.ids.input_number.text = "0.0"

    def handle_increment(self, text, increment):
        """Increase the input number value by positive/negative increment."""
        try:
            mile = float(text) + increment
            self.root.ids.input_number.text = str(mile)
        except ValueError:
            self.root.ids.input_number.text = str(increment)


MileKMConverter().run()
