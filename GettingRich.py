def digit_sum(number):
    return sum(int(digit) for digit in str(number))

for number in range(1, 10001):
    for a in range(1, number):
        if digit_sum(number) == 7:
            if number / a == 10 / 3:
                print(number, "divided by", a, "equals 3.333...")