
def initialize_empty_grid():
    squares = {}
    for i in range(8):
        for j in range(8):
            square_info = {'piece': None, 'coord':(i, j), 'selected':None, 'gamerule':None}
            squares[(i,j)] = square_info
    return squares

def fix_sprite_dir(piece):
    previous_dir = piece.sprite_dir
    piece.sprite_dir = os.path.dirname(os.path.realpath(__file__)) + '/../src/' + previous_dir