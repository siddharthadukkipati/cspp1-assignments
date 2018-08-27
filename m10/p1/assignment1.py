'''def'''
def get_available_letters(letters_guessed):
    '''
    :param letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
    yet been guessed.
    '''
    import string
    alphabets = string.ascii_lowercase
    for char in letters_guessed:
        if char in letters_guessed:
            alphabets = alphabets.replace(char, "")
    return alphabets

def main():
    '''
    Main function for the given program
    '''
    user_input = input()
    user_input = user_input.split()
    data = []
    for char in user_input:
        data.append(char[0])
    print(get_available_letters(data))


if __name__ == "__main__":
    main()
    