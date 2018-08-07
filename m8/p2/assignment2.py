"""
Exercise: Assignment-2
Write inp_a Python function, sumofdigits, that takes in one number and returns the
sum of digits of given number.
This function takes in one number and returns one number.
"""
def sum_of_digits(inp_n):
    """
    inp_n is positive Integer
    returns: inp_a positive integer, the sum of digits of inp_n.
    """
    # Your code here
    if inp_n == 0:
        return 0
    return inp_n%10 + sum_of_digits(inp_n//10)

def main():
    """
    calling function
    """
    inp_a = input()
    print(sum_of_digits(int(inp_a)))

if __name__ == "__main__":
    main()
