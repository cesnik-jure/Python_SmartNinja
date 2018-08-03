def sum_of_numbers(a, b):
    c = a + b
    print(c)
    return c


def sum_of_lists(a, b = []):
    s = 0
    for num in a:
        s = s + num
    for num in b:
        s = s + num
    return s

def sum_of_seperate_lists(a = [], b = []):
    sum1 = 0
    sum2 = 0
    for num in a:
        sum1 = sum1 + num
    for num in b:
        sum2 = sum2 + num
    return sum1, sum2

def main():
    number_one = 15
    number_two = 40
    d = sum_of_numbers(number_one, number_two)
    print(d)

    l = [5, 10, 15]
    k = [6, 3, 2]
    s1 = sum_of_lists(l, k)
    print(s1)
    s2 = sum_of_lists(l)
    print(s2)

    # sum1, sum2 = sum_of_seperate_lists(l, k)[0]
    print(sum_of_seperate_lists(l, k)[0])
    print(sum_of_seperate_lists(l, k)[1])


# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == "__main__":
    main()
