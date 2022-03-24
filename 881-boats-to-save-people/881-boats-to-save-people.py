class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        cnt = 0
        n = len(people)
        people.sort()
        l, r = 0, n -1
        people.sort()
        while l <= r :
            if people[r]==limit or people[l]+people[r]>limit:
                r -= 1
                cnt +=1 
            else:
                l += 1
                r -= 1
                cnt += 1
        return cnt
        
            
            
        