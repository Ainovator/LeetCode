from base import select_num, generate_random_list, step_check

object_list = []
input_step = None
class Solution(object):
    def __init__(self, nums = [], target = None):
        self.nums = nums
        self.target = target
    def change_target(self):
        end_this = False
        while not end_this:
            try:
                new_target = int(input("You target is: "))
                self.target = new_target
                end_this = True
                print("\n")
            except:
                print("Input only num")
    def new_nums(self):
        end_this = False
        while not end_this:
            try:
                len_adder = int(input("Input length of nums list: "))
                for i in range(len_adder):
                    print_assist = f"Input {i} num: "
                    num_adder = int(input(print_assist))
                    self.nums.append(num_adder)
                end_this = True
                print("\n")
            except:
                    print("Input only nums")
    def display_all_info(self):
        print(f"You target is: {self.target} .")
        print(f"You num list is: {self.nums}")


def first_step():
        if input_step == "y":
            list_set = generate_random_list()
        elif input_step == "n":
            new_object.new_nums()



end_program = False
while not end_program:

    print("Input Target: ")
    target_set = select_num()
    new_object = Solution([], target_set)
    
    while not step_check(input_step):
        input_step = input("Do you want random list? y/n | ")

    first_step()
    new_object.display_all_info()

    end_program = True