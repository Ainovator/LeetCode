class Solution(object):
    def isPalindrome(self,x):
        return str(x) == str(x)[::-1]
    
object = Solution()
print(object.isPalindrome(323))