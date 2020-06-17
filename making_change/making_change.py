#!/usr/bin/python

import sys


def making_change(amount, denominations):
    count = 0

    if amount == 0:
        return 1

    if amount == 1:
        return 1

    if amount % denominations[0] == 0:
        count += 1
    if amount % denominations[1] == 0:
        count += 1
    if amount % denominations[2] == 0:
        count += 1
    if amount % denominations[3] == 0:
        count += 1
    if amount % denominations[4] == 0:
        count += 1
    else:
        return count

    return count


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
