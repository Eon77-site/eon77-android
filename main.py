from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.core.window import Window
import time

try:
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.INTERNET, Permission.BLUETOOTH, Permission.ACCESS_FINE_LOCATION])
except:
    pass

THEME = {'bg': (0.01, 0.02, 0.03, 1), 'cyan': (0.00, 0.83, 1.00, 1), 'green': (0.00, 0.95, 0.50, 1)}

class Tab1(BoxLayout):
    def __init__(self, **k):
        super().__init__(orientation='vertical', padding=dp(10), **k)
        self.add_widget(Label(text='[b]REDE MESH EON-77[/b]\n\nONLINE\n4 nos conectados\n\nProof of Presence:\n1,250 AION', markup=True, font_size='14sp'))

class Tab2(BoxLayout):
    def __init__(self, **k):
        super().__init__(orientation='vertical', padding=dp(10), **k)
        self.add_widget(Label(text='[b]CARTEIRA AION[/b]\n\nReserva No.0:\n320,000,000 AION\n\nVesting: 36 meses', markup=True, font_size='14sp'))
        btn = Button(text='CLAIM AION', size_hint_y=None, height=dp(50))
        self.add_widget(btn)

class Tab3(BoxLayout):
    def __init__(self, **k):
        super().__init__(orientation='vertical', padding=dp(10), **k)
        self.add_widget(Label(text='[b]CHAT MESH P2P[/b]\n\nMensagens auto-destrutivas\n(24h)\n\nConectando...', markup=True, font_size='14sp'))

class EON77App(App):
    def build(self):
        Window.clearcolor = THEME['bg']
        root = BoxLayout(orientation='vertical')
        topbar = BoxLayout(size_hint_y=None, height=dp(50))
        topbar.add_widget(Label(text='[b]EON-77[/b]', markup=True, font_size='16sp'))
        self.clock = Label(text='--:--', font_size='12sp')
        topbar.add_widget(self.clock)
        root.add_widget(topbar)
        tabs = TabbedPanel(do_default_tab=False)
        t1 = TabbedPanelItem(text='REDE')
        t1.content = Tab1()
        tabs.add_widget(t1)
        t2 = TabbedPanelItem(text='CARTEIRA')
        t2.content = Tab2()
        tabs.add_widget(t2)
        t3 = TabbedPanelItem(text='CHAT')
        t3.content = Tab3()
        tabs.add_widget(t3)
        tabs.default_tab = t1
        root.add_widget(tabs)
        Clock.schedule_interval(lambda dt: setattr(self.clock, 'text', time.strftime('%H:%M:%S')), 1)
        return root

if __name__ == '__main__':
    EON77App().run()
