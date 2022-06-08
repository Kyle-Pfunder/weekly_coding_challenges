from random import randint, sample,randrange
from string import ascii_lowercase,digits
from os import system,get_terminal_size
from time import sleep


def error():
    system("cls")
    center("invalid entry",0)
    sleep(2)


def center(var,i,s):
    w,h = get_terminal_size()
    if i == 0: print(int((h*.3)) * "\n")
    print(f"{int(((w-len(var))/2)+s)*' '}{var}")


def test_case_generator(x):
    if x == 0:
        value = ''
        for i in range(3):
            value += f"{str(randint(1,10000))} "
        return value.strip()

    else: return ''.join(sample(ascii_lowercase+digits,randrange(8,20)))


def problem1():
    system("cls")

    for i in range(randrange(3,8)):
        value = test_case_generator(0)
        s=0

        sorted_list = [int(item) for item in value.split()]
        center(f"[test case {i+1}]: {value} {(25-len(value))*'='} middle value: {sorted(sorted_list)[1]}",i,s)
        
    print("\n\n")
    system("pause")


def problem2():
    system("cls")

    for i in range(randrange(3,8)):
        value = test_case_generator(1)
        sum = 0
        s = 0
        for char in value:
            if char.isdigit() == True: sum = sum+int(char)

        if len(str(sum)) == 1: s=-1
        center(f"[test case {i+1}]: {value} {(25-len(value))*'='} sum: {sum}",i,s)

    print("\n\n")
    system("pause")


while True:
    w,h = get_terminal_size()
    system("cls")
    try:
        print(int(h*.3)*"\n")
        selection = int(input(f"""
{int((w-34)/2)*' '}*** coding challenge - 6/10/22 ***

{int((w-13)/2)*' '}[1] problem 1
{int((w-13)/2)*' '}[2] problem 2
{int((w-13)/2)*' '}[3] exit

{int((w-11)/2)*' '}selection: """))

        if selection not in range(1,4): error()
        elif selection == 1: problem1()
        elif selection == 2: problem2()
        else:
            system("cls")
            exit()

    except ValueError: error()