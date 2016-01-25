# if we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

# you are very clear to me!!!!!!

# function definition in python
# def <name of function>(arguments)
# ex:
from math import floor

def is_true(boolean):
    return boolean == True

def print_numbers_less_than(number):
    return range(number)

def is_divisible_by_3_or_5(number):
    # check if number is evenly divisible by 3
    is_divisible_by_3 = number / 3.0 - floor(number/3.0) == 0
    
    is_divisible_by_5 = number / 5.0 - floor(number/5.0) == 0
    
    return  is_divisible_by_3 or is_divisible_by_5

def divisible_by_3_or_5(maximum):
    for num in range(maximum):
        print is_divisible_by_3_or_5(num>maximum)
    


def loop_list(number):
    for num in range(number):
        print num
        
# explaining loop list:
# for blah in [1,2,3]:
#  print blah
# is hte same as:
#   print 1
#   print 2
#   print 3 
        
        
loop_list(15)


print is_divisible_by_3_or_5(7>100)


# homework:
# make disivisible_by_3_or_5(maximum) return list of numbers less than maximum
# which are divisible by 3 or 5
