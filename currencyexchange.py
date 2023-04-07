from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.lang import Builder

Builder.load_file('currencyexchange.kv', rulesonly=True)


class MainScreen(BoxLayout):
    def calculate(self):
        if self.number_input.text:
            try:
                result = eval(self.number_input.text)
                self.update_result(str(result))
            except:
                self.update_result('Invalid input')

    def update_result(self, result):
        self.ids.result_label.text = result

class CalculatorApp(App):
    def build(self):
        return MainScreen()

if __name__ == '__main__':
    CalculatorApp().run()
