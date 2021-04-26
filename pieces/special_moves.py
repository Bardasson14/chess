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
       board.capture_piece(GameState.possible_en_passant)
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
        keys = get_canvas_keys(board.children)
        self.selected_piece = PIECES_EN[board.children[keys[0]].curselection()[0]]
        for key in keys:
            board.children[key].destroy()
        self.set_piece(board, original_pawn, row, col, sprites)
        board.lock=False

    def set_piece(self, board, original_pawn, row, col, sprites): 
        piece_class = self.selected_piece.title()
        board.canvas.delete(original_pawn.name)
        player_color = original_pawn.color
        modified_pawn = deepcopy(original_pawn)
        modified_pawn = globals()[piece_class](player_color, player_color + '_' + self.selected_piece + '_')
        index = PIECES_EN.index(self.selected_piece)
        filename = player_color + (get_piece_type(modified_pawn.name)).title()
        modified_pawn.name += str(self.promoted[index])
        ####print(self.promoted)
        self.promoted[index] += 1
        modified_pawn.sprite_dir = 'assets/img/' + filename  + '.png'
        ####print("DICT: ", modified_pawn.__dict__)
        board.add_piece(modified_pawn, row, col)

    def movRoque(self,board,gr,coord):
        piece = board.squares[coord]['piece']
        print(str(piece)+str(coord))
        if(gr=='lr'):
            if(piece.color=='white'):
                reftorre=(7,7)
                torre=board.squares[reftorre]['piece']
            else:
                reftorre=(0,7)
                torre=board.squares[reftorre]['piece']
            board.place_piece(torre,coord[0],coord[1]-1)
            board.squares[reftorre]['piece'] = None
        else:
            if(piece.color=='white'):
                reftorre=(7,0)
                torre=board.squares[reftorre]['piece']
            else:
                reftorre=(0,0)
                torre=board.squares[reftorre]['piece']
            board.place_piece(torre,coord[0],coord[1]+1)
            board.squares[reftorre]['piece'] = None
