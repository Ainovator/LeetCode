class Solution(object):
    def plusOne(self, digits):
        num_str = ''.join(map(str, digits))
        num_str = int(num_str) + 1
        return num_str
           
object = Solution()
print(object.plusOne([9,8,7]))