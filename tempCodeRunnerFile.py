from board import *
from player import Player
from game_state import GameState


def main():
    root = tk.Tk()
    root.title("chess")
    menubar = Menu(root)
    
    root.config(menu=menubar)
    gameMenu = Menu(menubar)

    gameMenu = Menu(menubar, tearoff=False)
    sub_menu = Menu(gameMenu, tearoff=0)
    sub_menu.add_command(label='Versus')
    sub_menu.add_command(label='IA')
    gameMenu.add_cascade(label='Mode', menu = sub_menu)
    
    gameMenu.add_separator()
    
    gameMenu.add_command(label='Exit', command = root.destroy)
    menubar.add_cascade(label="Game", menu = gameMenu, underline=1)     
    
    help_menu = Menu(menubar, tearoff=0)

    help_menu.add_command(label='Rules')
    help_menu.add_command(label='About...')
    menubar.add_cascade(label="Help", menu=help_menu, underline=0)

    
    board = Board(root)
    board.pack(side="top", fill="both", expand="true", padx=4, pady=4)
    
    
    LabelC1 = tk.LabelFrame(board, text="player2", height = 100, width = 150)
    LabelC1.pack()
    LabelC1.place(x = 600, y= 5)
    timer1  = Countdown(LabelC1)
    timer1.pack(padx = 30, pady = 10)
    
    LabelC2 = tk.LabelFrame(board, text="player1", height = 100, width = 150)
    LabelC2.pack()
    LabelC2.place(x = 600, y= 450)
    timer2  = Countdown(LabelC2)
    timer2.pack(padx = 30, pady = 10)


    state = GameState(board, [Player(0), Player(1)])
    #for sq in board.squares.values():
    #    print(sq)
    root.geometry('1000x600')
    root.resizable(width=0, height=0)
    root.mainloop()

