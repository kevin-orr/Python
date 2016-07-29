__author__ = 'kevinorr'

"""
This was my attempt at the first part of Q2 in a Google challenge about maximising the number of bunnies in train cars...

It passed the 'verify' section - all the tests passed.

"""

from collections import Counter

def answer(x):
    """
    sort the list and find out what the mode would be
    Then pick first element in sorted list and take enough from last element to make first element = mode value
    then repeat

    :param x: a train of cars holding rabbits
    :return: the max number of equal array elements
    """
    number_of_bunnies = sum(x)
    number_cars = len(x)
    # get integral of how many we can squeeze into each car
    estimate_per_car = number_of_bunnies / number_cars
    x = sorted(x)

    first_index = 0
    end_index = len(x) - 1
    #  now run around the list
    while first_index < end_index:
        bunnies_in_this_car = x[first_index]

        if bunnies_in_this_car == estimate_per_car:
            # move to next in list
            first_index += 1
            continue
        else:
            # take enough bunnies to share with this car from the maximal one at the end of list
            delta_to_add = estimate_per_car - x[first_index]
            x[first_index] += delta_to_add
            x[end_index] -= delta_to_add
            x = sorted(x)

        print x
    #  finally use Counter to get the frequency of the most common element
    return Counter(x).most_common(1)[0][1]



if __name__ == "__main__":

    train_full_of_bunnies = [0, 0, 0, 4]
    # for the list above we expect to get back 4 as answer -> [1, 1, 1, 1]
    expected_answer = 4
    maximal = answer(train_full_of_bunnies)
    assert expected_answer == answer(train_full_of_bunnies)

    train_full_of_bunnies = [1, 2, 3]
    expected_answer = 3
    maximal = answer(train_full_of_bunnies)
    assert expected_answer == answer(train_full_of_bunnies)

    train_full_of_bunnies = [1, 4, 1]
    expected_answer = 3
    maximal = answer(train_full_of_bunnies)
    assert expected_answer == answer(train_full_of_bunnies)

    train_full_of_bunnies = [1, 2, 2]
    expected_answer = 2
    maximal = answer(train_full_of_bunnies)
    assert expected_answer == answer(train_full_of_bunnies)

    train_full_of_bunnies = [2, 3, 4, 1, 6, 3]
    expected_answer = 5
    maximal = answer(train_full_of_bunnies)
    assert expected_answer == answer(train_full_of_bunnies)

    train_full_of_bunnies = [1, 0, 3, 3, 5, 10, 8, 12, 4, 15, 11, 2, 14, 5, 7, 13, 15, 5, 7, 10, 8, 12, 4, 15, 11, 2, 33, 5, 0, 44, 5, 7, 13, 15]
    expected_answer = 33
    maximal = answer(train_full_of_bunnies)
    assert expected_answer == answer(train_full_of_bunnies)



