from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.lang import Builder

Builder.load_file('zakladki.kv', rulesonly=True)


class MyTabbedPanel(TabbedPanel):
    pass


class TabbedPanelItem1(TabbedPanelItem):
    def __init__(self, **kwargs):
        super(TabbedPanelItem1, self).__init__(**kwargs)
        self.input = self.ids.input

    def update_image_left(self, option):
        if option == 'EUR':
            self.ids.image.source = 'icons/eur.png'
        elif option == 'USD':
            self.ids.image.source = 'icons/usa.png'
        elif option == 'PLN':
            self.ids.image.source = 'icons/pol.png'
        elif option == 'CHF':
            self.ids.image.source = 'icons/swi.png'
        elif option == 'GBP':
            self.ids.image.source = 'icons/gb.png'
        elif option == 'SWE':
            self.ids.image.source = 'icons/swe.png'
        elif option == 'JPN':
            self.ids.image.source = 'icons/jpn.png'

    def update_image_right(self, option):
        if option == 'EUR':
            self.ids.image2.source = 'icons/eur.png'
        elif option == 'USD':
            self.ids.image2.source = 'icons/usa.png'
        elif option == 'PLN':
            self.ids.image2.source = 'icons/pol.png'
        elif option == 'CHF':
            self.ids.image2.source = 'icons/swi.png'
        elif option == 'GBP':
            self.ids.image2.source = 'icons/gb.png'
        elif option == 'SWE':
            self.ids.image2.source = 'icons/swe.png'
        elif option == 'JPN':
            self.ids.image2.source = 'icons/jpn.png'


class TabbedPanelItem2(TabbedPanelItem):
    pass


class TabbedPanelItem3(TabbedPanelItem):
    pass


class MyApp(App):
    def build(self):
        tab_panel = MyTabbedPanel()
        return tab_panel


if __name__ == '__main__':
    MyApp().run()
