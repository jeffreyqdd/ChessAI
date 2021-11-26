from chess import Board
from keras import Model
import math
import numpy as np

# from src.processing.translate import Translate

# class SearchFramework:
#     def __init__(self, model:Model):
#         self.model:Model = model
    

#     def alphabeta(self, node:Board, eval:float, depth:int, alpha:float, beta:float, maximizing_player:bool):
#         if depth == 0 or node.is_game_over():
#             return eval

#         if maximizing_player:
#             value = math.inf

#             # generate positions
#             positions = []
#             for move in node.legal_moves:
#                 node.push(move)
#                 positions.append(Translate.matrix2d_to_matrix3d(
#                     Translate.board_to_matrix2d(board=node)
#                 ))
#                 node.pop()
#             positions = np.array(positions)

#             # general evaluations of the posision
#             evaluations = self.model.predict(positions)

#             #     value = max(value, self.alphabeta(node, ))
#         else:
#             pass

# from chess import Board


        

# '''
# function alphabeta(node, depth, α, β, maximizingPlayer) is
#     if depth = 0 or node is a terminal node then
#         return the heuristic value of node
#     if maximizingPlayer then
#         value := −∞
#         for each child of node do
#             value := max(value, alphabeta(child, depth − 1, α, β, FALSE))
#             if value ≥ β then
#                 break (* β cutoff *)
#             α := max(α, value)
#         return value
#     else
#         value := +∞
#         for each child of node do
#             value := min(value, alphabeta(child, depth − 1, α, β, TRUE))
#             if value ≤ α then
#                 break (* α cutoff *)
#             β := min(β, value)
#         return value
# '''