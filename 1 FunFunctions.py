#Odd/Even:
#Create a function called odd_even that counts from 1 to 2000. 
#As your loop executes have your program 
#print the number of that iteration and 
#specify whether it's an odd or even number.

#Multiply:
#Create a function called 'multiply' 
#that iterates through each value in a list (e.g. a = [2, 4, 10, 16]) 
#and returns a list where each value has been multiplied by 5.
#The function should multiply each value in the list by the second argument. 

def odd_even():
    for x in range(1, 2001):
        if x % 2 == 0:
            print "Number is", item, "This is an even number."
        else:
            print "Number is", item,  " this is an odd number"


def multiply(list, multiplier):
    newList = []
    for item in list:
        item = item * multiplier
        newList.append(item)
    return newList


def layered_multiples(arr):
    print arr
    new_array = []
    for x in arr:
        val_arr = []
        for i in range (0,x):
            val_arr.append(1)
        new_array.append(val_arr)
    return new_array   

x = layered_multiples(multiply([2,4,5],3))
print x

a = [2, 4, 10, 16]
b = multiply(a,5)
print b