# The Hill Climbing with restarts algorithm

import random
import NQProblem
import copy
import numpy as np

# The HillClimbingRestarts program implements hill-climbing with restarts algorithm. 


class HillClimbingRestarts:
    initialstate = 0
    
    def __init__(self, state, heuristic):
        self.initialState = state
        self.heuristicFunc = heuristic
        self.initialdisQ = copy.deepcopy(state.disQ)
    # This method is used to calculate heuristic value
    # @param self - The object of the class
    # @return nothing
    def heuristicValue(self):
        return (self.initialState.getAttacksNum() + self.heuristicFunc)
    
    # This method is used to get best moves if we just move one of the queens
    # @param self - The object of the class
    # @return self.initialState.disQ - The distribution of queens
    # @return cost - The cost of the N-queen problem
    def getBestMoves(self):
        moves = {}
        bestMoves = []
        intialHeuristicValue = self.heuristicValue()
        for col in range(0,self.initialState.numQ):
            for row in range(0,self.initialState.numQ):
                boardCopy = copy.deepcopy(self.initialState)
                if boardCopy.disQ[col] == row:
                    continue
        #Move the queen to the new row
                boardCopy.disQ[col] = row
                newBoard = NQProblem.NQProblem(boardCopy.numQ,boardCopy.disQ)
                moves[(col,row)] = newBoard.getAttacksNum() + self.heuristicFunc
        # Find the best moves
        for k,v in moves.items():
            if v < intialHeuristicValue:
                intialHeuristicValue = v
       
        for k,v in moves.items():
            if v == intialHeuristicValue:
                bestMoves.append(k)
                
        if len(bestMoves) > 0:
            pick = random.randint(0,len(bestMoves) - 1)
            col = bestMoves[pick][0]
            row = bestMoves[pick][1]
            self.initialState.disQ[col] = row
        # Calculate the cost of the N-queen problem
        cost = NQProblem.NQProblem(self.initialState.numQ,self.initialState.disQ).getAttacksNum() + self.heuristicFunc
        return (self.initialState.disQ, cost)
    
    
    # This is the method to calculate the cost of the best moves
    # @param self - The object of the class
    # @return pathCost - The cost of the best moves
    def pathCost(self):
        bestMoves = []
        bestMoves = np.array(self.getBestMoves()[0])
        initialdisQ = np.array(self.initialdisQ)
        pathCost = sum((initialdisQ - bestMoves)**2)
        return(pathCost)

