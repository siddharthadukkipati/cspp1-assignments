''' Write a python program to find the square root of the given number'''
def main():
    """square_root assignment"""
    s_v = int(input())
    epsilon_v = 0.01
    step_v = 0.1
    guess_v = 0
    while abs(guess_v**2 - s_v) >= epsilon_v:
        guess_v += step_v
    if (guess_v**2 - s_v) >= epsilon_v:
        print("failed")
    else:
        print(guess_v)
if __name__ == "__main__":
    main()
