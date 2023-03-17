

from turtle import right


def apartment_hunting(blocks):
    '''
    I am using two pass technique
    1. First I come the right end to left end and calculate optimal distance towards the right from each index
    2. Next I go from left end to right end and calculate optimal distance toward the left end.
        While doing the second step, I calculate the max distance to travel from the specific index to cover all requirements
        if the max distance is smaller the optimal distance I will update the optimal block index
    Finally I will return the optimal index
    
    '''
    req = ["gym","school","store"]
    n = len(blocks)
    rightOptimalDistance = [[0,0,0] for _ in range(n)]
    optimalDistance = [float("inf"),float("inf"),float("inf")]
    #step 1 - Moving from right to left
    #And calculation optimal distance towards the right from the index
    for i in range(n-1,-1,-1):
        optimalDistance = [
            0 if blocks[i]["gym"] else optimalDistance[0]+1,
            0 if blocks[i]["school"] else optimalDistance[1]+1,
            0 if blocks[i]["store"] else optimalDistance[2]+1
        ]
        rightOptimalDistance[i] = optimalDistance
    
    
    optimalDistance = float("inf")
    optimalIndex = 0
    leftOptimalDistance = [float("inf"),float("inf"),float("inf")]
    #step 2 - moving from the left end to right end
    for i in range(n):
        leftOptimalDistance = [
            0 if blocks[i]["gym"] else leftOptimalDistance[0]+1,
            0 if blocks[i]["school"] else leftOptimalDistance[1]+1,
            0 if blocks[i]["store"] else leftOptimalDistance[2]+1
        ]

        #here we calculate the max distance to travel, to reach all the requirements
        maxDistanceToTravel = 0
        for j in range(3):  #["gym","school","store"]
            maxDistanceToTravel = max(maxDistanceToTravel,min(leftOptimalDistance[j],rightOptimalDistance[i][j]))
            #min is to calculate the minimum distance in left and right distances that are calculated
            #from the minimum distances calculated, we find max distance
            
        #if the max distance to travel is less than the optimal distance, we will update the optimal index
        if maxDistanceToTravel<optimalDistance:
            optimalDistance = maxDistanceToTravel
            optimalIndex = i
    return optimalIndex

blocks = [
  {
    "gym": False,
    "school": True,
    "store": False,
  },
  {
    "gym": True,
    "school": False,
    "store": False,
  },
  {
    "gym": True,
    "school": True,
    "store": False,
  },
  {
    "gym": False,
    "school": True,
    "store": False,
  },
  {
    "gym": False,
    "school": True,
    "store": True,
  },
]
print(apartment_hunting(blocks))  #3



