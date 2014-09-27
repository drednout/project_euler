"""https://projecteuler.net/problem=1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Usage:
    solution.py max_number
"""
import sys

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    max_number = int(sys.argv[1])

    target_sum = 0
    for n in range(max_number):
        if n % 5 == 0:
            target_sum += n
            continue
        if n % 3 == 0:
            target_sum += n
            continue

    print("The answer is {}".format(target_sum))



if __name__ == "__main__": 
    main()
