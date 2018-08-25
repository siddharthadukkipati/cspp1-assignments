'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Format of the printing should be one key per line and separate
the key and frequency with a SPACE - SPACE.
'''

def print_dictionary(dictionary):
    """printing the dict values"""
    keys_inp = sorted(dictionary.keys())
    for values in keys_inp:
        print(values, '-', dictionary[values])

def main():
    """reading the dict"""
    dictionary = eval(input())
    print_dictionary(dictionary)

if __name__ == '__main__':
    main()
