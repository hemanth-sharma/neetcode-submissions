class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 1 2 3 4 5 6 7 8 9 10
        # while true
        # i += 3 = 4, 7, 10
        # j += 2 = 6, 8, 10
        # group the fleets 
        # compute the total fleets

        # y = x + time*v
        # (y - x)/v = time -> (10-1)/2 => 9/2 = CEIL(4.5)
        # find time for each car
        # time: [] # store them in hashmap using time as keys? hmm
        # target=12
        # position=[10,8,0,5,3]
        # speed=[2,4,1,1,3]
        # 0 1 2 3 4 5 6 7 8 9 10 11 12
        # i     i   i               ii
        # 10, 8, 5, 3, 0
        # 1, 1, 7, 3, 12 # # 1, 1, 12, 7, 3
        # Hmm sort the cars position and speed then calculate time
        
        cars = sorted(zip(position, speed), reverse=True)
        fleets = 0
        max_time = 0 # slowest time of the front car (cars are sorted by position so slowest so far is highest position one)
        for p, s in cars: 
            time = (target-p)/s

            if time > max_time:
                max_time = time
                fleets += 1
            
        return fleets


