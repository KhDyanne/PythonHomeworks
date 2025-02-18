                               #MAP

#1
a=[1,2,3,4,5,6,7]
triple_a=list(map(lambda i: i*3, a))
print(triple_a)

#2
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
nums3 = [7, 8, 9]

result = list(map(lambda x, y, z: x + y + z, nums1, nums2, nums3))
print(result)

#3
b=['ghost','red','royal blue','burgundy']
listify=list(map(list,b))
print(listify)

#4
bases_num = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

power=list(map(pow,bases_num,index))
print(power)

#5
c=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
power=list(map(lambda i: i**2,c))
print(power)

#6
chars = {'a', 'b', 'E', 'f', 'a', 'i', 'o', 'U', 'a'}
result=set(map(lambda i: (str(i).upper(),str(i).lower()),chars))
print(result)

#7
list1=[2,8,5,24,78]
list2=[4,9,8,5,3]

add_difference=list(map(lambda i,j:(i+j,i-j), list1,list2))
print(add_difference)

#8
myList=[2,6,12,4,33]
myTuple=(3,4,5,6,7,11)

print(list(map(str,myList)))
print(tuple(map(str,myTuple)))

#9
student_data  = [('Alberto Franco','15/05/2002','35kg'), ('Gino Mcneill','17/05/2002','37kg'), ('Ryan Parkes','16/02/1999', '39kg'), ('Eesha Hinton','25/09/1998', '35kg')]

students_data_name = list(map(lambda x: x[0], student_data))
students_data_dob = list(map(lambda x: x[1], student_data))
students_data_weight = list(map(lambda x: int(x[2][:-2]), student_data))

print("Name:")
print(students_data_name)

print("Date of birth:")
print(students_data_dob)

print("Weight:")
print(students_data_weight)

#10
def square_fibonacci(n):
    firstFib=[0,1]
    for i in range(2,n):
      firstFib.append(firstFib[-1]+firstFib[-2])
    
    result=list(map(lambda i: i**2,firstFib))
    return(result)
print('First 10 square of Fibonacci numbers: ')
print(square_fibonacci(10))

#11
d=[2,3,4,5,6,7,88,90]
def compute_sum(array):
    integers = map(int, array)
    return sum(integers)
compute_sum(d)

#12
e=[1,2,4,-5,6,0,-24,43,0,43,23,594,-5,6,7,-88,0]

positives=list(map(lambda i: i>0, e)).count(True)
negatives=list(map(lambda i: i<0, e)).count(True)
zeroes=list(map(lambda i: i==0, e)).count(True)

pos_ratio=positives/len(e)
neg_ratio=negatives/len(e)
zero_ratio=zeroes/len(e)

print(pos_ratio)
print(neg_ratio)
print(zero_ratio)

#13
nums1 = [1, 2, 3, 4, 5, 6, 7, 8]
nums2 = [2, 2, 3, 1, 2, 6, 7, 9]

pairs=list(map(lambda i,j: (i,j) if i==j else None,nums1,nums2))
same_pairs=list(filter(lambda i: i!=None,pairs))

print("Number of matching pairs: ", len(same_pairs))

#14
import random

nums1 = [1, 2, 7, 8, 3, 7]
nums2 = [4, 3, 8, 9, 4, 3, 8, 9]

def interleave_lists(list1, list2):
    combined = list1 + list2
    random.shuffle(combined)
    return combined

interleave_lists(nums1,nums2)

#15
myDict={'Math': [95,49,56,87,90], 'Biology': [77,79,84,90,80]}

keys=myDict.keys()
values=zip(*myDict.values())
print(values)
print(keys)

myList=list(map(lambda i: dict(zip(keys,i)),values))
print(myList)

#16
myList1=['Diana', 'Nozima', 'Oysha']
list_list=list(map(list,myList1))
print(list_list)

#17
myTuple2=[('Diana'), ('Nozima'), ('Oysha')]
list_str=list(map(str,myTuple2))
print(list_str)


                            #Filter

#1
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result=list(filter(lambda i: i%2==0, nums))
print(result)

#2
mixed_case_strings = ["Hello", "w3resource", "Python", "Filter", "Learning"]
result1=list(filter(lambda i: i.isupper(), ''.join(mixed_case_strings)))
print(result1)

#3
numbers = [20, 15, 24, 37, 23, 11, 7]
target=20
result2=list(filter(lambda i: i<=target,numbers))
print(result2)

#4
vowels=['A','E','I','O','U']
names = ["Elita", "Vitold", "Audovacar", "Kerensa", "Ramana", "Iolanda", "Landyn"]

result3=list(filter(lambda i: i[0] in vowels, names ))
print(result3)

#5
names = ["Elita", "", "Audovacar", "", "Ramana", "", "Landyn"]
result4=list(filter(lambda i: i!='',names))
print(result4)

#6
students=[
    {'name':'Dyanne', 'age': 20, 'grade': 97},
    {'name':'Enzy', 'age': 19, 'grade': 89},
    {'name':'Ayse', 'age': 19, 'grade': 76},
    {'name':'Nick', 'age': 22, 'grade': 100}
]    

result5=list(filter(lambda i: i['grade']>=95, students))
print(result5)

#7
nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
def isPrime(n):
        if n<2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n%i==0:
                return False
        return True
result6=list(filter(lambda i: isPrime(i),nums))
print(result6)

#8
words=['apple','tablet','laptop','keyboard','mouse','water']
result7=list(filter(lambda i: len(i)>5, words))
print(result7)

#9
names = ["Elita", "Vitold", "Audovacar", "Kerensa", "Ramana", "Iolanda", "Landyn"]
substring='ensa'

result8=list(filter(lambda i: substring in i, names))
print(result8)

#10
from datetime import datetime

date_strings = ["2023-07-11", "2022-02-22", "2024-05-11", "2025-12-31", "2021-01-01"]
now=datetime.now()

result9=list(filter(lambda i: datetime.strptime(i,"%Y-%m-%d")>now, date_strings))
print(result9)

#11
cities = [
    ("New York", 8500000),
    ("Los Angeles", 4000000),
    ("Chicago", 2700000),
    ("Houston", 2300000),
    ("Phoenix", 1600000),
    ("Philadelphia", 1500000),
    ("San Antonio", 1500000),
]

result10=list(filter(lambda i: i[1]>2000000,cities))
print(result10)

