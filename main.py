import sqlite3 as sq
from base import select_num, generate_random_list, step_check
#global input next step
input_step = None


class Solution(object):
    def __init__(self, nums = [], target=None):
        self.nums = nums
        self.target = target
    #method to create new list with nums
    def new_nums(self):
        end_this = False
        while not end_this:
            print("Input list lenght: ")
            len_adder = select_num()
            for i in range(len_adder):
                print(f"Input {i} num: ")
                num_adder = select_num()
                self.nums.append(num_adder)
            end_this = True
            print("\n")
    #method to show all atribute info
    def display_all_info(self):
        print(f"You target is: {self.target}.")
        print(f"You num list is: {self.nums}")

def find_sum(list_nums, target):
    for num in list_nums[:-1]:
        #Вычисление второго слогаемого
        partner_num = target - num
        #Количество этого числа в массиве
        count_second_num = new_object.nums[new_object.nums.index(num)+1:].count(partner_num)
        #Если число есть добавляю в массив количество вариаций
        if count_second_num > 0:
            print("Sum from: ", num, partner_num)
        else:
            pass
           
        
        


print("<Input target in next line>")
target_set = select_num()
new_object = Solution(target=target_set)

while not step_check(input_step):
    input_step = input("<Do you want random list? (y/n)>")

if input_step == "y":
    new_object.nums.extend(set(generate_random_list()))
else:
    new_object.new_nums()

find_sum(new_object.nums, target_set)
new_object.display_all_info()