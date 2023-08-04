#####################################################
# @Author: Abhilash Sarwade
# @Date:   2023-08-02 07:22:15 pm
# @email: a.sarwade@iitg.ac.in
# @File Name: decimal_to_binary.py
# @Project: lab1_20230804
#
# @Last Modified time: 2023-08-04 08:41:13 am
#####################################################

def integer_to_binary(integer_part):
    if integer_part == 0:
        return '0'

    binary_integer = ""
    while integer_part > 0:
        binary_integer = str(integer_part % 2) + binary_integer
        integer_part = integer_part // 2

    return binary_integer


def fractional_to_binary(fractional_part):
    binary_fractional = ""

    while fractional_part > 0:
        fractional_part = fractional_part*2
        if fractional_part >= 1:
            binary_fractional = binary_fractional+'1'
            fractional_part = fractional_part - 1
        else:
            binary_fractional = binary_fractional+'0'

    return binary_fractional


def decimal_to_binary(decimal_num):
    integer_part = int(decimal_num)
    fractional_part = decimal_num - integer_part

    binary_integer = integer_to_binary(integer_part)
    binary_fractional = fractional_to_binary(fractional_part)

    binary_num = binary_integer + '.' + binary_fractional

    return binary_num


decimal_nums = [23.375, 0.5, 3.14, 10.625, 0.1]
for decimal_num in decimal_nums:
    binary_num = decimal_to_binary(decimal_num)
    print(f"Binary representation of {decimal_num} is: {binary_num}")


def binary_to_decimal(binary_num):
    binary_integer = binary_num.split('.')[0]
    binary_fractional = binary_num.split('.')[1]

    decimal_integer = 0
    for n, b in enumerate(binary_integer[::-1]):
        decimal_integer = decimal_integer + int(b)*2**(n)

    decimal_fractional = 0
    for n, b in enumerate(binary_fractional):
        decimal_fractional = decimal_fractional + int(b)*2**(-n-1)

    decimal_num = decimal_integer + decimal_fractional

    return decimal_num
