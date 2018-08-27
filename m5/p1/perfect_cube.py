'''Write a python program to find if the given number is a perfect cube or not'''

def main():
    """Perfect cube"""
    s_v = int(input())
    guess_v = 0
    while guess_v**3 < s_v:
        guess_v += 1
    if guess_v**3 == s_v:
        print(str(s_v)+" is a perfect cube")
    else:
        print(str(s_v)+" is not a perfect cube")
if __name__ == "__main__":
    main()
