##2558137
##2744075
##2663211
from reconchess import *
from reconchess.utilities import without_opponent_pieces, is_illegal_castle
import chess
import chess.variant


def get_legal_moves(board):
    """
    Generate all valid moves for the current board position under RBC rules.

    RBC moves include three categories:
      1. The null move (no piece is moved, encoded as '0000').
      2. Pseudolegal moves (standard moves where the king may remain in check).
      3. RBC-specific castling moves (opponent may attack squares between king/rook).

    Args:
        board (chess.Board): The current board position.

    Returns:
        set[chess.Move]: All valid RBC moves for the position.
    """
    moves = set()

    # 1. Null move — represents doing nothing this turn
    moves.add(chess.Move.null())

    # 2. Pseudolegal moves — all standard piece moves, including ones that
    #    leave the king in check (legal in RBC since the goal is to capture the king)
    for move in board.pseudo_legal_moves:
        moves.add(move)

    # 3. RBC castling moves — uses a board stripped of opponent pieces to
    #    bypass the standard restriction on castling through attacked squares,
    #    then filters out moves that are still illegal under RBC rules
    for move in without_opponent_pieces(board).generate_castling_moves():
        if not is_illegal_castle(board, move):
            moves.add(move)

    return moves


def next_states(fen):
    """
    Return all valid RBC moves from a given position, sorted alphabetically.

    Args:
        fen (str): The current board position as a FEN string.

    Returns:
        list[str]: Sorted list of valid moves in UCI format (e.g. 'e2e4', '0000').
    """
    board = chess.Board(fen)
    results = []

    for move in get_legal_moves(board):
        results.append(str(move))

    results.sort()
    return results


def next_positions(fen):
    """
    Return all possible next board positions reachable from a given position.

    Each position is the result of applying one valid RBC move (including the
    null move) to the current board. Duplicate positions are removed.

    Args:
        fen (str): The current board position as a FEN string.

    Returns:
        list[str]: Sorted list of resulting positions as FEN strings.
    """
    board = chess.Board(fen)
    result = []

    for move in get_legal_moves(board):
        # Work on a copy so the original board is not modified
        board_copy = board.copy()
        board_copy.push(move)
        result.append(board_copy.fen())

    # Remove duplicates (e.g. null move may produce same FEN as another move)
    # and sort alphabetically
    return sorted(set(result))


if __name__ == "__main__":
    # Read the current board position from stdin
    fen = input().strip()

    # Print each possible next position on its own line
    for position in next_positions(fen):
        print(position)