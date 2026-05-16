#students number
##2558137
##2744075
##2663211

import chess

n = int(input())

states = []

for _ in range(n):
    states.append(input())

window = input()

observations = window.split(";")

valid_states = []

for fen in states:

    board = chess.Board(fen)

    valid = True

    for observation in observations:

        square_name, expected = observation.split(":")

        square = chess.parse_square(square_name)

        piece = board.piece_at(square)

        
        if expected == "?":
            if piece is not None:
                valid = False
                break

       
        else:
            if piece is None or piece.symbol() != expected:
                valid = False
                break

    if valid:
        valid_states.append(fen)

valid_states.sort()

for state in valid_states:
    print(state)