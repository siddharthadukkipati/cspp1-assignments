"""
Exercise: Assignment-1
Write a Python function, factorial(inp_n), that takes in one number and returns
the factorial of given number.
This function takes in one number and returns one number.
"""
def fact_rec(inp_n):
    """
    inp_n is positive Integer
    returns: a positive integer, the fact_rec of inp_n.
    """
    # Your code here
    if inp_n <= 1:
        return 1
    return inp_n * fact_rec(inp_n-1)

def main():
    """calling the function"""
    inp_a = input()
    print(fact_rec(int(inp_a)))

if __name__ == "__main__":
    main()
