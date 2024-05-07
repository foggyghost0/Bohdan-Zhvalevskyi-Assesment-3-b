"""
Blackjack
"""


def calculate_score(a: int, b: int, c: int):
    int_list = [a, b, c]

    if sum(int_list) < 21 or sum(int_list) == 21:
        return sum(int_list)

    elif sum(int_list) > 21 and (a == 11 or b == 11 or c == 11):
        new_summ = sum(int_list) - 10
        if new_summ > 21:
            return "BUST"
        else:
            return print(new_summ)
    else:
        return "BUST"


"""
Even Numbers
"""


def even_positive_numbers(a):
    new_list = [x for x in a if (x > 0) and (x % 2 == 0)]
    return new_list


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(
        "Test your functions by calling them here. Use different parameter values to test them with different "
        "scenarios.")

    '''My Testing Below'''

    # 01 Blackjack
    print(calculate_score(11, 11, 11))
    # 02 Even Numbers
    mylist_0 = [1, 2, 3]
    print(even_positive_numbers(mylist_0))
    mylist = [10, 22, 31, 24, 35, 36]
    print(even_positive_numbers(mylist))
    mylist_2 = [-10, -22, 31, 24, 35, 36]
    print(even_positive_numbers(mylist_2))
