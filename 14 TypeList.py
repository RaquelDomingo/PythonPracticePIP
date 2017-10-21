# #input
# list1 = ['magical unicorns', 19, 'hello', 98.98, 'world']

# sum = 0
# string = ""
# type = [False, False]

# for value in list1:
#     if isinstance(value, float) or isinstance(value, int):
#         sum += value
#         type[0] = True
#     else:
#         string += value + " "
#         type[1] = True
# if all(type): print "The array you entered is mixed type.\n String: %s\n Sum: %.2f" %(string, sum)  
# elif type[0]: print "The array you entered is integer type.\n Sum: %.2f" %(sum)
# elif type[1]: print "The array you entered is string type.\n String: %s" %(string)


# #input2
# list1 = [2,3,1,7,4,12]

# sum = 0
# string = ""
# type = [False, False]

# for value in list1:
#     if isinstance(value, float) or isinstance(value, int):
#         sum += value
#         type[0] = True
#     else:
#         string += value + " "
#         type[1] = True
# if all(type): print "The array you entered is mixed type.\n String: %s\n Sum: %.2f" %(string, sum)  
# elif type[0]: print "The array you entered is integer type.\n Sum: %.2f" %(sum)
# elif type[1]: print "The array you entered is string type.\n String: %s" %(string)


#input3
list1 = ['magial','unicorns']

sum = 0
string = ""
type = [False, False]

for value in list1:
    if isinstance(value, float) or isinstance(value, int):
        sum += value
        type[0] = True
    else:
        string += value + " "
        type[1] = True
if all(type): print "The array you entered is mixed type.\n String: %s\n Sum: %.2f" %(string, sum)  
elif type[0]: print "The array you entered is integer type.\n Sum: %.2f" %(sum)
elif type[1]: print "The array you entered is string type.\n String: %s" %(string)
