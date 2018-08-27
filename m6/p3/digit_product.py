""" # given input product_num the individual number example 123 output should be  6"""
inp_1 = int(input())
product_num = 1
initial_number = 1
num_ = 1
if inp_1 < 0:
    num_ = -1
    inp_1 = abs(inp_1)
else:
    num_ = 1
if inp_1 != 0:
    while inp_1 >= 1:
        initial_number = inp_1 % 10
        product_num = product_num * initial_number
        inp_1 = inp_1 // 10
    print(num_*product_num)
else:
    print("0")
