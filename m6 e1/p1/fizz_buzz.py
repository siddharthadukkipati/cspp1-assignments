'''
Write a short program that prints each number from 1 to num on a new line.
For each multiple of 3, print "Fizz" instead of the number.
For each multiple of 5, print "Buzz" instead of the number.
For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.
'''
inpu_num = int(input())
count_ = 1
while count_ <= inpu_num:
    if count_%3 == 0 and count_%5 == 0:
        print("Fizz")
        print("Buzz")
    elif count_%3 == 0:
        print("Fizz")
    elif count_%5 == 0:
        print("Buzz")
    else:
        print(count_)
    count_ = count_ + 1
