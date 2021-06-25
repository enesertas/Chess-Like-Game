#Chess-like game
import sys
input_file = open(sys.argv[1], "rt")

board = [
        [["R1", "a8"], ["N1", "b8"], ["B1", "c8"], ["QU", "d8"], ["KI", "e8"], ["B2", "f8"], ["N2", "g8"], ["R2", "h8"]], 
        [["P1", "a7"], ["P2", "b7"], ["P3", "c7"], ["P4", "d7"], ["P5", "e7"], ["P6", "f7"], ["P7", "g7"], ["P8", "h7"]], 
        [["  ", "a6"], ["  ", "b6"], ["  ", "c6"], ["  ", "d6"], ["  ", "e6"], ["  ", "f6"], ["  ", "g6"], ["  ", "h6"]], 
        [["  ", "a5"], ["  ", "b5"], ["  ", "c5"], ["  ", "d5"], ["  ", "e5"], ["  ", "f5"], ["  ", "g5"], ["  ", "h5"]], 
        [["  ", "a4"], ["  ", "b4"], ["  ", "c4"], ["  ", "d4"], ["  ", "e4"], ["  ", "f4"], ["  ", "g4"], ["  ", "h4"]], 
        [["  ", "a3"], ["  ", "b3"], ["  ", "c3"], ["  ", "d3"], ["  ", "e3"], ["  ", "f3"], ["  ", "g3"], ["  ", "h3"]], 
        [["p1", "a2"], ["p2", "b2"], ["p3", "c2"], ["p4", "d2"], ["p5", "e2"], ["p6", "f2"], ["p7", "g2"], ["p8", "h2"]], 
        [["r1", "a1"], ["n1", "b1"], ["b1", "c1"], ["qu", "d1"], ["ki", "e1"], ["b2", "f1"], ["n2", "g1"], ["r2", "h1"]]
        ]
initial_board = [
        [["R1", "a8"], ["N1", "b8"], ["B1", "c8"], ["QU", "d8"], ["KI", "e8"], ["B2", "f8"], ["N2", "g8"], ["R2", "h8"]], 
        [["P1", "a7"], ["P2", "b7"], ["P3", "c7"], ["P4", "d7"], ["P5", "e7"], ["P6", "f7"], ["P7", "g7"], ["P8", "h7"]], 
        [["  ", "a6"], ["  ", "b6"], ["  ", "c6"], ["  ", "d6"], ["  ", "e6"], ["  ", "f6"], ["  ", "g6"], ["  ", "h6"]], 
        [["  ", "a5"], ["  ", "b5"], ["  ", "c5"], ["  ", "d5"], ["  ", "e5"], ["  ", "f5"], ["  ", "g5"], ["  ", "h5"]], 
        [["  ", "a4"], ["  ", "b4"], ["  ", "c4"], ["  ", "d4"], ["  ", "e4"], ["  ", "f4"], ["  ", "g4"], ["  ", "h4"]], 
        [["  ", "a3"], ["  ", "b3"], ["  ", "c3"], ["  ", "d3"], ["  ", "e3"], ["  ", "f3"], ["  ", "g3"], ["  ", "h3"]], 
        [["p1", "a2"], ["p2", "b2"], ["p3", "c2"], ["p4", "d2"], ["p5", "e2"], ["p6", "f2"], ["p7", "g2"], ["p8", "h2"]], 
        [["r1", "a1"], ["n1", "b1"], ["b1", "c1"], ["qu", "d1"], ["ki", "e1"], ["b2", "f1"], ["n2", "g1"], ["r2", "h1"]]
        ]

w_team = ["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8", "r1", "n1", "b1", "qu", "ki", "b2", "n2", "r2"]
b_team = ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8", "R1", "N1", "B1", "QU", "KI", "B2", "N2", "R2"]
pawn = ["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8", "P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8"]
knight = ["n1", "n2", "N1", "N2"]
bishop = ["b1", "b2", "B1", "B2"]
rook = ["r1", "r2", "R1", "R2"]
queen = ["qu", "QU"]
king = ["ki", "KI"]

def initialize():
    global board
    board = initial_board

def find_inside_position(row, column):
    return board[row-1][column-1][1]

def find_a_piece(piece):
    row = 0
    column = 0
    for a in board:
        row += 1
        for r in a:
            column += 1
            if piece in r[0]:
                if column%8 == 0:
                    return row, 8
                else:
                    return row, (column)%(8)

def find_a_position(position):
    row = 0
    column = 0
    for a in board:
        row += 1
        for r in a:
            column += 1
            if position in r:
                if column%8 == 0:
                    return row, 8
                else:
                    return row, (column)%(8)

def command_printer(command):
    a = "> "
    for i in command:
        a += i 
        a += " "
    print(a)

def board_printer():
    a = ""
    for i in range(8):
        for j in range(8):
            a += board[i][j][0]
            a += " "
        a += "\n"
    a = a.strip("\n")
    print("-"*23)
    
    print(a)
    print("-"*23)
def is_empty(row, column):
    if  0 < row < 9 and 0 < column < 9:
        if board[row-1][column-1][0] == "  ":
            return True
        else:
            return False
    else:
        return False

def is_white(row, column):
    if  0 < row < 9 and 0 < column < 9:
        if board[row-1][column-1][0] in w_team:
            return True
        else:
            return False
    else:
        return False

def is_black(row, column):
    if  0 < row < 9 and 0 < column < 9:
        if board[row-1][column-1][0] in b_team:
            return True
        else:
            return False
    else:
        return False

def replace(old_r, old_c, row, column, piece):
    board[row-1][column-1][0] = piece
    board[old_r-1][old_c-1][0] = "  "

def move(piece, position):
    row, column = find_a_piece(piece)
    new_row, new_column = find_a_position(position)
    replace(row, column, new_row, new_column, piece)

def possible_moves_printer(_list):
    temp_list = []
    for i in _list:
        i = find_inside_position(i[0], i[1])
        temp_list.append(i)
    temp_list.sort()
    temp_str = ""
    for i in temp_list:
        temp_str += i
        temp_str += " "
    print(temp_str)

def possible_moves_list_printer(_list):
    _list.sort()
    temp_str = ""
    for i in _list:
        temp_str += i
        temp_str += " "
    print(temp_str)

def kings_thrones():
    a, b = find_a_piece("ki")
    c, d = find_a_piece("KI")
    kings_positions = []
    kings_positions.append(find_inside_position(a, b))
    kings_positions.append(find_inside_position(c, d))
    return kings_positions

def possible_moves_convert_list(_tuple):
    _list_2 = []
    for i in _tuple:
        i = find_inside_position(i[0], i[1])
        if i == kings_thrones()[0] or i == kings_thrones()[1]:
            continue
        else:
            _list_2.append(i)
    return _list_2

def sub_pos_mov(piece, possibilities_w, possibilities_b):
    l_possible_moves = []
    if piece in w_team:
        for i in possibilities_w:
            if is_empty(i[0], i[1]) or is_black(i[0], i[1]):
                l_possible_moves.append(i)
    elif piece in b_team:
        for i in possibilities_b:
            if is_empty(i[0], i[1]) or is_white(i[0], i[1]):
                l_possible_moves.append(i)
    return l_possible_moves

#following functions checks all the possible squares that queen rook and bishop can go and appends until they can't
def qu_bi_ro_dir_w(_list):
    _list_ = []
    for i in _list:
        if is_empty(i[0], i[1]):
            _list_.append(i)
        elif is_black(i[0], i[1]):
            _list_.append(i)
            break
        else:
            break
    return _list_
def qu_bi_ro_dir_b(_list):
    _list_ = []
    for i in _list:
        if is_empty(i[0], i[1]):
            _list_.append(i)
        elif is_white(i[0], i[1]):
            _list_.append(i)
            break
        else:
            break
    return _list_

#following functions are getting possible moves for bishop rook and queen
def sub_pos_mov_kn(piece, possibilities_w, possibilities_b, diagonals):
    l_possible_moves = []
    if piece in w_team:
        for i in possibilities_w:
            if is_empty(i[0], i[1]) or is_black(i[0], i[1]):
                l_possible_moves.append(i)
        for i in diagonals:
            if is_empty(i[0], i[1]):
                l_possible_moves.append(i)
    elif piece in b_team:
        for i in possibilities_b:
            if is_empty(i[0], i[1]) or is_white(i[0], i[1]):
                l_possible_moves.append(i)
        for i in diagonals:
            if is_empty(i[0], i[1]):
                l_possible_moves.append(i)
    return l_possible_moves
def sub_pos_mov_qu(piece, up, urd, right, rdd, down, dld, lud, left):
    possible_moves_list = []
    if piece in w_team:
        possible_moves_list += qu_bi_ro_dir_w(up)
        possible_moves_list += qu_bi_ro_dir_w(urd)
        possible_moves_list += qu_bi_ro_dir_w(right)
        possible_moves_list += qu_bi_ro_dir_w(rdd)
        possible_moves_list += qu_bi_ro_dir_w(down)
        possible_moves_list += qu_bi_ro_dir_w(dld)
        possible_moves_list += qu_bi_ro_dir_w(left)
        possible_moves_list += qu_bi_ro_dir_w(lud)
    elif piece in b_team:
        possible_moves_list += qu_bi_ro_dir_b(up)
        possible_moves_list += qu_bi_ro_dir_b(urd)
        possible_moves_list += qu_bi_ro_dir_b(right)
        possible_moves_list += qu_bi_ro_dir_b(rdd)
        possible_moves_list += qu_bi_ro_dir_b(down)
        possible_moves_list += qu_bi_ro_dir_b(dld)
        possible_moves_list += qu_bi_ro_dir_b(left)
        possible_moves_list += qu_bi_ro_dir_b(lud)
    return possible_moves_list
def sub_pos_mov_ro(piece, up, right, down, left):
    possible_moves_list = []
    if piece in w_team:
        possible_moves_list += qu_bi_ro_dir_w(up)
        possible_moves_list += qu_bi_ro_dir_w(right)
        possible_moves_list += qu_bi_ro_dir_w(down)
        possible_moves_list += qu_bi_ro_dir_w(left)
    elif piece in b_team:
        possible_moves_list += qu_bi_ro_dir_b(up)
        possible_moves_list += qu_bi_ro_dir_b(right)
        possible_moves_list += qu_bi_ro_dir_b(down)
        possible_moves_list += qu_bi_ro_dir_b(left)
    return possible_moves_list
def sub_pos_mov_bi(piece, urd, rdd, dld, lud):
    possible_moves_list = []
    if piece in w_team:
        possible_moves_list += qu_bi_ro_dir_w(urd)
        possible_moves_list += qu_bi_ro_dir_w(lud)
    elif piece in b_team:
        possible_moves_list += qu_bi_ro_dir_b(rdd)
        possible_moves_list += qu_bi_ro_dir_b(dld)
    return possible_moves_list

def check_if_legal(move, movelist):
    if move in kings_thrones():
        return False
    elif move in movelist:
        return True
    else:
        return False
#following function checks a piece and type and uses necessary functions for each piece and returns a list of possible moves
def possible_moves(piece):
    if piece in pawn:
        row, column = find_a_piece(piece)
        l_possibles = sub_pos_mov(piece, [(row-1, column)], [(row+1, column)])
        return l_possibles
    elif piece in knight:
        row, column = find_a_piece(piece)
        l_possibles = sub_pos_mov_kn(piece, 
        [(row+1,column+2), (row+1,column-2), (row-1,column+2), (row-1,column-2), 
        (row-2,column+1), (row-2,column-1), (row+2,column+1), (row+2,column-1)], 
        [(row+1,column+2), (row+1,column-2), (row-1,column+2), (row-1,column-2), 
        (row-2,column+1), (row-2,column-1), (row+2,column+1), (row+2,column-1)], 
        [(row-1, column-1), (row+1, column-1), (row+1, column+1), (row-1, column+1)])
        return l_possibles
    elif piece in king:
        row, column = find_a_piece(piece)
        l_possibles = sub_pos_mov(piece, 
        [(row+1, column+1), (row+1, column), (row+1, column-1), (row, column-1), 
        (row, column+1), (row-1, column+1), (row-1, column), (row-1, column-1)], 
        [(row+1, column+1), (row+1, column), (row+1, column-1), (row, column-1), 
        (row, column+1), (row-1, column+1), (row-1, column), (row-1, column-1)])
        return l_possibles
    elif piece in queen:
        row, column = find_a_piece(piece)
        l_possibles = sub_pos_mov_qu(piece, 
        [(row-1, column), (row-2, column), (row-3, column), (row-4, column), 
        (row-5, column), (row-6, column), (row-7, column)], #upward moves
        [(row-1, column+1), (row-2, column+2), (row-3, column+3), (row-4, column+4), 
        (row-5, column+5), (row-6, column+6), (row-7, column+7)], #up-right diagonal moves
        [(row, column+1), (row, column+2), (row, column+3), (row, column+4), 
        (row, column+5), (row, column+6), (row, column+7)], # right moves
        [(row+1, column+1), (row+2, column+2), (row+3, column+3), (row+4, column+4), 
        (row+5, column+5), (row+6, column+6), (row+7, column+7)], #right down diagonal moves
        [(row+1, column), (row+2, column), (row+3, column), (row+4, column), 
        (row+5, column), (row+6, column), (row+7, column)], # down moves
        [(row+1, column-1), (row+2, column-2), (row+3, column-3), (row+4, column-4), 
        (row+5, column-5), (row+6, column-6), (row+7, column-7)], # down left diagonal
        [(row, column-1), (row, column-2), (row, column-3), (row, column-4), 
        (row, column-5), (row, column-6), (row, column-7)], # left
        [(row-1, column-1), (row-2, column-2), (row-3, column-3), (row-4, column-4), 
        (row-5, column-5), (row-6, column-6), (row-7, column-7)] #left up diagonal
        )
        return l_possibles
    elif piece in rook:
        row, column = find_a_piece(piece)
        l_possibles = sub_pos_mov_ro(piece, 
        [(row-1, column), (row-2, column), (row-3, column), (row-4, column), 
        (row-5, column), (row-6, column), (row-7, column)], 
        [(row, column+1), (row, column+2), (row, column+3), (row, column+4), 
        (row, column+5), (row, column+6), (row, column+7)], 
        [(row+1, column), (row+2, column), (row+3, column), (row+4, column), 
        (row+5, column), (row+6, column), (row+7, column)], 
        [(row, column-1), (row, column-2), (row, column-3), (row, column-4), 
        (row, column-5), (row, column-6), (row, column-7)])
        return l_possibles
    elif piece in bishop:
        row, column = find_a_piece(piece)
        l_possibles = sub_pos_mov_bi(piece,    
        [(row-1, column+1), (row-2, column+2), (row-3, column+3), (row-4, column+4), 
        (row-5, column+5), (row-6, column+6), (row-7, column+7)],
        [(row+1, column+1), (row+2, column+2), (row+3, column+3), (row+4, column+4), 
        (row+5, column+5), (row+6, column+6), (row+7, column+7)],
        [(row+1, column-1), (row+2, column-2), (row+3, column-3), (row+4, column-4), 
        (row+5, column-5), (row+6, column-6), (row+7, column-7)],
        [(row-1, column-1), (row-2, column-2), (row-3, column-3), (row-4, column-4), 
        (row-5, column-5), (row-6, column-6), (row-7, column-7)])
        return l_possibles

#following code uses necessary functions and prints the output for each command
list_input = input_file.read().splitlines()
c = 0
for i in list_input:
    list_input[c] = list_input[c].split(" ")
    c += 1
for i in list_input:
    command_printer(i)
    if i[0] == "move":
        if check_if_legal(i[2], possible_moves_convert_list(possible_moves(i[1]))):
            move(i[1], i[2])
            print("OK")
        else:
            print("FAILED")
    elif i[0] == "print":
        board_printer()
    elif i[0] == "showmoves":
        if len(possible_moves_convert_list(possible_moves(i[1]))) == 0:
            print("FAILED")
        else:
            possible_moves_list_printer(possible_moves_convert_list(possible_moves(i[1])))
    elif i[0] == "initialize":
        initialize()
        board_printer()
    elif i[0] == "exit":
        break