# Определение класса ListNode
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1=[], l2=[]):
        
        
        # Проверим, если переданы списки, иначе установим пустые списки
        l1 = l1 if l1 is not None and isinstance(l1, list) else []
        l2 = l2 if l2 is not None and isinstance(l2, list) else []

        # Если списки не пустые, выполним реверс и построим числа
        if l1:
            l1 = list(reversed(l1))
            num_1 = ""
            for num in range(len(l1)):
                num_1 = str(num_1)  + str(l1[num])
            
        if l2:
            l2 = list(reversed(l2))
            num_2 = ""
            for num in range(len(l2)):
                num_2 = str(num_2)+ str(l2[num])
            
                
        if l1 and l2:
            total_sum = str(int(num_1) + int(num_2))
            clear_sum = []
            for num in total_sum[::-1]:
                clear_sum.append(int(num))
            return clear_sum
            


object = Solution()
answer = object.addTwoNumbers([2,4,3],[5,6,4])
print(answer)