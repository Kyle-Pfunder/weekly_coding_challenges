from time import sleep
from os import system


def error():
    system("cls")
    print("invalid entry")
    sleep(2)


def challengeA():
    num_arrays = [[515, 341, 98, 44, 211],[63251, 78221],[1, 2, 3, 4]]

    system("cls")
    for array in num_arrays:
        print(f"""
==========================================================
array {num_arrays.index(array) + 1}: {array}

 ascending order: {reorderDigits(array,'asc')}
descending order: {reorderDigits(array,'desc')}""")


def reorderDigits(array: list, order: str):
    if order == "asc": order = False
    else: order = True

    for num in array:
        array[array.index(num)] = int(''.join(sorted(str(num),reverse=order)))

    return array


def challengeB():
    num_arrays = [[2, 8, 4, 1],[-1, -10, 1, -2, 20],[-1, -20, 5, -1, -2, 2]]

    system("cls")

    for array in num_arrays:
        print(f"""
==========================================================
array {num_arrays.index(array) + 1}: {array} -> [{canPartition(array)}]""")


def canPartition(array: list):
    mx = max(array)
    mn = min(array)

    abs_max = abs(mx)
    abs_min = abs(mn)

    if abs_max > abs_min: prod = mx
    else: prod = mn

    x = 1
    for num in array:
        if num != prod: x = x * num

    return bool(prod == x)


while True:
    system("cls")

    try:
        selection = int(input("""
*** coding challenge - 6/3/22 ***

[1] challenge A
[2] challenge B
[3] exit

selection: """))

        if selection not in range(1,4): error()
        elif selection == 1: challengeA()
        elif selection == 2: challengeB()
        else:
            system("cls")
            exit()

        print("\n\n")
        system("pause")
    except ValueError: error()