'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    """
    function to read multiple lines of input and
    to print out a String as an output
    """
    output_string = ""
    no_of_lines = int(input())
    for _ in range(no_of_lines):
        output_string += input() + '\n'
    print(output_string)
if __name__ == '__main__':
    """
    main function
    """
    main()
