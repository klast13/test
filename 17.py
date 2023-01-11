def num_to_word(n):

    def sigle_num(n):
        if n == 0:
            return ''
        elif n == 1:
            return 'One'
        elif n == 2:
            return 'Two'
        elif n == 3:
            return 'Three'
        elif n == 4:
            return 'Four'
        elif n == 5:
            return 'Five'
        elif n == 6:
            return 'Six'
        elif n == 7:
            return 'Seven'
        elif n == 8:
            return 'Eight'
        elif n == 9:
            return 'Nine'
    word = ''
    if n > 99:
        word += sigle_num(n // 100) + 'Hundred' + 'And' * (n % 100 != 0)
    if n % 100 < 10:
        word += sigle_num(n % 100)
    elif n % 100 < 14 or n % 100 == 15:
        if n % 100 == 10:
            word += 'Ten'
        elif n % 100 == 11:
            word += 'Eleven'
        elif n % 100 == 12:
            word += 'Twelve'
        elif n % 100 == 13:
            word += 'Thirteen'
        elif n % 100 == 15:
            word += 'Fifteen'
    elif n % 100 < 20:
        word += sigle_num(n % 10) + 'teen'
    else:
        if n % 100 // 10 == 2:
            word += 'Twenty' + sigle_num(n % 10)
        elif n % 100 // 10 == 3:
            word += 'Thirty' + sigle_num(n % 10)
        elif n % 100 // 10 == 4:
            word += 'Forty' + sigle_num(n % 10)
        elif n % 100 // 10 == 5:
            word += 'Fifty' + sigle_num(n % 10)
        elif n % 100 // 10 == 6:
            word += 'Sixty' + sigle_num(n % 10)
        elif n % 100 // 10 == 7:
            word += 'Seventy' + sigle_num(n % 10)
        elif n % 100 // 10 == 8:
            word += 'Eighty' + sigle_num(n % 10)
        elif n % 100 // 10 == 9:
            word += 'Eighty' + sigle_num(n % 10)
    return word


s = 0
for i in range(1, 1000):
    s += len(num_to_word(i))
print(s)
