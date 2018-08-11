'''
    Assignment-1 Create Social Network
'''

def create_social_network(data):
    '''
        The data argument passed to the function is a string
        It represents simple social network data
        In this social network data there are people following other people

        Here is an example social network data string:
        John follows Bryant,Debra,Walter
        Bryant follows Olive,Ollie,Freda,Mercedes
        Mercedes follows Walter,Robin,Bryant
        Olive follows John,Ollie

        The string has multiple lines and each line represents one person
        The first word of each line is the name of the person
        The second word is follows that separates the person from the followers
        After the second word is a list of people separated by ,

        create_social_network function should split the string on lines
        then extract the person and the followers by splitting each line
        finally add the person and the followers to a dictionary and
        return the dictionary

        Caution: watch out for trailing spaces while splitting the string.
        It may cause your test cases to fail although your output may be right

        Error handling case:
        Return a empty dictionary if the string format of the data is invalid
        Empty dictionary is not None, it is a dictionary with no keys
    '''
    print("Range")
    inp_a = int(input())
    print("Enter the dict values")
    a_dict = {}
    for i in range(inp_a):
        data = input()
        l = data.split("follows")
        if l[0] not in a_dict:
            a_dict[l[0]] = l[1].split(",")
        else:
            a_dict[l[0]].append(l[1].split(","))
    for i in a_dict:
        a_dict[i] = set(a_dict[i])
    print(a_dict)
def main():
    '''
        handling testcase input and printing output
    '''
    string = ''
    print(create_social_network(string))

if __name__ == "__main__":
    main()
