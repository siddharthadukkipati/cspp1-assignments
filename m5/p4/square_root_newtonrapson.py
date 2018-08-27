'''Write a python program to find the square root of the given number'''

def main():
    """Square_root_newton"""
    s_v = float(input())
    epsilon_v = 0.01
    guess_v = s_v/2.0
    while guess_v <= s_v:
        if abs(guess_v**2-s_v) >= epsilon_v:
            guess_v = guess_v-(guess_v**2 - s_v)/(2*guess_v)
        else:
            break
    if abs(guess_v**2-s_v) >= epsilon_v:
        print("Failed")
    else:
        print(guess_v)
if __name__ == "__main__":
    main()
