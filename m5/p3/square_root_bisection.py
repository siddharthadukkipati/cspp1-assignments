# Write a python program to find the square root of the given number
''' using approximation method: square_root bijection'''

def main():
    """Defining main"""
    s_v = int(input())
    epsilon_v = 0.01
    lo_v = 0
    hi_v = s_v
    guess_v = (lo_v+hi_v)/2
    while abs(guess_v**2-s_v) >= epsilon_v:
        if guess_v**2 > s_v:
            hi_v = guess_v
        else:
            lo_v = guess_v
        guess_v = (lo_v+hi_v)/2
    if (guess_v**2-s_v) >= epsilon_v:
        print("Failed")
    else:
        print(guess_v)

if __name__ == "__main__":
    main()
