import random
import time

def decor_timer(funct):
    def timer():
        start_time = time.time()
        funct()
        end_time = time.time()
        print("Time load: ", end_time-start_time, "\n")
    return timer


def select_num():
    end_target = False
    while not end_target:
        try: 
            first_target = int(input("Input num: "))
            print("Ok, you num is done")
            end_target = True
            
        except:
            print("Input only nums")        
    return first_target

@decor_timer
def generate_random_list():
    sep_list = []
    random_len = random.randint(5,10)
    for i in range(random_len):
        sep_list.append(random.randint(1,9))
    print("You list is generated")
    return sep_list

#Function to check input y/n
def step_check(input):
    try:
        input_lower = input.lower()
    except:
        input_lower = input

    if input_lower == "y" or input_lower == "n":
        print("okey, lets do it")
        return True, input_lower
    else:
        print('Input only "y" or "n"')
        return False, input_lower


                
