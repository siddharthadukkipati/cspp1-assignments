'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    out_str = ""
    lines = int(input())
    for i in range(lines):
        out_str += input() + '\n'  
        i += 1
    print(out_str)
if __name__ == '__main__':
    main()
