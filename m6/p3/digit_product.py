'''
Given a  number int_input, find the product of all the digits
example: 
	input: 123
	output: 6
'''
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    int_input = int(input())
    product = 1
    for _ in range(int_input):
    	product = product * _
    print(product)

if __name__ == "__main__":
    main()
