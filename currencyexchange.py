from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class ArithmeticApp(App):
    def build(self):
        # utworzenie interfejsu użytkownika
        layout = BoxLayout(orientation='vertical')
        self.input = self.root.ids.input_field
        self.operation_label = self.root.ids.operation_label
        self.add_button = self.root.ids.add_button
        self.subtract_button = self.root.ids.subtract_button
        self.multiply_button = self.root.ids.multiply_button
        self.divide_button = self.root.ids.divide_button
        self.result_label = self.root.ids.result_label

        # przypisanie funkcji do przycisków
        self.add_button.bind(on_press=self.add)
        self.subtract_button.bind(on_press=self.subtract)
        self.multiply_button.bind(on_press=self.multiply)
        self.divide_button.bind(on_press=self.divide)

        return layout

    def add(self, instance):
        self.perform_operation(lambda x, y: x + y)

    def subtract(self, instance):
        self.perform_operation(lambda x, y: x - y)

    def multiply(self, instance):
        self.perform_operation(lambda x, y: x * y)

    def divide(self, instance):
        self.perform_operation(lambda x, y: x / y)

    def perform_operation(self, operation):
        # pobranie liczby z pola tekstowego
        try:
            num = float(self.input.text)
        except ValueError:
            self.result_label.text = 'Nieprawidłowa liczba'
            return

        # wykonanie operacji arytmetycznej
        try:
            result = operation(num, 2)
        except ZeroDivisionError:
            self.result_label.text = 'Nie można dzielić przez 0'
            return

        # wyświetlenie wyniku
        self.result_label.text = str(result)


if __name__ == '__main__':
    ArithmeticApp().run()
