'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
def tokenize(string):
    """function to count the freq of the word"""
    words = string.split()
    dictionary = {}
    for word in words:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    return dictionary
def main():
    """to read the input"""
    lines = int(input())
    inp_string = input()
    text = ''.join(inp_string)
    text.split()
    print(tokenize(text))

if __name__ == '__main__':
    main()
