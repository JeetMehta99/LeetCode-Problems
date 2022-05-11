# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """
class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        def goBack():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
        
        # need the curr direction so to know dir robot is facing
        def backTrack(x, y, d):
            robot.clean()
            for i in range(4):
                new_d = (d+i) % 4 # clockwise dir. if cur is 3 then next is 3+i 
                new_x = x+ direction[new_d][0]
                new_y = y + direction[new_d][1]
                if (new_x, new_y) not in seen and robot.move(): # if cur direction if robot can forward. at curr position can robot move up then we just 
                    seen.add((new_x, new_y))
                    backTrack(new_x, new_y, new_d)
                    goBack() # goback to prev state so next for loop will have same initial state
                robot.turnRight()
                
        direction = [(-1, 0), (0, 1), (1, 0), (0, -1)] # Up, R, Down, L
        seen = set()
        seen.add((0, 0))
        backTrack(0, 0, 0)