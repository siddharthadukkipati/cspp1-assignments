"""Assume s is a string of lower case characters.
Write a program that prints the longest substring of s in
which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print
Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring.
For example, if s = 'abcbcd', then your program should print
Longest substring in alphabetical order is: abc
Note: This problem may be challenging. We encourage you to work smart.
If you've spent more than a few hours on this problem, we suggest that you
move
on to a different part of the course.
If you have time, come back to this problem after you've had a
break and cleared your head."""

def main():
    """to print the longest alphabetical series"""
    inp_str = input()
    max_count = 0
    gain_count = 0
    count_c = 0
    for i in range(len(inp_str)-1):
        if inp_str[i] <= inp_str[i+1]:
            count_c += 1
        else:
            count_c = 0
        if gain_count < count_c:
            gain_count = count_c
            max_count = i
    d_max = max_count - gain_count + 1
    print(inp_str[d_max:d_max+gain_count+1])
if __name__ == "__main__":
    main()
