class Solution(object):
    def isValid(self,x):
        if x.count("\'") == 2:
            return True
        else:
            return False

object = Solution()
print(object.isValid("\'\'"))