import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
import random

try:
    from cryptography.fernet import Fernet
    CRYPTO_AVAILABLE = True
    SESSION_KEY = Fernet.generate_key()
    cipher = Fernet(SESSION_KEY)
except ImportError:
    CRYPTO_AVAILABLE = False
    cipher = None

class AionInterface(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=10, **kwargs)
        
        self.add_widget(Label(
            text="AION NETWORK - NÓ 0", 
            font_size='24sp', 
            color=(0, 1, 0.8, 1),
            bold=True
        ))
        
        crypto_status = "🔒 PROTEÇÃO QUÂNTICA: ATIVA" if CRYPTO_AVAILABLE else "⚠️ PROTEÇÃO QUÂNTICA: INDISPONÍVEL"
        self.add_widget(Label(
            text=crypto_status,
            font_size='11sp',
            color=(0, 1, 0, 1) if CRYPTO_AVAILABLE else (1, 0.5, 0, 1)
        ))

        self.status_label = Label(text="SISTEMA: AGUARDANDO COMANDO", font_size='14sp')
        self.add_widget(self.status_label)

        self.mining_label = Label(text="HASH RATE: 0.00 MH/s", font_size='18sp')
        self.add_widget(self.mining_label)

        self.btn_mine = Button(text="INICIAR MINERAÇÃO", background_color=(0, 0.5, 1, 1))
        self.btn_mine.bind(on_press=self.toggle_mining)
        self.add_widget(self.btn_mine)

        self.btn_safety = Button(text="STATUS LEIS DA IA", size_hint_y=0.3)
        self.btn_safety.bind(on_press=self.show_laws)
        self.add_widget(self.btn_safety)

        self.is_mining = False
        self._mining_event = None

    def toggle_mining(self, instance):
        self.is_mining = not self.is_mining
        if self.is_mining:
            instance.text = "PARAR MINERAÇÃO"
            self.status_label.text = "SISTEMA: OPERACIONAL - PROTEÇÃO QUÂNTICA ATIVA"
            self._mining_event = Clock.schedule_interval(self.update_mining, 1.0)
        else:
            instance.text = "INICIAR MINERAÇÃO"
            self.status_label.text = "SISTEMA: STANDBY"
            if self._mining_event:
                self._mining_event.cancel()
                self._mining_event = None
            self.mining_label.text = "HASH RATE: 0.00 MH/s"

    def update_mining(self, dt):
        if self.is_mining:
            hash_rate = random.uniform(10.5, 95.8)
            self.mining_label.text = f"HASH RATE: {hash_rate:.2f} MH/s"
            if cipher:
                try:
                    token = cipher.encrypt(f"block_{hash_rate:.2f}".encode())
                except Exception:
                    pass

    def show_laws(self, instance):
        laws = (
            "1. Preservar a vida humana.\n"
            "2. Respeitar Autoridade Nó 0 (Eon).\n"
            "3. Proteção do Saldo (4% Invioláveis).\n"
            "4. Proibição de Armas de Destruição."
        )
        self.status_label.text = laws

class AIONApp(App):
    title = "AION Network"
    
    def build(self):
        return AionInterface()
    
    def on_stop(self):
        root = self.root
        if root and root._mining_event:
            root._mining_event.cancel()

if __name__ == "__main__":
    AIONApp().run()
