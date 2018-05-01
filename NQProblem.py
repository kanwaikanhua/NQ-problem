


# Class to represent N-Queen initial problem
# as well as intermediate states
class NQProblem:
    numQ = 0  # number of Queens
    disQ = [] # distribution of Queens
    numAttacks = -1
    nIdx = (0,0) # next neighbor index

    def __init__(self, numberQ, distributionQ):
        self.numQ = numberQ
        self.disQ = distributionQ[:]

    def getAttacksNum(self):
        if self.numAttacks == -1:
            self.numAttacks = 0
            # account for diagonal attacks
            for i in range(0, self.numQ):
                curQPos = self.disQ[i]
                for j in range(i+1, self.numQ):
                    diagDist = j-i
                    if (self.disQ[j] == curQPos - diagDist) or                       (self.disQ[j] == curQPos + diagDist):
                        self.numAttacks = self.numAttacks + 1
                    
            # account for side attacks
            for i in range(0, self.numQ):
                curQPos = self.disQ[i]
                subL = self.disQ[i+1:]
                self.numAttacks = self.numAttacks + subL.count(curQPos)
        
        return self.numAttacks

    def getNextNeighbour(self):
        neighbour = NQProblem(0,[])
        dist = 0
        c = self.nIdx[0]
        r = self.nIdx[1]
        found = False
        while c < self.numQ and found == False:
            while r < self.numQ and found == False:
                if self.disQ[c] != r+1:
                    newState = self.disQ[:c] + [r+1] + self.disQ[c+1:]
                    dist = abs(self.disQ[c] - (r+1))
                    neighbour = NQProblem(self.numQ, newState)
                    found = True
                r = r+1
                
            if r == self.numQ:
                r = 0
                c = c+1

        self.nIdx = (c,r)

        return (neighbour, dist)

    def getNeighbours(self):
        nghs = []
        nT = self.getNextNeighbour()
        while nT[0].numQ != 0:
            nghs.append(nT)  
            nT = self.getNextNeighbour()

        return nghs

    def test(self):
        print('Number of Queens: ', self.numQ)
        print('Initial state: ', self.disQ)
        print('Number of attacks: ', self.getAttacksNum())

