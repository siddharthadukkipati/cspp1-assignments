'''
Write a program that prints the longest substring
of s in which the letters occur in alphabetical order'''
def main():
    """defining main function"""
    str_s = input()
    max_count = 0
    gain_count = 0
    count_count = 0
    for i in range(len(str_s)-1):
        if str_s[i] <= str_s[i+1]:
            count_count += 1
        else:
            count_count = 0
        if gain_count < count_count:
            gain_count = count_count
            max_count = i
    d_d = max_count-gain_count+1
    print(str_s[d_d:d_d+gain_count+1])
if __name__ == "__main__":
    main()
