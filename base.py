import random
import time

#decor function to show time manage
def decor_timer(funct):
    def timer():
        start_time = time.time()
        funct()
        end_time = time.time()
        print("Time load: ", end_time-start_time, "\n")
    return funct
#function to take only num
def select_num():
    end_target = False
    while not end_target:
        try: 
            first_target = int(input("Input num: "))
            print("\n")
            end_target = True
            
        except:
            print("Input only nums")        
    return first_target

#function to generate list with random nums
@decor_timer
def generate_random_list():
    sep_list = []
    random_len = random.randint(5, 10)
    for i in range(random_len):
        sep_list.append(random.randint(1, 9))
    print("Your list is generated \n")
    return sep_list





#Function to check input y/n
def step_check(input):
    try:
        input_lower = input.lower()
    except:
        input_lower = input

    if input_lower == "y" or input_lower == "n":
        print("Lets do it \n")
        return input_lower
    else:
        print('Input only "y" or "n"')
        return False


                
