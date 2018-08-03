""" Write a python program to find the square root of the given number
using approximation method
"""

def main():
    """ Cube root program approximation method"""
    inp_a = int(input())
    guess_a = 0
    check_a = 0.01
    # check is just a tollerance value to check
    while abs(guess_a**3 - inp_a) >= check_a and guess_a <= inp_a:
        guess_a += 0.0001
    if abs(guess_a**3 - inp_a) >= check_a:
        print("The give number is a cube root")
    else:
        print("failed")
if __name__ == "__main__":
    main()
