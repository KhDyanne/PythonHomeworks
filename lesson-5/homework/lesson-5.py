# 1. Given a list of tuples where each tuple contains a name and a score, 
# create a new list that contains the names of students who scored above 80.
# Example input: [('Mike', 75), ('Joe', 90), ('Beck', 85)]
# Expected output: ['Joe', 'Beck']

list_tuples=[('Mike', 75), ('Joe', 90), ('Beck', 85)]
new_list=[]

for name, score in list_tuples:        
    if score>80:
        new_list.append(name)

print(new_list)
    

# 2. Given a tuple with several lists inside it, 
# write a function to return the list with the maximum sum of its elements.
# Example input: ([1, 2], [3, 4], [5, 6, 7])
# Expected output: [5, 6, 7]

tuple_list=([1, 2], [3, 4], [5, 6, 7], [8,1,1,1])
max_elements=max(tuple_list, key=sum)
print(max_elements)

# 3. Given a list of tuples with names and ages, 
# return a list of names where the age is greater than 30 and less than 50.
# Example input: [('Mike', 25), ('Joe', 31), ('Beck', 40)]
# Expected output: ['Joe', 'Beck']

info_list=[('Mike', 25), ('Joe', 31), ('Beck', 40)]
new_list=[]

for name, age in info_list:        
    if age>30 and age<50:
        new_list.append(name)

print(new_list)


# 4. Given a list of integers, 
# write a function to return a list of tuples where the first element is the number 
# and the second is 'Even' or 'Odd' depending on whether the number is even or odd.
# Example input: [1, 2, 3, 4]
# Expected output: [(1, 'Odd'), (2, 'Even'), (3, 'Odd'), (4, 'Even')]

nums=[1,2,3,4]

def func1(nums):
 result=[]
 for i in nums:
    if i%2==0:
      result.append((i, 'Even'))
    else:
      result.append((i, 'Odd'))        
 return result

print(func1(nums))

# 5. Given a list of tuples containing a string and an integer, 
# write a function that returns a tuple of the string with the largest length 
# and its corresponding integer. If two strings have the same length, 
# choose the one with the larger integer.
# Example input: [('apple', 5), ('banana', 4), ('cherry', 6)]
# Expected output: ('apple', 5)

fruits=[('apple', 5), ('banana', 4), ('cherry', 6)]
max_fruit=max(fruits, key=lambda x: (len(x[0]), x[1]))
print(max_fruit)

# 6. Given a list of tuples where each tuple contains a date (as a string in 'YYYY-MM-DD' format) and an event, 
# return the list of events in the order of the most recent dates.
# Example input: [('2024-12-01', 'Event A'), ('2025-01-01', 'Event B')]
# Expected output: [('2025-01-01', 'Event B'), ('2024-12-01', 'Event A')]

events=[('2024-12-01', 'Event A'), ('2025-01-01', 'Event B')]

def recent_event(event):
    return sorted(event,key=lambda x: x[0], reverse=True)

print(recent_event(events))
    

# 7. Given a list of tuples where each tuple contains a name and a score, 
# return the highest score and the corresponding name.
# Example input: [('Mike', 75), ('Joe', 90), ('Beck', 85)]
# Expected output: ('Joe', 90)

names=[('Mike', 75), ('Joe', 90), ('Beck', 85)]

max_score=max(names, key=lambda x: x[1])
print(max_score)
    


# 8. Given a list of tuples where each tuple contains a product name and its price, 
# write a function to return a list of products whose price is between 50 and 100.
# Example input: [('product1', 45), ('product2', 60), ('product3', 120)]
# Expected output: [('product2', 60)]

products=[('product1', 45), ('product2', 60), ('product3', 120)]
result=[]

for i,j in products:
    if j>50 and j<100:
        result.append((i,j))
    
print(result)


# 9. Given a list of tuples where each tuple contains a person's name and their age, 
# return the name of the oldest person in the list.
# Example input: [('Mike', 25), ('Joe', 31), ('Beck', 40)]
# Expected output: 'Beck'

names=[('Mike', 25), ('Joe', 31), ('Beck', 40)]

max_score=max(names, key=lambda x: x[1])
print(max_score[0])

# 10. Given a list of tuples containing a student's name and their grades in multiple subjects, 
# return the names of students who have an average grade greater than 80.
# Example input: [('Mike', [85, 75, 90]), ('Joe', [70, 80, 60])]
# Expected output: ['Mike']

students=[('Mike', [85, 75, 90]), ('Joe', [70, 80, 60])]
result=[]

for name, grades in students:
    if sum(grades)/len(grades)>80:
        result.append(name)
        
print(result)


