                          #PYTHON FUNCTIONS
                          
#1
def max_three(x,y,z):
    return max(x,y,z)

#2
def sum_all(list):
    return sum(list)
sum_all((8,2,3,0,7))

#3
def multiply(list):
    total=1    
    for i in list:
        total*=i        
    return total
multiply((8,2,3,-1,7))

#4
def reverse(string):
    return string[::-1]
reverse('1234abcd')

#5
def factorial(num):
    if num==0:
        return 1
    else:
        return num*factorial(num-1)
num=int(input('Enter a number: '))
factorial(num)

#6
def in_range(num,my_range):
    if num in range(my_range[0], my_range[1]):
        return 'In Range'
    else:
        return 'Not In Range'
   
in_range(3,[2,6])

#7
def my_count(string):
    count={'Upper Case':0, 'Lower Case':0}
    
    for i in string:
        if i.isupper():
            count["Upper Case"]+=1
        elif i.islower():
            count["Lower Case"]+=1
        else:
            pass
        
    print('Number of Upper Case Letter: ', count["Upper Case"])
    print('Number of Lower Case Letter: ', count["Lower Case"])
    
my_count('The quick Brow Fox')

#8
def distinct(my_list):
    return list(set(my_list))
distinct([1,2,3,3,3,3,4,5])

#9
def is_prime(num):
    if num==1:
        return False
    elif num==2:
        return True
    else:
        for i in range(2,num):
            if num%i==0:
                return False
        return True
    
is_prime(401)
    
    
#10
def is_even(my_list):
    result=[]
    for i in my_list:
        if i%2==0:
            result.append(i)
        else:
            pass
    return result

is_even([1,2,3,4,5,6,7,8,9])


#11
def isPerfect(num):
    x=[]
    
    for i in range(1,num):
        if num%i==0:
            x.append(i)
        else:
            pass
    
    if sum(x)==num:
        return 'Perfect Number'
    else:
        return 'Not Perfect'    

isPerfect(28)

#12
def isPalindrome(string):
    reversedString=string[::-1].lower().replace(" ","")
    
    if string.lower().replace(" ","")==reversedString:
        return 'Palindrome'
    else:
        return 'Not Paindrome'
    
isPalindrome('Madam')

#13
def pascalTriangle(n):
    row = [1]
    y = [0]
    for x in range(max(n, 0)):
        print(row)
        row = [l + r for l, r in zip(row + y, y + row)]
    return n >= 1
pascalTriangle(6)

    
#14
import string
def isPangram(my_string):    
    for letter in string.ascii_lowercase:
        if my_string.lower().count(letter)==0:
            return False
            break
    return True
        
isPangram("The quick brown fox jumps over the lazy dog")
      
      
#15
words=[n for n in input().split('-')]
words.sort()
print('-'.join(words))

#16
def square(x,y):
    squared=[n*n for n in range(x,y+1)]
    return squared
square(1,30)

#17
class color:
 PURPLE = '\033[95m'
 CYAN = '\033[96m'
 DARKCYAN = '\033[36m'
 BLUE = '\033[94m'
 GREEN = '\033[92m'
 YELLOW = '\033[93m'
 RED = '\033[91m'
 BOLD = '\033[1m'
 UNDERLINE = '\033[4m'
 ITALICS='\033[3m'
 END = '\033[0m'

print (color.BOLD + 'Hello World !' + color.END)
print (color.UNDERLINE + 'Hello World !' + color.END)
print (color.ITALICS + 'Hello World !' + color.END)


#18
code='''
def square(num):
    return num*num
print('Result is ', square(3))
'''
exec(code)

#19
def A(n1):
    def B(n2):
        return n2*n2+n1*n1
    return B
func=A(3)
print(func(2))


#20
def just():
    a=2
    b=9
    d='Diana'
    n='Nozima'
    
    print('just a random function')
    
print(just.__code__.co_nlocals)

#21
import time

def square(num):    
    return num*num

time.sleep(10)
square(3)

                            #PYTHON LAMBDA
                            
#Lambda

#1
l=lambda a: a+15
print(l(5))

l=lambda a,b: a*b
print(l(5,9))

#2
def func(x):
    return lambda a: a*x

result=func(3)
result(15)

#3
a=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
a.sort(key=lambda x: x[1])
print(a)

#4
b=[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
b.sort(key=lambda x: x['color'])
print(b)

#5
c=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('Original List:', c)
print('\nEven numbers for the list:')
even_numbers=list(filter(lambda x: x%2==0,c))
print(even_numbers)
print('\nOdd numbers for the list:')
odd_numbers=list(filter(lambda x: x%2==1,c))
print(odd_numbers)

#6
d=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square=list(map(lambda x: x*x,d))
print(square)

#7
startWith=lambda x: x.startswith('P')
print(startWith('Python'))
print(startWith('Java'))

#8
import datetime
now=datetime.datetime.now()
print(now)

year=lambda x: x.year
month=lambda x: x.month
day=lambda x: x.day
time=lambda x: x.time()

print(year(now))
print(month(now))
print(day(now))
print(time(now))

#9
isNum=lambda x: x.isnumeric()
print(isNum('Diana'))
print(isNum('1601'))
print(isNum('A2005'))

#10
n=10
fib_series=[0,1]
list(map(lambda _: fib_series.append(fib_series[-1]+fib_series[-2]), range(n)))

print(fib_series)

#11
f=[1, 2, 3, 5, 7, 8, 9, 10]
g=[1, 2, 4, 8, 9]

x=[]
intersection=list(filter(lambda a: a in f,g))
print(intersection)

#12
arrayL=[-1, 2, -3, 5, 7, 8, 9, -10]
positive=[x for x in arrayL if x>=0]
negative=[x for x in arrayL if x<0]

print(positive+negative)

#13
original_array = [1, 2, 3, 5, 7, 8, 9, 10]
even_count = len(list(filter(lambda x: x % 2 == 0, original_array)))
odd_count = len(list(filter(lambda x: x % 2 != 0, original_array)))
print("Number of even numbers in the above array:", even_count)
print("Number of odd numbers in the above array:", odd_count)

#14
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
filtered_days = list(filter(lambda x: len(x) == 6, days))
print(filtered_days)

#15
list1=[1,2,3]
list2=[4,5,6]

result=list(map(lambda i,j: i+j, list1,list2))
print(result)


#16
names = [{'Name': 'S ROY', 'Grade': 1}, {'Name': 'B BOSE', 'Grade': 3}, {'Name': 'N KAR', 'Grade': 2}, {'Name': 'C DUTTA', 'Grade': 1}, {'Name': 'G GOSH', 'Grade': 1}]
lowgrade = list(map(lambda i: (i['Name'], i['Grade']), names))

sortedGrade = sorted(lowgrade, key=lambda i: i[1])

uniqueGrades = sorted(set(grade for _, grade in sortedGrade))

second_lowest_student = [student for student in sortedGrade if student[1] == uniqueGrades[1]]

print(second_lowest_student)

#17
h = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]

newList = list(filter(lambda i: i % 19 == 0 or i % 13 == 0, h))
print(newList)

#18
k=['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']

palindromes=list(filter(lambda i: i[::-1]==i,k))
print(palindromes)

#19
l= ['bcda', 'abce', 'cbda', 'cbea', 'adcb']
target_string = 'abcd'
anagrams = list(filter(lambda x: sorted(x) == sorted(target_string), l))

print("Anagrams of '{}' in the above list:".format(target_string))
print(anagrams)


#20
m='sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5'
m=m.split(' ')
nums=list(filter(lambda i: i.isnumeric(),m))
int_list=list(map(int,nums))
result=sorted(list(filter(lambda i: i>len(m),int_list)))
print(result)

#21
n= [2, 4, 6, 9, 11]
given_num=2
result=list(map(lambda i: i*given_num,n))
print(result)

#22
names=['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']
result=list(filter(lambda i: i[0].isupper() ,names))
print(len(''.join(result)))

#23
original_array = [2, 4, -6, -9, 11, -12, 14, -5, 17]
pos_sum = sum(list(filter(lambda x: x>=0, original_array)))
neg_sum = sum(list(filter(lambda x: x<0, original_array)))

print('Sum of the positive numbes: ',pos_sum)
print('Sum of the negative numbes: ',neg_sum)

#24
def divisible_nums(start, end):
    return list(filter(lambda num: all(digit!='0' and num%int(digit)==0 for digit in str(num)),range(start,end+1)))

print(divisible_nums(1,25))

#25
def rearrange_bigger(n):
    nums = list(str(n))
    
    for i in range(len(nums) - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            z = nums[i:]        
            y = min(filter(lambda x: x > z[0], z))            
            z.remove(y)            
            z.sort()            
            nums[i:] = [y] + z            
            return int("".join(nums))    
    return False

n = 12
print("Original number:", n)
print("Next bigger number:", rearrange_bigger(n))

n = 10
print("\nOriginal number:", n)
print("Next bigger number:", rearrange_bigger(n))

n = 201
print("\nOriginal number:", n)
print("Next bigger number:", rearrange_bigger(n))

n = 102
print("\nOriginal number:", n)
print("Next bigger number:", rearrange_bigger(n))

n = 2451
print("\nOriginal number:", n)
print("Next bigger number:", rearrange_bigger(n)) 

#26
origin_list=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
max_list=max(filter(lambda x: x, origin_list))
min_list=min(filter(lambda x: x, origin_list))

print('\nList with max length: ',max_list)
print('\nList with min length: ',min_list)

#27
colors=[['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]
sorted_list=[sorted(i, key=lambda i:i[0]) for i in colors]
print(sorted_list)

#28
num_list=[[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
sort=sorted(num_list, key=lambda i: (len(i),i[0]))
print(sort)

#29
heterogeneous=['Python', 3, 2, 4, 5, 'version']
maxValue=max(filter(lambda i: isinstance(i, int), heterogeneous))
print(maxValue)

#30
original_matrix=[[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
sorted_matrix=sorted(original_matrix, key=lambda i: sum(i))
print(sorted_matrix)

#31
myList=['Python', 'list', 'exercises', 'practice', 'solution']
sizeString=list(filter(lambda i: len(i)==8, myList))
print(sizeString)

#32
mixedList=[1, 'abcd', 3.12, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
countFloats=len(list(filter(lambda i: isinstance(i, float),mixedList)))
print(countFloats)

#33
input_string = "W3resource"

valid_string = lambda s: (
    any(c.isupper() for c in s) and     
    any(c.islower() for c in s) and     
    any(c.isdigit() for c in s) and
    len(s) >= 6  
)
if valid_string(input_string):
    print(['Valid string.'])
else:
    print(['Invalid string.'])

#34
my_dict={'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}

filtered=dict(filter(lambda i: i[1][0]>6 and i[1][1]>=70, my_dict.items()))
print(filtered)

#35
p=[1, 2, 4, 6, 8, 10, 12, 14, 16, 17,15]

check=lambda i: i==sorted(i)

print(check(p))

#36
def myNthElement(n):
  q=[('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]

  nthElement=list(map(lambda i: i[n],q))
  print(nthElement)
  
myNthElement(1)

#37
def sortByIndex(n):
    r=[('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
    sorted_r=sorted(r,key=lambda i: i[n])
    print(sorted_r)

sortByIndex(0)
sortByIndex(2)

#38
list1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2=[2,4,6,8]

difference=list(filter(lambda i: i not in list2,list1))
print(difference)

#39
s=['red', 'black', 'white', 'green', 'orange']
pattern='ite'
isSubstring=list(filter(lambda i: pattern in i,s))
print(isSubstring)

#40
t1= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
t2=[[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]

intersection=[list(filter(lambda sublist2: sublist2 in t1, sublist1)) for sublist1 in t2]
print(intersection)

#41
myColors=['Red', 'Green', 'Blue', 'White', 'Black']
reverse=list(map(lambda i: i[::-1],myColors))
print(reverse)

#42
from functools import reduce
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
product = reduce(lambda x, y: x * y, list1)
print("Product of the said list numbers:", product)

#43
from functools import reduce
list1 = [4,3,2,2,-1,18]
product = reduce(lambda x, y: x * y, list1)
print("Product of the said list numbers:", product)

#44
p=((10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3))
pp=tuple(map(lambda i: sum(i)/len(i),zip(*p)))
print(pp)

#45
def tuple_int_str(tuple_str):
    result = tuple(map(lambda x: (int(x[0]), int(x[2])), tuple_str))
    return result

tuple_str =  (('233', 'ABCD', '33'), ('1416', 'EFGH', '55'), ('2345', 'WERT', '34'))

print("Original tuple values:")
print(tuple_str)

print("\nNew tuple values:")
print(tuple_int_str(tuple_str))

#46
s=[12, 33, 23, 10.11, 67, 89, 45, 66.7, 23, 12, 11, 10.25, 54]
max_s=max(s,key=lambda i: i)
min_s=min(s,key=lambda i: i)
print(s.index(max_s),',',max_s)
print(s.index(min_s),',',min_s)

#47
mixed_list = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]

sorted_list = sorted(mixed_list, key=lambda x: (isinstance(x, str), x))
print("Original list:")
print(mixed_list)
print("\nSorted list:")
print(sorted_list)

#48
t=['4', '12', '45', '7', '0', '100', '200', '-12', '-500']
tt=sorted(t, key=lambda i: int(i))
print(tt)

#49
u=[3, 4, 5, 8, 0, 3, 8, 5, 0, 3, 1, 5, 2, 3, 4, 2]
counts = {}
for item in u:
    counts[item] = (lambda x: counts.get(x, 0) + 1)(item)

print("Original list:")
print(u)
print("\nCount the occurrences of the items in the said list:")
print(counts)

#50
w=['orange', 'red', 'green', 'blue', 'white', 'black']
remove_target=['orange', 'black']
remove_w=list(filter(lambda i: i not in remove_target,w))
print(remove_w)

#51
v=[('V', 62), ('VI', 68), ('VII', 72), ('VIII', 70), ('IX', 74), ('X', 65)]
min_v=min(v, key=lambda i: i[1])
max_v=max(v, key=lambda i: i[1])
print('Min Value is ',min_v[1],',', 'Max value is ', max_v[1])

#52
z=[12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
remove_z=list(filter(lambda i: i!=None,z))
print(remove_z)



