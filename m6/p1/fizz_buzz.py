'''
Write a short program that prints each number from 1 to i on a new line.
For each multiple of 3, print "Fizz" instead of the number.
For each multiple of 5, print "Buzz" instead of the number.
For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.
'''
def main():
    '''
    Read number from the input, store it in variable num.
    '''
    num = int(input())
    i = ""
    for i in range(0,num):
    	print(i)
    	if i%3 == 0:
    		i = "Buzz"
    	elif i%5 == 0:
    		i = "Fizz"
    	elif i%3 == 0 and i%5 == 0:
    		i = "/nFizzBuzz"
    	else:
    		i = i
    	print(i)
if __name__ == "__main__":
    main()
