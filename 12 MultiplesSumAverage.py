#Multiples
#Part I
for count in range(1, 1001, 2):
    print count #prints all the odd numbers from 1 to 1000

#Part II
for count in range(5,1000001,5):
    print count #prints all the multiples of 5 from 5 to 1,000,000

#Sum List
numbers = [1, 2, 5, 10, 255, 3]
sum = 0
for i in numbers:
    sum += i
print sum #prints the sum of all the values in the list

#Average List
numbers = [1, 2, 5, 10, 255, 3]
sum = 0
for i in numbers:
    sum += i
print sum/len(numbers) #prints the average of the values in the list