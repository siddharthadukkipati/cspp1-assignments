""""#Assume s is a string of lower case characters.
#Write a program that counts up the number of vowels contained in the string s.
 Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example,
 if s = 'azcbobobegghakl', your program should print:
#Number of vowels: 5
"""
def main():
    """
    main function
    """
    inp_var = input()
    vowels_str = ""
    consonents_str = ""
    for char in inp_var:
        if char in 'AEIOUaeiou':
            vowels_str += char
        else:
            consonents_str += char
    print(len(vowels_str))
if __name__ == "__main__":
    main()
