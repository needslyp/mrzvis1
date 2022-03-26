import math
import time

def sum_vector(vec1: list, vec2: list):

    if len(vec1) < len(vec2):
        while len(vec1) != len(vec2):
            vec1.append(0)
    elif len(vec2) < len(vec1):
        while len(vec1) != len(vec2):
            vec2.append(0)

    newVector = []
    buffer = 0
    for x in range(len(vec1) - 1, -1, -1):
        item = (vec1[x] * (not vec2[x]) + (not vec1[x]) * vec2[x] + buffer) % 2
        buffer = (vec1[x] * vec2[x] + (vec1[x] + vec2[x]) * buffer) % 2
        newVector.insert(0, item)

    newVector.insert(0, buffer)
    newVector.pop(0)
    return newVector

def parse_to_binary(num: int):
    newVector = []
    while num != 0:
        newVector.insert(0, num%2)
        num = math.floor(num/2)

    return newVector

def parse_from_binary(vec:list):
    num=0
    for x in range(len(vec)-1, -1,-1):
        if vec[x] == 1:
            num += 2**(len(vec)-(x+1))

    return num

def binary_vector_extention(vec: list, size: int):
    amount = size - len(vec)
    for i in range(amount):
        vec.insert(0, 0)

def move_right(vec: list, size:int):
    for i in range(size):
        vec.insert(0, 0)

def operation(mid_sum_pair:list, vect1:list, arg2:int):
    vec_zero = parse_to_binary(0)
    binary_vector_extention(vec_zero, len(mid_sum_pair)+1)
    move_right(vect1, 1)

    if arg2 == 1:
        mid_sum_pair = sum_vector(mid_sum_pair, vect1)

    if arg2 == 0:
        mid_sum_pair = sum_vector(mid_sum_pair, vec_zero)

    return mid_sum_pair

def conveyer(vector1:list, vector2:list):
    for x in vect1:
        if x < 0 or x > 15:
            vector1.remove(x)


    for x in vect2:
        if x < 0 or x > 15:
            vector2.remove(x)

    print('First vector : ', end='')
    print(*vector1, sep=' ')
    print('Second vector : ', end='')
    print(*vector2, sep=' ')

    if len(vector1) > len(vector2):
        size = len(vector2)
    else:
        size = len(vector1)

    print('Amount numbers in conveyer : ' + str(size))

    for i in range(size):
        num1 = vector1[i]
        print('First input number : ' + str(num1))
        num2 = vector2[i]
        print('Second input number : ' + str(num2))

        print()

        arg1 = parse_to_binary(num1)
        arg2 = parse_to_binary(num2)
        mid_sum_pair = parse_to_binary(0)

        if len(arg1) > len(arg2):
            binary_vector_extention(arg1, len(arg1) + 4 - len(arg1)%4)
            binary_vector_extention(arg2, len(arg1) + 4 - len(arg1)%4)
            binary_vector_extention(mid_sum_pair, len(arg1) + 4 - len(arg1)%4)
        elif len(arg2) == 4 and len(arg1) == 4:
            binary_vector_extention(mid_sum_pair, 4)
        elif len(arg2) >= len(arg1):
            binary_vector_extention(arg1, len(arg2) + 4 - len(arg2)%4)
            binary_vector_extention(arg2, len(arg2) + 4 - len(arg2)%4)
            binary_vector_extention(mid_sum_pair, len(arg2) - len(arg2)%4)




        print('First number in binary :                  ', end='')
        print(*arg1, sep='')

        print('Second number in binary :                 ', end='')
        print(*arg2, sep='')

        print('Create an intermediate response :         ', end='')
        print(*mid_sum_pair, sep='')

        print()

        print('Conveyer started')
        tick1 = time.perf_counter()
        ind = 0
        for ind in range(len(arg2)):
            if arg2[ind] == 1:
                break

        step = 0
        print('-'*80)
        for conv_step in range(ind, len(arg2)):
            step += 1

            tick = time.perf_counter()
            print('Start of step : ' + str(step))
            print('Intermediate sum :                        ', end='')
            print(*mid_sum_pair, sep='')
            print('Input argument : ' + str(arg2[conv_step]))

            mid_sum_pair = operation(mid_sum_pair, arg1, arg2[conv_step])

            print('Output intermediate sum :                 ', end='')
            print(*mid_sum_pair, sep='')
            print('End of step')
            tock = time.perf_counter()

            print(f"Time of step : {tock - tick:0.5f} sec")

            print('-' * 70)
        print('Conveyer finished')
        print('Multiplication of two vectors :           ' + str(parse_from_binary(mid_sum_pair)))
        binary_vector_extention(mid_sum_pair, 8)
        tock1 = time.perf_counter()
        print('Multiplication of two vectors in binary : ', end='')
        print(*mid_sum_pair, sep='')
        print(f"Time of all conveyer : {tock1 - tick1:0.5f} sec")
        print('#'*80)
        print()


vect1 = [5,23,15,8,13]
vect2 = [4,15,17,14]

conveyer(vect1, vect2)

