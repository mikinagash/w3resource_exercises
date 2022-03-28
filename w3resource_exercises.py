 #Q1
# print("twinkle,twinkle,little star, \n \t how i wonder what you are ! \n \t\t up above the world so high,\n\t\t like a dimond in the sky.\n twinkle , twinkle , little star,\n \t how i wonder what you are ")

#q2
# import sys
# print("python version")
# print(sys.version)
# print("version info")
# print(sys.version_info)

#q3
# import datetime
# now = datetime.datetime.now()
# print("current date and time :")
# print(now.strftime("%Y-%m-%d %H:%M:%S"))

#q4
# radius = float(input("enter radius of circle :"))
# print( "the radius of the circle is :",round(3.14124* radius **2,2) )

#q5
# first_name = input("enter your first name :")
# last_name = input("enter your last name :")
# print(last_name + '  '+ first_name)


#q6
# numbers = input("enter comma seprated numbers :")
# list = numbers.split(",")
# tuple = tuple(list)
# print("list:",list)
# print("tuple :",tuple)

#Q7
# filename = input("Input the Filename: ")
# f_extns = filename.split(".")
# print ("The extension of the file is : " + repr(f_extns[-1]))


#q8
# my_goal = []
# for i in range(1500,2701):
#         if (i % 5 == 0) and (i % 7 == 0):
#                 my_goal.append(str(i))
# print(my_goal)



# 9date
# exam_st_date = (3,20,2022)
# print( "The examination will start from : %i / %i / %i"%exam_st_date)
#
# 10
# a = int(input("Input an integer : "))
# n1 = int( "%s" % a )
# n2 = int( "%s%s" % (a,a) )
# n3 = int( "%s%s%s" % (a,a,a) )
# print (n1+n2+n3)
#
# 11
# print(abs._doc_)
#
# 12
# import calendar
# y = int(input("Input the year : "))
# m = int(input("Input the month : "))
# print(calendar.month(y, m))
#
# 13
# import calendar
# y = int(input("Input the year : "))
# m = int(input("Input the month : "))
# print(calendar.month(y, m))
#
# 14
# from datetime import date
# f_date = date(2014, 7, 2)
# l_date = date(2014, 7, 11)
# delta = l_date - f_date
# print(delta.days)
#
# 15
# pi = 3.1415926535897931
# r= 6.0
# V= 4.0/3.0*pi* r**3
# print('The volume of the sphere is: ',V)
#
# 16
# def difference(n):
#     if n <= 17:
#         return 17 - n
#     else:
#         return (n - 17) * 2
#
# print(difference(22))
# print(difference(14))
#
# 17
# def near_thousand(n):
#     return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
#
#
# print(near_thousand(1000))
# print(near_thousand(900))
# print(near_thousand(800))
# print(near_thousand(2200))
#
# 18
# def sum_thrice(x, y, z):
#     sum = x + y + z
#
#     if x == y == z:
#         sum = sum * 3
#     return sum
#
#
# print(sum_thrice(1, 2, 3))
# print(sum_thrice(3, 3, 3))
#
# 19
# def new_string(str):
#   if len(str) >= 2 and str[:2] == "Is":
#     return str
#   return "Is" + str
#
# print(new_string("Array"))
# print(new_string("IsEmpty"))
#
# 20
# def larger_string(str, n):
#    result = ""
#    for i in range(n):
#       result = result + str
#    return result
#
# print(larger_string('abc', 2))
# print(larger_string('.py', 3))
#
# 21
# num = int(input("Enter a number: "))
# mod = num % 2
# if mod > 0:
#     print("This is an odd number.")
# else:
#     print("This is an even number.")
#
# 22
# def list_count_4(nums):
#   count = 0
#   for num in nums:
#     if num == 4:
#       count = count + 1
#
#   return count
#
# print(list_count_4([1, 4, 6, 7, 4]))
# print(list_count_4([1, 4, 6, 4, 7, 4]))
#
# 23
# def substring_copy(str, n):
#     flen = 2
#     if flen > len(str):
#         flen = len(str)
#     substr = str[:flen]
#
#     result = ""
#     for i in range(n):
#         result = result + substr
#     return result
#
#
# print(substring_copy('abcdef', 2))
# print(substring_copy('p', 3));
#
# #24
# def is_vowel(char):
#     all_vowels = 'aeiou'
#     return char in all_vowels
# print(is_vowel('c'))
# print(is_vowel('e'))
#
# #25
# def is_group_member(group_data, n):
#    for value in group_data:
#        if n == value:
#            return True
#    return False
# print(is_group_member([1, 5, 8, 3], 3))
# print(is_group_member([5, 8, 3], -1))
#
# #26
# def histogram( items ):
#     for n in items:
#         output = ''
#         times = n
#         while( times > 0 ):
#           output += '*'
#           times = times - 1
#         print(output)
#
# histogram([2, 3, 6, 5])
#
# 27
# def concatenate_list_data(list):
#     result= ''
#     for element in list:
#         result += str(element)
#     return result
#
# print(concatenate_list_data([1, 5, 12, 2]))
#
# #28
# numbers = [
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
#     958, 743, 527
# ]
#
# for x in numbers:
#     if x == 237:
#         print(x)
#         break;
#     elif x % 2 == 0:
#         print(x)
#
# #29
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# print("Original set elements:")
# print(color_list_1)
# print(color_list_2)
# print("\nDifferenct of color_list_1 and color_list_2:")
# print(color_list_1.difference(color_list_2))
# print("\nDifferenct of color_list_2 and color_list_1:")
# print(color_list_2.difference(color_list_1))
#
# 30
# b = int(input("Input the base : "))
# h = int(input("Input the height : "))
#
# area = b*h/2
#
# print("area = ", area)
#
# #31
# def gcd(x, y):
#    gcd = 1
#    if x % y == 0:
#        return y
#    for k in range(int(y / 2), 0, -1):
#        if x % k == 0 and y % k == 0:
#            gcd = k
#            break
#    return gcd
# print("GCD of 12 & 17 =",gcd(12, 17))
# print("GCD of 4 & 6 =",gcd(4, 6))
# print("GCD of 336 & 360 =",gcd(336, 360))
#
# #32
# def lcm(x, y):
#   if x > y:
#       z = x
#   else:
#       z = y
#   while(True):
#       if((z % x == 0) and (z % y == 0)):
#           lcm = z
#           break
#       z += 1
#   return lcm
# print(lcm(4, 6))
# print(lcm(15, 17))
#
# 33
# def sum(x, y, z):
#     if x == y or y == z or x==z:
#         sum = 0
#     else:
#         sum = x + y + z
#     return sum
#
# print(sum(2, 1, 2))
# print(sum(3, 2, 2))
# print(sum(2, 2, 2))
# print(sum(1, 2, 3))
#
# 34
# def sum(x, y):
#     sum = x + y
#     if sum in range(15, 20):
#         return 20
#     else:
#         return sum
#
# print(sum(10, 6))
# print(sum(10, 2))
# print(sum(10, 12))
#
# 35
# def test_number5(x, y):
#    if x == y or abs(x-y) == 5 or (x+y) == 5:
#        return True
#    else:
#        return False
# print(test_number5(7, 2))
# print(test_number5(3, 2))
# print(test_number5(2, 2))
# print(test_number5(7, 3))
# print(test_number5(27, 53))
#
# 36
# def add_numbers(a, b):
#    if not (isinstance(a, int) and isinstance(b, int)):
#        return "Inputs must be integers!"
#    return a + b
# print(add_numbers(10, 20))
# print(add_numbers(10, 20.23))
# print(add_numbers('5', 6))
# print(add_numbers('5', '6'))
#
# 37
# def personal_details():
#     name, age = "Simon", 19
#     address = "Bangalore, Karnataka, India"
#     print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))
#
# personal_details()
#
# #38
# x, y = 4, 3
# result = x * x + 2 * x * y + y * y
# print("({} + {}) ^ 2) = {}".format(x, y, result))
#
# 39
# amt = 10000
# int = 3.5
# years = 7
# future_value = amt*((1+(0.01*int)) ** years)
# print(round(future_value,2))
#
# 40
# import math
# p1 = [4, 0]
# p2 = [6, 6]
# distance = math.sqrt( ((p1[0]-p2[0])*2)+((p1[1]-p2[1])*2) )
#
# print(distance)
#
# 41
# For 32 bit it will return 32 and for 64 bit it will return 64
# import struct
# print(struct.calcsize("P") * 8)
#
# 42
# For 32 bit it will return 32 and for 64 bit it will return 64
# import struct
# print(struct.calcsize("P") * 8)
#
# 43
# import platform
# import os
# print("Name of the operating system:",os.name)
# print("\nName of the OS system:",platform.system())
# print("\nVersion of the operating system:",platform.release())
#
# 44
# import site;
# print(site.getsitepackages())
#
# 45
# from subprocess import call
# call(["ls", "-l"])
