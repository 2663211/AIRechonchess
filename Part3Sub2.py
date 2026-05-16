##2558137
##2744075
##2663211
import chess
import chess.engine
from collections import Counter

engine = chess.engine.SimpleEngine.popen_uci('/opt/stockfish/stockfish', setpgrp=True)


def king_capture(board):
    for sq, piece in board.piece_map().items():
        if piece.piece_type == chess.KING and piece.color != board.turn:
            for move in board.legal_moves:
                if move.to_square == sq:
                    return move
            break
    return None


def get_move(board):
    move = king_capture(board)
    if move:
        return move.uci()

    
    result = engine.play(board, chess.engine.Limit(time=0.05))
    return result.move.uci()


if __name__ == "__main__":
    n = int(input().strip())

    freq = Counter()

    for _ in range(n):
        board = chess.Board(input().strip())
        move = get_move(board)
        freq[move] += 1

    best = max(freq.values())
    best_moves = [m for m in freq if freq[m] == best]

    print(sorted(best_moves)[0], flush=True)

engine.quit()