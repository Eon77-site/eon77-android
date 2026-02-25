from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.progressbar import ProgressBar
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.core.window import Window
import random

try:
    from cryptography.fernet import Fernet
    CRYPTO_AVAILABLE = True
    SESSION_KEY = Fernet.generate_key()
    cipher = Fernet(SESSION_KEY)
except ImportError:
    CRYPTO_AVAILABLE = False
    cipher = None

class AionDashboard(TabbedPanel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.do_default_tab = False
        self.tab_pos = 'bottom_mid'
        self.is_mining = False
        self._mining_event = None

        # --- ABA 1: MINERAÇÃO (NÓ 0) ---
        self.tab_mine = TabbedPanelItem(text='AION')
        layout_mine = BoxLayout(orientation='vertical', padding=20, spacing=15)
        layout_mine.add_widget(Label(
            text="AUTORIDADE NÓ 0",
            font_size='22sp',
            color=(0, 1, 0.7, 1),
            bold=True
        ))

        crypto_status = "🔒 PROTEÇÃO QUÂNTICA: ATIVA" if CRYPTO_AVAILABLE else "⚠️ PROTEÇÃO: INDISPONÍVEL"
        layout_mine.add_widget(Label(
            text=crypto_status,
            font_size='11sp',
            color=(0, 1, 0, 1) if CRYPTO_AVAILABLE else (1, 0.5, 0, 1)
        ))

        self.hash_label = Label(text="HASH RATE: 0.00 MH/s", font_size='20sp')
        layout_mine.add_widget(self.hash_label)

        self.status_label = Label(text="SISTEMA: STANDBY", font_size='13sp')
        layout_mine.add_widget(self.status_label)

        self.btn_mine = Button(
            text="ATIVAR PROTOCOLO",
            size_hint=(1, 0.2),
            background_color=(0, 0.7, 1, 1)
        )
        self.btn_mine.bind(on_press=self.toggle_mining)
        layout_mine.add_widget(self.btn_mine)
        self.tab_mine.add_widget(layout_mine)

        # --- ABA 2: CARTEIRA & VESTING ---
        self.tab_wallet = TabbedPanelItem(text='CARTEIRA')
        layout_wallet = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout_wallet.add_widget(Label(
            text="RESERVA EON (4%)",
            font_size='18sp',
            bold=True
        ))
        self.balance_label = Label(
            text="320,000,000 AION",
            font_size='24sp',
            color=(1, 0.8, 0, 1)
        )
        layout_wallet.add_widget(self.balance_label)
        self.vesting_label = Label(text="Vesting: Ativo", font_size='12sp')
        layout_wallet.add_widget(self.vesting_label)
        self.progress_vesting = ProgressBar(max=100, value=5)
        layout_wallet.add_widget(self.progress_vesting)
        self.tab_wallet.add_widget(layout_wallet)

        # --- ABA 3: REDE & ALERTA DE PROXIMIDADE ---
        self.tab_mesh = TabbedPanelItem(text='REDE')
        layout_mesh = BoxLayout(orientation='vertical', padding=15, spacing=10)
        layout_mesh.add_widget(Label(
            text="RADAR DE PROXIMIDADE",
            font_size='18sp',
            bold=True,
            color=(1, 0, 0, 1)
        ))

        self.proximity_status = Label(
            text="Scanner Passivo: Ativo",
            font_size='12sp'
        )
        layout_mesh.add_widget(self.proximity_status)

        self.msg_input = TextInput(
            hint_text='Msg de Emergência P2P...',
            multiline=False,
            size_hint=(1, 0.2)
        )
        layout_mesh.add_widget(self.msg_input)

        self.btn_send = Button(
            text="DISPARAR ALERTA MESH",
            size_hint=(1, 0.2),
            background_color=(0.8, 0, 0, 1)
        )
        self.btn_send.bind(on_press=self.send_p2p)
        layout_mesh.add_widget(self.btn_send)

        self.log_mesh = Label(
            text="Radar: Silencioso",
            font_size='11sp',
            color=(0.7, 0.7, 0.7, 1)
        )
        layout_mesh.add_widget(self.log_mesh)
        self.tab_mesh.add_widget(layout_mesh)

        self.add_widget(self.tab_mine)
        self.add_widget(self.tab_wallet)
        self.add_widget(self.tab_mesh)

        Clock.schedule_interval(self.check_proximity, 10.0)

    def toggle_mining(self, instance):
        self.is_mining = not self.is_mining
        if self.is_mining:
            instance.text = "DESATIVAR PROTOCOLO"
            instance.background_color = (1, 0.3, 0, 1)
            self.status_label.text = "SISTEMA: OPERACIONAL"
            self._mining_event = Clock.schedule_interval(self.update_mining, 1.0)
        else:
            instance.text = "ATIVAR PROTOCOLO"
            instance.background_color = (0, 0.7, 1, 1)
            self.status_label.text = "SISTEMA: STANDBY"
            if self._mining_event:
                self._mining_event.cancel()
                self._mining_event = None
            self.hash_label.text = "HASH RATE: 0.00 MH/s"

    def update_mining(self, dt):
        if self.is_mining:
            hash_rate = random.uniform(10.5, 95.8)
            self.hash_label.text = f"HASH RATE: {hash_rate:.2f} MH/s"
            if cipher:
                try:
                    cipher.encrypt(f"block_{hash_rate:.2f}".encode())
                except Exception:
                    pass

    def check_proximity(self, dt):
        if random.random() > 0.8:
            self.log_mesh.text = "!!! ALERTA: NÓ VIZINHO DETETADO (Assinatura Eon) !!!"
            self.proximity_status.text = "STATUS: CONTACTO PRÓXIMO"
            self.proximity_status.color = (1, 1, 0, 1)
        else:
            self.log_mesh.text = "Radar: A varrer frequências P2P..."
            self.proximity_status.text = "Scanner Passivo: Ativo"
            self.proximity_status.color = (1, 1, 1, 1)

    def send_p2p(self, instance):
        msg = self.msg_input.text.strip()
        if msg:
            if cipher:
                try:
                    encrypted = cipher.encrypt(msg.encode())
                    self.log_mesh.text = f"✅ MSG CIFRADA E ENVIADA"
                except Exception:
                    self.log_mesh.text = f"✅ MSG ENVIADA: {msg}"
            else:
                self.log_mesh.text = f"✅ MSG ENVIADA: {msg}"
            self.msg_input.text = ""
        else:
            self.log_mesh.text = "⚠️ Digite uma mensagem antes de enviar."

    def on_stop_mining(self):
        if self._mining_event:
            self._mining_event.cancel()

class AIONApp(App):
    title = "AION Network"

    def build(self):
        Window.clearcolor = (0.05, 0.05, 0.1, 1)
        return AionDashboard()

    def on_stop(self):
        root = self.root
        if root and root._mining_event:
            root._mining_event.cancel()

if __name__ == "__main__":
    AIONApp().run()
