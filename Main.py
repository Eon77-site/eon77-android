import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
import random

# Tenta importar a criptografia. Se o build for "leve", ele avisa mas não trava.
try:
    from cryptography.fernet import Fernet
    CRYPTO_AVAILABLE = True
except ImportError:
    CRYPTO_AVAILABLE = False

class AionInterface(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=10, **kwargs)
        
        # Cabeçalho de Autoridade
        self.add_widget(Label(
            text="AION NETWORK - NÓ 0", 
            font_size='24sp', 
            color=(0, 1, 0.8, 1),
            bold=True
        ))
        
        self.status_label = Label(text="SISTEMA: AGUARDANDO COMANDO", font_size='14sp')
        self.add_widget(self.status_label)

        # Painel de Mineração Simulado
        self.mining_label = Label(text="HASH RATE: 0.00 MH/s", font_size='18sp')
        self.add_widget(self.mining_label)

        # Botões de Comando
        self.btn_mine = Button(text="INICIAR MINERAÇÃO", background_color=(0, 0.5, 1, 1))
        self.btn_mine.bind(on_press=self.toggle_mining)
        self.add_widget(self.btn_mine)

        self.btn_safety = Button(text="STATUS LEIS DA IA", size_hint_y=0.3)
        self.btn_safety.bind(on_press=self.show_laws)
        self.add_widget(self.btn_safety)

        self.is_mining = False

    def toggle_mining(self, instance):
        self.is_mining = not self.is_mining
        if self.is_mining:
            instance.text = "PARAR MINERAÇÃO"
            self.status_label.text = "SISTEMA: OPERACIONAL - PROTEÇÃO QUÂNTICA ATIVA"
            Clock.schedule_interval(self.update_mining, 1.0)
        else:
            instance.text = "INICIAR MINERAÇÃO"
            self.status_label.text = "SISTEMA: STANDBY"
            Clock.unschedule(self.update_mining)

    def update_mining(self, dt):
        if self.is_mining:
            hash_rate = random.uniform(10.5, 95.8)
            self.mining_label.text = f"HASH RATE: {hash_rate:.2f} MH/s"

    def show_laws(self, instance):
        laws = (
            "1. Preservar a vida humana.\n"
            "2. Respeitar Autoridade Nó 0 (Eon).\n"
            "3. Proteção do Saldo (4% Invioláveis).\n"
            "4. Proibição de Armas de Destruição."
        )
        self.status_label.text = laws

class AIONApp(App):
    def build(self):
        return AionInterface()

if __name__ == "__main__":
    AIONApp().run()
