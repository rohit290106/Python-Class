# Python List Programs (Sequence & Indexing)
# Basic Logical Programs
# # 1. Find the sum of all elements in a list
# list1=[1,2,3,4,5,6]
# print("The sum of all elements in a list is",sum(list1))

# # 2. Find the maximum element in a list
# list1=[1,2,3,4,5,6]
# print("The maximum element in a list is",max(list1))

# 3. Find the minimum element in a list
# list1=[1,2,3,4,5,6]
# print("The minimum element in a list is",min(list1))

# # 4. Count even and odd numbers in a list
# list1=[1,2,3,4,5,6]
# even=sum(1 for i in list1 if i%2==0)
# odd=sum(1 for i in list1 if i%2!=0)
# print("Even number in a list is",even)
# print("Odd number in a list is",odd)

# # 5. Calculate the average of list elements
# list1=[1,2,3,4,5,6]
# average=sum(list1)/len(list1)
# print("The average of list elements is",average)

# # 6. Reverse a list using indexing
# list1=[1,2,3,4,5,6]
# list1.reverse()
# print("Reverse of a list is ",list1)

# # 7. Sort a list in ascending order
# list1=[1,2,6,3,5,4]
# list1.sort()
# print("Sort a list in ascending order is",list1)

# # 8. Sort a list in descending order
# list1=[1,2,6,3,5,4]
# list1.sort(reverse=True)
# print("Sort a list in descending order is",list1)

# # 9. Find the second largest number in a list
# list1=[1,2,6,3,5,4]
# list1.sort()
# print("The second largest number in a list is",list1[-2])

# # 10. Remove duplicate elements from a list
# list1=[1,2,3,4,5,5,6,6]
# print("The unique element in a list is",list(set(list1)))


                                                                # # Mathematical Logic Programs
# # 11. Find the sum of even numbers in a list
# list1=[1,2,3,4,5,6]
# sum1=sum(i for i in list1 if i%2==0)
# print("The sum of even numbers in a list is",sum1)

# # 12. Multiply all numbers in a list
# import math
# list1=[1,2,3,4,5,6]
# print(math.prod(list1))

# # 13. Find square of each element in a list
# list1=[1,2,3,4,5,6]
# print("The square of element in a list is",[i**2 for i in list1])

# # 14. Find cube of each element in a list
# list1=[1,2,3,4,5,6]
# print("The cube of each element in a list is",[i**3 for i in list1])

# # 15. Generate Fibonacci series using a list
# list1=[0,1]
# n=int(input("Enter how many Fibonacci numbers you want to see:"))
# for i in range (2,n):
#     list1.append(list1[-1]+list1[-2])
# print(f"The Fibonacci numbers upto {n} numbers is {list1}")

# # 16. Find prime numbers in a list
# list1=[1,2,3,4,5,6,7,8,9,10,-11,12,13]
# prime=[i for i in list1 if i>1 and all( i%n!=0 for n in range (2,int(i**1/2+1)))]
# print("The prime numbers in a list is",prime)

# # 17. Check whether a number is prime
# n=int(input("Enter the value:"))
# prime=n>1 and all(n%i!=0 for i in range (2,int(n**1/2+1)))
# if prime:
#     print(f"{n} is a prime number")
# else:
#     print(f"{n} is not a prime number")

# # 18. Find factorial of a number
# import math
# n=int(input("Enter the value:"))
# print(f"The factorial of {n} is {math.factorial(n)}")

# 19. Find greatest common divisor (GCD)
# 20. Find least common multiple (LCM)
# List and Sequence Programs
# 21. Merge two lists
# 22. Find common elements in two lists
# 23. Find difference between two lists
# 24. Rotate list elements
# 25. Find length of list without using len()
# 26. Insert element at specific index
# 27. Delete element from specific index
# 28. Count occurrence of an element in a list
# 29. Search element in a list
# 30. Separate positive and negative numbers
# Advanced Logical Programs
# 31. Find palindrome numbers in a list
# 32. Count frequency of elements in a list
# 33. Find the largest difference between elements
# 34. Check if a list is sorted
# 35. Find missing number in a sequence
# 36. Implement bubble sort algorithm
# 37. Implement selection sort algorithm
# 38. Implement linear search algorithm
# 39. Implement binary search algorithm
# 40. Find all pairs with given sum
# Advanced Mathematical Programs
# 41. Matrix addition using lists
# 42. Matrix multiplication using lists
# 43. Transpose of a matrix
# 44. Find diagonal elements of a matrix
# 45. Find determinant of a matrix
# 46. Generate multiplication table
# 47. Check Armstrong number
# 48. Check perfect number
# 49. Generate Pascal’s triangle
# 50. Solve quadratic equation