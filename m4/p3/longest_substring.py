'''
Write a program that prints the longest substring
of s in which the letters occur in alphabetical order'''
def main():
    """defining main function"""
    str_s = input()
    m_c = 0
    g_c = 0
    c_co = 0
    for i in range(len(str_s)-1):
        if str_s[i] <= str_s[i+1]:
            c_co += 1
        else:
            c_co = 0
        if g_c < c_co:
            g_c = c_co
            m_c = i
    d_d = m_c-g_c+1
    print(str_s[d_d:d_d+g_c+1])
if __name__ == "__main__":
    main()
