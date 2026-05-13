##2558137
##2744075
##2663211
from reconchess import *
import chess


def board(state):
    """Convert a FEN string into a chess.Board object."""
    return chess.Board(state)


def MoveExecution(state, move):
    """
    Apply a move to a chess position and return the resulting position.

    Args:
        state (str): The current board position as a FEN string.
        move  (str): The move to apply in UCI format (e.g. 'e2e4', '0000' for null move).

    Returns:
        str: The new board position as a FEN string, or an error message on failure.
    """
    try:
        # Load the board from the FEN string
        board = chess.Board(state)

        # Parse the UCI move string into a Move object.
        # chess.Move.from_uci also handles the null move ('0000').
        uci_move = chess.Move.from_uci(move)

        # Push the move onto the board without a strict legality check,
        # since RBC allows pseudolegal moves (king may remain in check).
        board.push(uci_move)

        # Return the updated board state as a FEN string
        return board.fen()

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    # Read the current board state and the move from stdin
    state = input().strip()
    move = input().strip()

    print(MoveExecution(state, move))