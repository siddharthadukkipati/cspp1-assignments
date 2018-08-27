'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
    """
    measuring the frequency
    """
    key_inp = sorted(dictionary.keys())
    for values in key_inp:
        print(values, '-', dictionary[values]*('#'))

def main():
    """
    reading dictionary
    """
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
