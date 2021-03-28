from utils import *
from pieces.bishop import Bishop
from pieces.king import King
from pieces.knight import Knight
from pieces.pawn import Pawn 
from pieces.queen import Queen
from pieces.rook import Rook
from copy import deepcopy
from game_state import GameState

PIECES_EN = ['bishop', 'knight', 'queen', 'rook']
PIECES_PT = ['Bispo', 'Cavalo', 'Rainha', 'Torre']

class SpecialMoves:

    promoted = [3,3,2,3]

    def __init__(self):
        self.selected_piece = None
    
    def en_passant(self, board, piece, row, col, ref):
       board.pieceCapture(GameState.possible_en_passant)
       board.squares[GameState.possible_en_passant]['piece'] = None
       
    def pawn_promotion(self, board, original_pawn, row, col, sprites):
        listbox = tk.Listbox(board, selectmode = 'single', width = 7, height=6)
        listbox.pack(expand = True, fill = "both")
        label = tk.Label(board, text = "Selecione a peça na qual o peão se transformará")
        label.pack()
        for piece in PIECES_PT:
            listbox.insert(listbox.size(), piece)
        submit = tk.Button(master = board, text = "Escolher", command = lambda: self.destroy_promotion_menu(board, original_pawn, row, col, sprites))
        submit.pack()

    def destroy_promotion_menu(self, board, original_pawn, row, col, sprites):  
        listbox_key = '!listbox'
        label_key = '!label'
        button_key = '!button'
        i = 1

        while listbox_key not in board.children:
            i+=1
            listbox_key = "!listbox{}".format(i)
            
        if (i!=1):
            label_key = "!label{}".format(i)
            button_key = "!button{}".format(i)

        self.selected_piece = PIECES_EN[board.children[listbox_key].curselection()[0]]
        board.children[listbox_key].destroy()
        board.children[label_key].destroy()
        board.children[button_key].destroy()
        self.set_piece(board, original_pawn, row, col, sprites)

    def set_piece(self, board, original_pawn, row, col, sprites): 
        piece_class = self.selected_piece.title()
        print("piece_class: ", self.selected_piece)
        board.canvas.delete(original_pawn.name)
        del sprites[original_pawn.spriteID]
        player_color = original_pawn.color
        modified_pawn = deepcopy(original_pawn)
        modified_pawn = globals()[piece_class](player_color, player_color + '_' + self.selected_piece)
        index = PIECES_EN.index(self.selected_piece)
        modified_pawn.name += str(self.promoted[index])
        self.promoted[index] += 1
        filename = player_color + (get_piece_type(modified_pawn.name)).title()
        modified_pawn.sprite_dir = 'assets/img/' + filename  + '.png'
        board.addPiece(modified_pawn, row, col)
        
    def castling(self):
        pass