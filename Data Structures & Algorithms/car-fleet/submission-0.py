class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        length = len(position)
        for i in range(length):
            cars.append([position[i], speed[i]])
        cars.sort()
        fleets = 0
        moves = 0
        length -= 1
        while length >= 0 :
            if not moves:
                moves = (target - cars[length][0]) / cars[length][1]
                fleets += 1
            else:
                curMoves = (target - cars[length][0]) / cars[length][1]
                if curMoves <= moves:
                    length -= 1
                    cars.pop()
                else:
                    moves = 0
        return fleets