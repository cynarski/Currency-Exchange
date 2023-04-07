from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


# noinspection PyAttributeOutsideInit
class ArithmeticApp(App):
    def build(self):
        # utworzenie interfejsu użytkownika
        layout = BoxLayout(orientation='vertical')
        self.input = TextInput(text='', multiline=False)
        self.operation_label = Label(text='Wybierz operację:', size_hint=(1, 0.5))
        self.add_button = Button(text='+', size_hint=(1, 0.5))
        self.subtract_button = Button(text='-', size_hint=(1, 0.5))
        self.multiply_button = Button(text='*', size_hint=(1, 0.5))
        self.divide_button = Button(text='/', size_hint=(1, 0.5))
        self.result_label = Label(text='', size_hint=(1, 0.5))

        # dodanie widgetów do layoutu
        layout.add_widget(self.input)
        layout.add_widget(self.operation_label)
        layout.add_widget(self.add_button)
        layout.add_widget(self.subtract_button)
        layout.add_widget(self.multiply_button)
        layout.add_widget(self.divide_button)
        layout.add_widget(self.result_label)

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
