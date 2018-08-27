'''assume s is a string of lower case characters.
number of times bob occurs is: 2'''

def main():
    """definition"""
    count_v = 0
    inp_str = input()
    comp_str = 'bob'
    for i in range(len(inp_str)):
        if comp_str == inp_str[i:i+3]:
            count_v = count_v + 1
    print(count_v)
if __name__ == "__main__":
    main()
