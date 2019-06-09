# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 19:47:02 2019
@author: Adam

"""

import time, sys, math

start_time=time.gmtime()

tests=[1, 1000, 10000, 100000, 1000000, 10000000]

try:
    name_of_file = 'primes_list.txt'
    file = open(name_of_file).read()
    prime_list = file.split("\n")
    if prime_list[len(prime_list)-1]=="":
        prime_list.pop()

    else:
        print("Not recognized format")
        sys.exit()

except:
    prime_list=[2,3]      


for counter, value in enumerate(prime_list):
    prime_list[counter]=int(value) 
     

how_much_in_table = len(prime_list)
how_much_wanted=max(tests)
 
print("Uploaded from file:",name_of_file, how_much_in_table, "prime numbers\nTime:",time.mktime(time.gmtime())-time.mktime(start_time))


last_checked_number = prime_list[how_much_in_table-1]

file=open( name_of_file, 'a')
 
while how_much_in_table < how_much_wanted:
    checked_number = last_checked_number + 2
    is_prime=True
    squared_number = int(math.sqrt(checked_number))
    for i in prime_list:
        if (checked_number % i) == 0:
            is_prime = False
            break
        if i > squared_number:
            break
    last_checked_number = checked_number
    if is_prime:
        prime_list.append(last_checked_number)
        file.write(str(last_checked_number)+'\n')
        how_much_in_table += 1
        if how_much_in_table%10000==0:
            print(str(how_much_in_table)+' '+str(last_checked_number))