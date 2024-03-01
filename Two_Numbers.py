class Solution(object):
    def addTwoNumbers(self, l1=[], l2=[]):
        num_1, num_2 = 0, 0

        # Проверим, если переданы списки, иначе установим пустые списки
        l1 = l1 if l1 is not None and isinstance(l1, list) else []
        l2 = l2 if l2 is not None and isinstance(l2, list) else []
        
        # Если списки не пустые, выполним реверс
        if l1:
            l1 = list(reversed(l1))
            for num in range(len(l1)):
                num_1 = num_1 * 10 + l1[num]
        if l2:
            l2 = list(reversed(l2))
            for num in range(len(l2)):
                num_2 = num_2 * 10 + l2[num]
       
        sum_result = num_1 + num_2

        return sum_result

# Пример использования
object = Solution()
print(object.addTwoNumbers([2,4,3], [5,6,4]))
