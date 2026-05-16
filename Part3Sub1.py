##2558137
##2744075
##2663211
import chess
import chess.engine


engine = chess.engine.SimpleEngine.popen_uci('/opt/stockfish/stockfish', setpgrp=True)

def find_king_capture(board):
    """
    Returns a move that captures the opponent king if possible.
    """
    opponent_king_square = None

    # find opponent king
    for square, piece in board.piece_map().items():
        if piece.piece_type == chess.KING and piece.color != board.turn:
            opponent_king_square = square
            break

    if opponent_king_square is None:
        return None

    
    for move in board.legal_moves:
        if move.to_square == opponent_king_square:
            return move

    return None


def choose_move(fen):
    board = chess.Board(fen)

    
    king_move = find_king_capture(board)
    if king_move:
        return king_move.uci()

    
    result = engine.play(board, chess.engine.Limit(time=0.5))
    return result.move.uci()


if __name__ == "__main__":
    fen = input().strip()
    print(choose_move(fen))

engine.quit()