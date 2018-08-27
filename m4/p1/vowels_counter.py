"""Assume s is a string of lower case characters.
Number of vowels: 5"""
def main():
    """Enter string"""
    s_v = input()
    count_v = 0
    for char in s_v:
        if char in 'AEIOUaeiou':
            count_v = count_v + 1
    print(str(count_v))
if __name__ == "__main__":
    main()
