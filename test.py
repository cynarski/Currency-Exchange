from kivy.app import App
from kivy.uix.spinner import Spinner
from kivy.uix.boxlayout import BoxLayout

class CurrencyConverterApp(App):
    def build(self):
        # Utwórz listę z nazwami walut
        currency_list = ['USD', 'EUR', 'JPY']

        # Utwórz Spinner
        spinner = Spinner(
            # Ustaw opcje wyboru walut jako wartości spinnera
            values=currency_list,

            # Ustaw domyślną wartość spinnera
            text=currency_list[0],

            # Ustaw styl spinnera
            background_color=(0.2, 0.2, 0.2, 1),
            color=(1, 1, 1, 1),
            size_hint=(None, None),
            size=(100, 44)
        )

        # Utwórz layout i dodaj spinner
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(spinner)

        return layout

if __name__ == '__main__':
    CurrencyConverterApp().run()
