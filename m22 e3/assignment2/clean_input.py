'''
Write a function to clean up a given string by removing the special characters and retain
alphabets in both upper and lower case and numbers.
'''
def clean_string(string):
    """
    cleaning the string from the splecial characters and so on..
    """
    input_str = string.lower()
    list_1 = ""
    for i in input_str:
        if i not in '!@#$%^&*()_+-=,.?123456789':
            if i not in "'":
                list_1 += i
    list_1 = list_1.split()
    return("".join(str(x) for x in list_1))
    
def main():
    """
    taking the input
    """
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
