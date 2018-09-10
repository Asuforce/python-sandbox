# coding:utf-8

input = input()
xem = float(input)
balance = 0

if xem < 10001:
    print('It is not enough', 10001-xem, 'XEM to harvest.')
    exit()


def equation(i, b):
    if i == 1:
        return b * 0.1

    minusOne = equation(i-1, b)

    return minusOne + (b-minusOne)*0.1


i = 1
while True:
    balance = equation(i, xem)
    print('Day:', i, 'balance =>', balance)

    if balance > 10000:
        break

    i = i+1
