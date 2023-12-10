class Solution:
    
    #Function to check if two strings are rotations of each other or not.
    def areRotations(self,s1,s2):
        s1=s1+s1
        if s2 in s1:
          return 1
        return 0
