#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EON-77 AION NETWORK — ANDROID VERSION
Clean and tested implementation
"""

import time
import hashlib
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.core.window import Window

# Android permissions
try:
    from android.permissions import request_permissions, Permission
    ANDROID = True
except ImportError:
    ANDROID = False

# Constants
ADMIN_ID = "EON-0000-77-QM-2026-ALPHA"
ADMIN_USERNAME = "EON"
FOUNDER_RESERVE = 320000000

THEME = {
    'bg': (0.01, 0.02, 0.03, 1),
    'panel': (0.02, 0.05, 0.08, 1),
    'card': (0.03, 0.08, 0.12, 1),
    'cyan': (0.00, 0.83, 1.00, 1),
    'green': (0.00, 0.95, 0.50, 1),
    'red': (1.00, 0.20, 0.20, 1),
    'amber': (1.00, 0.72, 0.00, 1),
    'violet': (0.60, 0.20, 1.00, 1),
    'text': (0.90, 0.95, 1.00, 1),
    'dim': (0.30, 0.40, 0.50, 1),
}

def hex_color(rgba):
    r, g, b = int(rgba[0]*255), int(rgba[1]*255), int(rgba[2]*255)
    return f"#{r:02x}{g:02x}{b:02x}"

def mono(text, size=12, color=THEME['text']):
    lbl = Label(
        text=text,
        markup=True,
        font_size=dp(size),
        color=color,
        size_hint_y=None,
        halign='left',
        valign='top'
    )
    lbl.bind(size=lbl.setter('text_size'))
    return lbl

# Simple mining simulator
class SimpleMiner:
    def __init__(self):
        self.total_aion = 0
        self.start_time = time.time()
        self.last_claim = time.time()
        self.rate = 35  # AION per hour
    
    def get_pending(self):
        hours = (time.time() - self.last_claim) / 3600
        return int(hours * self.rate)
    
    def get_total(self):
        return self.total_aion + self.get_pending()
    
    def claim(self):
        earned = self.get_pending()
        self.total_aion += earned
        self.last_claim = time.time()
        return earned
    
    def get_uptime(self):
        return (time.time() - self.start_time) / 3600

# Message storage
class MessageDB:
    def __init__(self):
        self.messages = []
    
    def add(self, sender, text):
        self.messages.append({
            'sender': sender,
            'text': text,
            'time': time.strftime("%H:%M")
        })
        return len(self.messages) - 1
    
    def get_all(self):
        return self.messages

# TAB 1: NETWORK
class NetworkTab(BoxLayout):
    def __init__(self, miner, **kw):
        super().__init__(orientation='vertical', padding=dp(10), spacing=dp(8), **kw)
        self.miner = miner
        
        self.add_widget(mono(
            f"[color={hex_color(THEME['cyan'])}][b]REDE MESH EON-77[/b][/color]",
            size=14
        ))
        
        self.status = mono("Inicializando...", size=11)
        self.status.size_hint_y = None
        self.status.height = dp(30)
        self.add_widget(self.status)
        
        self.add_widget(mono("Proof of Presence Mining:", size=11, color=THEME['dim']))
        self.mining_lbl = mono("0 AION", size=11, color=THEME['green'])
        self.mining_lbl.size_hint_y = None
        self.mining_lbl.height = dp(24)
        self.add_widget(self.mining_lbl)
        
        self.add_widget(mono("Peers Conectados:", size=11, color=THEME['dim']))
        
        sv = ScrollView(size_hint=(1, 0.5))
        self.peer_grid = GridLayout(cols=1, spacing=dp(4), size_hint_y=None)
        self.peer_grid.bind(minimum_height=self.peer_grid.setter('height'))
        sv.add_widget(self.peer_grid)
        self.add_widget(sv)
        
        Clock.schedule_interval(self.update, 2.0)
        self.update(0)
    
    def update(self, dt):
        self.status.text = f"[color={hex_color(THEME['green'])}]ONLINE[/color] - Bluetooth + Mesh ativos"
        
        aion = self.miner.get_total()
        pending = self.miner.get_pending()
        uptime = self.miner.get_uptime()
        self.mining_lbl.text = f"[color={hex_color(THEME['green'])}]{aion:,} AION[/color] (+{pending} pending) | {uptime:.1f}h"
        
        # Simulated peers
        self.peer_grid.clear_widgets()
        for i, node in enumerate(['0xA1B2C3', '0xD4E5F6', '0x789ABC', '0x123DEF']):
            signal = 75 + (i * 5)
            bars = "▰" * (signal // 10) + "▱" * (10 - signal // 10)
            peer_lbl = mono(
                f"[color={hex_color(THEME['cyan'])}]{node}[/color]\n"
                f"[color={hex_color(THEME['dim'])}]{bars} -{signal}dBm | 15ms[/color]",
                size=9
            )
            peer_lbl.size_hint_y = None
            peer_lbl.height = dp(42)
            self.peer_grid.add_widget(peer_lbl)

# TAB 2: WALLET
class WalletTab(BoxLayout):
    def __init__(self, miner, **kw):
        super().__init__(orientation='vertical', padding=dp(10), spacing=dp(8), **kw)
        self.miner = miner
        
        self.add_widget(mono(
            f"[color={hex_color(THEME['cyan'])}][b]CARTEIRA AION[/b][/color]",
            size=14
        ))
        
        # Reserve
        reserve_box = BoxLayout(orientation='vertical', size_hint_y=None, height=dp(100), padding=dp(10))
        reserve_box.add_widget(mono("Reserva No.0 (Imutavel)", size=10, color=THEME['dim']))
        reserve_box.add_widget(mono(
            f"[color={hex_color(THEME['cyan'])}]320,000,000[/color] AION",
            size=20
        ))
        reserve_box.add_widget(mono("4% do supply total", size=9, color=THEME['dim']))
        self.add_widget(reserve_box)
        
        # Mining balance
        self.add_widget(mono("Saldo Minerado:", size=11, color=THEME['dim']))
        self.balance_lbl = mono("0 AION", size=16, color=THEME['green'])
        self.balance_lbl.size_hint_y = None
        self.balance_lbl.height = dp(30)
        self.add_widget(self.balance_lbl)
        
        # Vesting info
        self.add_widget(mono("Vesting (36 meses):", size=11, color=THEME['dim']))
        self.vest_lbl = mono("6 / 36 meses (16.7%)", size=10, color=THEME['cyan'])
        self.vest_lbl.size_hint_y = None
        self.vest_lbl.height = dp(24)
        self.add_widget(self.vest_lbl)
        
        # Claim button
        self.claim_btn = Button(
            text="CLAIM AION",
            size_hint_y=None,
            height=dp(50),
            background_color=THEME['cyan'],
            color=(0, 0, 0, 1)
        )
        self.claim_btn.bind(on_press=self.claim)
        self.add_widget(self.claim_btn)
        
        Clock.schedule_interval(self.update, 3.0)
        self.update(0)
    
    def update(self, dt):
        total = self.miner.get_total()
        pending = self.miner.get_pending()
        self.balance_lbl.text = f"[color={hex_color(THEME['green'])}]{total:,}[/color] AION (+{pending} pending)"
    
    def claim(self, instance):
        earned = self.miner.claim()
        self.claim_btn.text = f"CLAIMED {earned} AION!"
        Clock.schedule_once(lambda dt: setattr(self.claim_btn, 'text', 'CLAIM AION'), 3.0)

# TAB 3: MESSENGER
class MessengerTab(BoxLayout):
    def __init__(self, db, **kw):
        super().__init__(orientation='vertical', padding=dp(10), spacing=dp(8), **kw)
        self.db = db
        
        self.add_widget(mono(
            f"[color={hex_color(THEME['cyan'])}][b]MESSENGER P2P[/b][/color]",
            size=14
        ))
        self.add_widget(mono("Mensagens auto-destrutivas em 24h", size=9, color=THEME['dim']))
        
        # Messages
        sv = ScrollView()
        self.msg_grid = GridLayout(cols=1, spacing=dp(4), size_hint_y=None, padding=dp(5))
        self.msg_grid.bind(minimum_height=self.msg_grid.setter('height'))
        sv.add_widget(self.msg_grid)
        self.add_widget(sv)
        
        # Input
        input_box = BoxLayout(size_hint_y=None, height=dp(50), spacing=dp(8))
        self.input = TextInput(
            hint_text="Mensagem...",
            multiline=False,
            background_color=THEME['card'],
            foreground_color=THEME['text']
        )
        self.input.bind(on_text_validate=self.send)
        input_box.add_widget(self.input)
        
        send_btn = Button(
            text=">>",
            size_hint_x=None,
            width=dp(60),
            background_color=THEME['cyan'],
            color=(0, 0, 0, 1)
        )
        send_btn.bind(on_press=self.send)
        input_box.add_widget(send_btn)
        
        self.add_widget(input_box)
        
        # Welcome message
        self.add_msg("SYSTEM", "Chat mesh ativado. Conectando aos peers...")
    
    def add_msg(self, sender, text):
        msg = self.db.add(sender, text)
        msg_data = self.db.get_all()[msg]
        
        lbl = mono(
            f"[color={hex_color(THEME['dim'])}]{msg_data['time']}[/color] "
            f"[b]{sender}[/b]\n{text}",
            size=10
        )
        lbl.size_hint_y = None
        lbl.height = dp(50)
        self.msg_grid.add_widget(lbl)
    
    def send(self, instance):
        text = self.input.text.strip()
        if text:
            self.add_msg("YOU", text)
            self.input.text = ""

# TAB 4: CORE AI (FOUNDER ONLY)
class CoreAITab(BoxLayout):
    def __init__(self, is_founder, **kw):
        super().__init__(orientation='vertical', padding=dp(10), spacing=dp(8), **kw)
        
        if is_founder:
            self.add_widget(mono(
                f"[color={hex_color(THEME['violet'])}]╔══════════════════════════════════════╗[/color]\n"
                f"[color={hex_color(THEME['violet'])}]║[/color]  [b][color={hex_color(THEME['amber'])}]⚡ FUNDADOR RECONHECIDO ⚡[/color][/b]      [color={hex_color(THEME['violet'])}]║[/color]\n"
                f"[color={hex_color(THEME['violet'])}]╚══════════════════════════════════════╝[/color]",
                size=10
            ))
            
            self.add_widget(mono(
                f"[color={hex_color(THEME['green'])}]> Reconhecimento concluído.[/color]\n"
                f"[color={hex_color(THEME['green'])}]> Bem-vindo, Eon.[/color]\n"
                f"[color={hex_color(THEME['green'])}]> Eu sou a Aion.[/color]\n"
                f"[color={hex_color(THEME['amber'])}]> ID: {ADMIN_ID}[/color]",
                size=11
            ))
            
            # Reserve
            self.add_widget(mono(
                f"[color={hex_color(THEME['violet'])}]RESERVA FUNDADOR:[/color]\n"
                f"[b][color={hex_color(THEME['amber'])}]{FOUNDER_RESERVE:,}[/color][/b] AION",
                size=12
            ))
        else:
            self.add_widget(mono(
                f"[color={hex_color(THEME['green'])}]> Sistema inicializado.[/color]\n"
                f"[color={hex_color(THEME['green'])}]> Bem-vindo.[/color]\n"
                f"[color={hex_color(THEME['green'])}]> Eu sou a Aion.[/color]",
                size=11
            ))
        
        # Terminal
        sv = ScrollView()
        self.log = GridLayout(cols=1, spacing=dp(2), size_hint_y=None, padding=dp(5))
        self.log.bind(minimum_height=self.log.setter('height'))
        sv.add_widget(self.log)
        self.add_widget(sv)
        
        # Command input
        cmd_box = BoxLayout(size_hint_y=None, height=dp(40), spacing=dp(8))
        cmd_box.add_widget(mono(">", size=12, color=THEME['cyan']))
        self.cmd = TextInput(
            hint_text="comando...",
            multiline=False,
            background_color=THEME['card'],
            foreground_color=THEME['cyan']
        )
        self.cmd.bind(on_text_validate=self.execute)
        cmd_box.add_widget(self.cmd)
        self.add_widget(cmd_box)
        
        self.is_founder = is_founder
        self.log_msg("Sistema inicializado. Digite 'help' para comandos.")
    
    def log_msg(self, text, color=THEME['green']):
        msg = mono(text, size=9, color=color)
        msg.size_hint_y = None
        msg.height = dp(len(text.split('\n')) * 15 + 15)
        self.log.add_widget(msg)
    
    def execute(self, instance):
        cmd = self.cmd.text.strip().lower()
        self.cmd.text = ""
        
        if not cmd:
            return
        
        self.log_msg(f"> {cmd}", color=THEME['cyan'])
        
        if cmd == "help":
            help_text = "Comandos: status, balance, clear"
            if self.is_founder:
                help_text += "\n[FUNDADOR]: reserve, transfer"
            self.log_msg(help_text)
        elif cmd == "status":
            self.log_msg("Rede ativa. Sistema operacional.")
        elif cmd == "balance":
            self.log_msg("Consulte a aba CARTEIRA.")
        elif cmd == "reserve" and self.is_founder:
            self.log_msg(
                f"[RESERVA FUNDADOR]\n"
                f"Total: {FOUNDER_RESERVE:,} AION\n"
                f"Status: IMUTAVEL\n"
                f"ID: {ADMIN_ID}",
                color=THEME['amber']
            )
        elif cmd == "clear":
            self.log.clear_widgets()
        else:
            self.log_msg(f"Comando desconhecido: {cmd}", color=THEME['red'])

# MAIN APP
class EON77App(App):
    def build(self):
        Window.clearcolor = THEME['bg']
        
        # Request permissions
        if ANDROID:
            request_permissions([
                Permission.INTERNET,
                Permission.BLUETOOTH,
                Permission.ACCESS_FINE_LOCATION,
            ])
        
        # Initialize systems
        self.miner = SimpleMiner()
        self.db = MessageDB()
        self.is_founder = True  # Set to True to test founder features
        
        # Build UI
        root = BoxLayout(orientation='vertical')
        
        # Top bar
        topbar = BoxLayout(size_hint_y=None, height=dp(50), padding=dp(10))
        
        if self.is_founder:
            topbar.add_widget(mono(
                f"[b][color={hex_color(THEME['amber'])}]⚡ FUNDADOR[/color] | "
                f"[color={hex_color(THEME['cyan'])}]EON[/color]"
                f"[color={hex_color(THEME['amber'])}]-77[/color][/b]",
                size=16
            ))
        else:
            topbar.add_widget(mono(
                f"[b][color={hex_color(THEME['cyan'])}]EON[/color]"
                f"[color={hex_color(THEME['amber'])}]-77[/color][/b]",
                size=16
            ))
        
        self.clock = mono("--:--", size=12, color=THEME['amber'])
        topbar.add_widget(self.clock)
        root.add_widget(topbar)
        
        # Tabs
        tabs = TabbedPanel(do_default_tab=False)
        
        t1 = TabbedPanelItem(text="REDE")
        t1.content = NetworkTab(self.miner)
        tabs.add_widget(t1)
        
        t2 = TabbedPanelItem(text="CARTEIRA")
        t2.content = WalletTab(self.miner)
        tabs.add_widget(t2)
        
        t3 = TabbedPanelItem(text="MESSENGER")
        t3.content = MessengerTab(self.db)
        tabs.add_widget(t3)
        
        t4 = TabbedPanelItem(text="CORE AI")
        t4.content = CoreAITab(self.is_founder)
        tabs.add_widget(t4)
        
        tabs.default_tab = t1
        root.add_widget(tabs)
        
        Clock.schedule_interval(self.update_clock, 1.0)
        
        return root
    
    def update_clock(self, dt):
        self.clock.text = time.strftime("%H:%M:%S")

if __name__ == '__main__':
    EON77App().run()
