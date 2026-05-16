#students number
##2558137
##2744075
##2663211

import chess
from reconchess.utilities import without_opponent_pieces, is_illegal_castle

fen = input()
capture_square_input = input()

board = chess.Board(fen)

target = chess.parse_square(capture_square_input)

moves = list(board.pseudo_legal_moves)


for move in without_opponent_pieces(board).generate_castling_moves():
    if not is_illegal_castle(board, move):
        if move not in moves:
            moves.append(move)

states = []

for move in moves:

    
    if board.is_capture(move) and move.to_square == target:

        new_board = board.copy()
        new_board.push(move)

        states.append(new_board.fen())

states.sort()

for state in states:
    print(state)