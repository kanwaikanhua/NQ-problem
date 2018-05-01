


import random
import time
import NQProblem
import HillClimbingRestarts


# Running show_full_board funtion will give a board
# @param  board - The distribution of N-Queens 
# @return nothing


def showFullBoard(board):
    for row in range(len(board)):
        line = ""             
        for column in range(len(board)):
            if board[column] == row:
                # Q -the Queens in the problem 
                line += "Q "
                #. - empty Tiles in the board
            else:
                line += ". "
        print(line)
    print("\n") 

# Running this function will give best moves 
# @param numQ - The number of N-Queens
# @param hrFn - The initial heuristic value
# @param reTr - The number of restarts
# @return nothing

def runGreedyHillClimbingAlg(numQ,hrFn,reTr):
    print('')
    print('Running Greedy Hill Climbing Algorithm with NQ = ', numQ, ' \nInitial heuristic value=  ', hrFn, '\nNumber of restarts=', reTr )
    # Set up initial values
    bestBoard={}
    heuristicValues=[]
    #path_cost = []
    startTime = time.clock()
    minHeuristicValue = 0
 
    for i in range(reTr):
        # generate initial state
        distributionQ = random.sample(range(numQ), numQ)
        initialNQP = NQProblem.NQProblem(numQ,distributionQ)
        
        # running Hill climbing with restarts
        hillClimbing = HillClimbingRestarts.HillClimbingRestarts(initialNQP,hrFn)
        tempBestMove = hillClimbing.getBestMoves()[0]
        tempBestHvalue = hillClimbing.getBestMoves()[1]
        tempPathCost = hillClimbing.pathCost()
        
        heuristicValues.append(tempBestHvalue)
        bestBoard[tempBestHvalue] = [tempBestMove,tempPathCost]
    print(bestBoard)
    # Find the best moves based on heuristic value
    minHeuristicValue = min(heuristicValues)
    bestMoves = bestBoard.get(minHeuristicValue)[0]
    pathCostBestMoves = bestBoard.get(minHeuristicValue)[1]

    print( 'The best solution of N-queen problem: %s '%bestMoves)
    showFullBoard(bestMoves)
    print('The heuristic value of the solution: %s'%minHeuristicValue)
    print('The path cost of the solution: %s'%pathCostBestMoves)

    # Heuristic values of all of the restarts
    #print('Heuristic values of all of the restarts: \n %s '%heuristicValues)
    
    # check time
    print('Size of puzzle is %s'%numQ, 'Time-consuming is %s'%(time.clock() - startTime))
    if (time.clock() - startTime) > 10:
        print('')
        print('Running time exceeded 10sec limit, bailing out.')
    

# main
print('Please select how many queens in the problem: ')
numQ = int(input('NQ: '))
hrFn = int(input('Initial heuristic value:'))
reTr = int(input('The number of restarts:'))
runGreedyHillClimbingAlg(numQ,hrFn,reTr)

