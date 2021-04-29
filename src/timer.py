import tkinter as tk
import datetime
from game_state import GameState
from player import Player

class Countdown(tk.Frame):
    
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.show_widgets()
        self.seconds_left = 600
        self.timer_on = False

    def show_widgets(self):
        self.label.pack()
    
    def create_widgets(self):
        self.label = tk.Label(self, text="00:10:00")
        self.entry = tk.Entry(self, justify='center')
        self.entry.focus_set()

    def restart(self):
        self.seconds_left = 600
        
    def countdown(self):
        '''Atualuza o label conforme o tempo restante.'''
        self.label['text'] = self.convert_seconds_left_to_time()

        if self.seconds_left:
            self.seconds_left -= 1
            self.timer_on = self.after(1000, self.countdown)
        else:
            self.timer_on = False

    def start_timer(self):
        '''começa a contagem'''
        
        self.stop_timer()
        self.countdown()                            

    def stop_timer(self):
        '''Para ele após o tempo estipulado.'''
        if self.timer_on:
            self.after_cancel(self.timer_on)
            self.timer_on = False

    def convert_seconds_left_to_time(self):
        return datetime.timedelta(seconds=self.seconds_left)