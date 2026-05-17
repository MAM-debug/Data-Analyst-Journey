# practicing List in python

numbers=[10,20,30,40,50]
print(numbers[0]) # accessing the first element of the list
print(numbers[1]) # accessing the second element of the list
print(numbers[-1]) # accessing the last element of the list

cities=["New York","London","Paris","Tokyo"]
print(cities[0]) # accessing the first element of the list
print("Karachi" in cities) # checking if "Karachi" is in the list
cities.append("Karachi") # adding "Karachi" to the list
print("Karachi" in cities) # checking if "Karachi" is in the list after adding it

age=[25,30,35,40]
sum_age=sum(age) # calculating the sum of the ages
average_age=sum_age/len(age) # calculating the average age
largest_age=max(age) # finding the largest age
smallest_age=min(age) # finding the smallest age

marks = [78, 45, 90, 62, 55]
for mark in marks:
    if mark >= 60:
        print("Pass")
        print(mark)

#difference between append and extend method in list(good for interview)
list1=[1,2,3]
list2=[4,5,6]
list1.append(list2) # appending list2 to list1
print(list1) # list1 now contains list2 as a single element
list1=[1,2,3]
list1.extend(list2) # extending list1 with the elements of list2
print(list1) # list1 now contains the individual elements of list2

#Practicing nested list

empolyees=[
    ["John", "Doe", 30],
    ["Jane", "Smith", 25],
    ["Mike", "Johnson", 35]
]
print(empolyees[0]) # accessing the first employee
print(empolyees[0][0]) # accessing the first name of the first employee
print(empolyees[0][1]) # accessing the last name of the first employee
print(empolyees[0][2]) # accessing the age of the first employee

#list comprehension
squares=[x**2 for x in range(1,11)] # creating a list of squares from 1 to 10
#basic syntex = [expression for item in iterable if condition]