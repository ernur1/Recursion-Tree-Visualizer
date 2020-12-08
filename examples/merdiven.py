
"""
Playing With Stairs
Imagine you want to determine all the different ways you can reach a specific stair in a staircase by hopping one, two, or three stairs at a time. How many paths are there to the fourth stair? Here are all the different combinations:
"""
from visualiser.visualiser import Visualiser as vs

from functools import lru_cache
from timeit import repeat
@lru_cache(maxsize=None)

def steps_to(stair):
    if stair == 1:
        # You can reach the first stair with only a single step
        # from the floor.
        return 1
    elif stair == 2:
        # You can reach the second stair by jumping from the
        # floor with a single two-stair hop or by jumping a single
        # stair a couple of times.
        return 2
    elif stair == 3:
        # You can reach the third stair using four possible
        # combinations:
        # 1. Jumping all the way from the floor
        # 2. Jumping two stairs, then one
        # 3. Jumping one stair, then two
        # 4. Jumping one stair three times
        return 4
    else:
        # You can reach your current stair from three different places:
        # 1. From three stairs down
        # 2. From two stairs down
        # 2. From one stair down
        #
        # If you add up the number of ways of getting to those
        # those three positions, then you should have your solution.
        return (
            steps_to(stair - 3)
            + steps_to(stair - 2)
            + steps_to(stair - 1)
        )

#for x in range(1,15):
x=10
print(x, steps_to(x))


#setup_code = "from __main__ import steps_to"
#stmt = "steps_to(30)"
#times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)
#print(f"Minimum execution time: {min(times)}")