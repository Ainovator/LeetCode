class Solution(object):
    def twoSum(self, nums, target):
        for i, num in enumerate(nums):
            # Вычисление второго слагаемого
            partner_num = target - num
            # Если число есть, добавляем в массив количество вариаций
            if partner_num in nums[i+1:]:
                # Используем enumerate для получения индексов
                partner_index = nums.index(partner_num, i + 1)
                return i, partner_index
            else:
                pass

object = Solution()
answer = object.twoSum([3, 3], 6)
print(answer)



