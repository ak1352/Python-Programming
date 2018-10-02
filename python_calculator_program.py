number = ''  # to take input from user
choices = []  # default values


###############################
def add(choices):
    return choices[0] + choices[1]


def sub(choices):
    return choices[0] - choices[1]


def mul(choices):
    return choices[0] * choices[1]


def div(choices):
    return choices[0] / choices[1]


################################

def enter_operator():
    op_choice = ''
    result = ''
    op_choice = int(input("Please select an option: \n 1. + \n 2. - \n 3, * \n 4. / \n 5. Quit"))
    if op_choice == 1:
        result = add(choices)
        print(result)
        print('\n')
        user_input()
    elif op_choice == 2:
        result = sub(choices)
        print(result)
        print('\n')
        user_input()
    elif op_choice == 3:
        result = mul()
        print(result)
        print('\n')
        user_input()
    elif op_choice == 4:
        result = div()
        print(result)
        print('\n')
        user_input()
    elif op_choice == 5:
        print("Program is Quitting...")
    else:
        print("You didnot enter a valid option.")
        user_input()


###########################
def user_input():
    for i in range(2):
        number1 = input("Please enter 1st number:")
        choices.append(int(number1))

    enter_operator()
###################################
user_input()