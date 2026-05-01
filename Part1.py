from reconchess import *
import chess
# def isNumber(s):
#     return s.isdigit()

# def Board(state):
#     state_comp=state.split()
#     if len(state_comp)!=6:
#         return "Error: Invalid FEN structure (expected 6 components)"
#     piece_pos=state_comp[0]
#     rows=piece_pos.split("/")
#     matrix=[]
#     for row_str in rows:
#         row_data=[]
#         for char in row_str:
#             if isNumber(char):
#                 for _ in range(int(char)):
#                     row_data.append(".")
#             else:
#                 row_data.append(char)
#         matrix.append(row_data)
        
# #     for row in matrix:
# #         print(" ".join(row))
# #     return ""
#     return matrix
def board(state):
    return chess.Board(state)

    
def MoveExecution(state, move):
    try:
        board = chess.Board(state)  # load FEN

        uci_move = chess.Move.from_uci(move)

        # Check if move is legal
        if uci_move not in board.legal_moves:
            return "Illegal move"

        board.push(uci_move)  # execute move

        return board.fen()  # return new FEN

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    state = input().strip()
    move = input().strip()
    print(MoveExecution(state, move))