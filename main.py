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

def find_sum(list_nums):
    for num in range(len(list_nums)):
        print(num)


print("<Input target in next line>")
target_set = select_num()
new_object = Solution(target=target_set)

while not step_check(input_step):
    input_step = input("<Do you want random list? (y/n)>")

if input_step == "y":
    new_object.nums.extend(generate_random_list())
else:
    new_object.new_nums()

find_sum(new_object.nums)
new_object.display_all_info()