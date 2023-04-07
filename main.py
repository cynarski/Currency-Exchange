from kivy.app import App
from currencyexchange import CurrencyExchange


class CurrencyExchangeApp(App):

    def build(self):
        return CurrencyExchange()


if __name__ == '__main__':
    CurrencyExchangeApp().run()