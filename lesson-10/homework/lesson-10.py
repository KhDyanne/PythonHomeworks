#Python class, Basic exercises

#1
import array
for name in array.__dict__:
    print(name)

#2
class MyClass1:
    x = 10
    y = 20

print("Namespace of MyClass:", MyClass1.__dict__)

#3
class MyClass2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

instance = MyClass2("Alice", 25)

print("Namespace of the instance:", instance.__dict__)

#4
import builtins
help(builtins.abs)
print(builtins.abs(-155))

#5
def myStudent(id,name,section):
    return f'Student ID is {id}, name is {name} and section is {section}'
myStudent('D2110206','Daniel','002')

#6
def student_data(student_id, student_name=None,student_class=None):
    print(f'Student ID is {student_id}')
    if student_name:
        print(f'Student name is {student_name}')
    if student_class:
        print(f'Student class is {student_class}')
    
student_data('D2110206','Daniel')

#7
class Student:
    pass
print(type(Student))
print(Student.__dict__.keys())
print(Student.__module__)

#8
class Student:
    pass

class Marks:
    pass

student=Student()
marks=Marks()

print(isinstance(student,Student))
print(isinstance(marks, Marks))
print(isinstance(student,Marks))
print(isinstance(marks, Student))
print(isinstance(Student,object))
print(isinstance(Marks,object))

#9
class Student:
    def __init__(self, student_name='Daniel', marks=87):
        self.student_name=student_name
        self.marks=marks
    def display_original(self):
        return f'Original Student Info: \nName: {self.student_name}, Marks: {self.marks}'
    def display_modified(self):
        return f'\nModified Student Info: \nName: {self.student_name}, Marks: {self.marks}'

student=Student() 
print(student.display_original())

student=Student('Diana', 95)
print(student.display_modified())

#10
class Student:
    def __init__(self, student_id, student_name):
        self.student_id=student_id
        self.student_name=student_name

student=Student(666,'Daniel')
student.student_class='12'

print(student.__dict__)

del student.student_name

print(student.__dict__)

#11
class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = None

    def set_student_class(self, student_class):
        self.student_class = student_class

    def display(self):
        attributes = self.__dict__  
        for attr, value in attributes.items():
            print(f"{attr}: {value}")

student = Student(666, "Daniel")
student.set_student_class("12")

print("Student Attributes:")
student.display()

#12
class Student:
    def __init__(self, student_id, student_name=None, marks_language=None, marks_science=None, marks_math=None):
        self.student_id = student_id
        self.student_name = student_name
        self.marks_language = marks_language
        self.marks_science = marks_science
        self.marks_math = marks_math

    def display_attributes(self):
        if self.student_name: 
            print(f"student_id -> {self.student_id}")
            print(f"student_name -> {self.student_name}")
        else: 
            print(f"student_id -> {self.student_id}")
            print(f"marks_language -> {self.marks_language}")
            print(f"marks_science -> {self.marks_science}")
            print(f"marks_math -> {self.marks_math}")

student_1 = Student(student_id="666", student_name="Daniel")
student_2 = Student(student_id="667", marks_language=56, marks_science=87, marks_math=76)

print("Student 1:")
student_1.display_attributes()

print("\nStudent 2:")
student_2.display_attributes()

#Python class, Basic application

#1
class RomanConverter:
    def __init__(self, number):
        self.number = number

    def to_roman(self):
        roman_numerals = {
            1000: "M", 900: "CM", 500: "D", 400: "CD",
            100: "C", 90: "XC", 50: "L", 40: "XL",
            10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"
        }

        result = ""
        num = self.number

        for value, numeral in roman_numerals.items():
            while num >= value:
                result += numeral
                num -= value         

        return result

number = int(input("Enter an integer (1 to 3999): "))
converter = RomanConverter(number)
print(f"Roman numeral: {converter.to_roman()}")

#2
class RomanToInteger:
    def __init__(self, roman):
        self.roman = roman.upper()

    def to_integer(self):
        roman_values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        integer_value = 0
        prev_value = 0

        for char in reversed(self.roman):
            current_value = roman_values[char]
            if current_value < prev_value:
                integer_value -= current_value
            else:
                integer_value += current_value
            prev_value = current_value

        return integer_value

roman_input = input("Enter a Roman numeral: ")
converter = RomanToInteger(roman_input)
print(f"Integer value: {converter.to_integer()}")

#3
class Validity:
    def isValid(self,str):
        list=[]
        chars={"(": ")", "{": "}", "[": "]"}
        for parenthese in list:
            if parenthese in chars:
                list.append(parenthese)
            elif len(list)==0 or chars[list.pop()]!=parenthese:
                return False
        return len(list)==0

print(Validity().isValid("()"))    
print(Validity().isValid("(){}[]"))
print(Validity().isValid("()[{)}"))
        
#4
class Unique:
    def subsets(self, set):
        return self.subsetRe([], sorted(set))
    
    def subsetRe(self, current,set):
        if set:
            return self.subsetRe(current, set[1:])+self.subsetRe(current+[set[0]],set[1:])
        return [current]
    
print(Unique().subsets([4,5,6]))

#5
class Pair:
    def sumPair(self,nums,target):
        pair={}
        for i, num in enumerate(nums):
            if target-num in pair:
                return (pair[target-num], i)
            pair[num]=i

print(Pair().sumPair((10,20,30,40,50,60,70),50))

#6
class ThreeSum:
    def sumThree(self, nums, target):
        nums.sort() 
        triplets = []

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == target:
                    triplets.append((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1

        return triplets
print(ThreeSum().sumThree([-25, -10, -7, -3, 2, 4, 8, 10], 0))

#7
class MyClass:
    def pow(self,num,degree):
        if num==0 or num==1 or degree==1:
            return num
        
        if num==-1:
            if degree%2==0:
                return 1
            else:
                return -1
        
        if degree==0:
            return 1
        
        if degree<0:
            return 1/self.pow(num,-degree)
        
        value=self.pow(num,degree//2)
           
        if degree%2==0:
            return value*value
    
        return value*value*num
    
print(MyClass().pow(2,-3))
print(MyClass().pow(3,5))
print(MyClass().pow(300,0))

#8
class py_solution:
    def reverse_words(self, s):
        return ' '.join(reversed(s.split()))

print(py_solution().reverse_words('hello .py'))

9
class String():
    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input()

    def print_String(self):
        print(self.str1.upper())

str1 = String()
str1.get_String()
str1.print_String()

#10
class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def rectangle_area(self):
        return self.length*self.width

newRectangle = Rectangle(12, 10)
print(newRectangle.rectangle_area())

#11
class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14
    
    def perimeter(self):
        return 2*self.radius*3.14

MyCircle = Circle(8)
print(MyCircle.area())
print(MyCircle.perimeter())

#12
import datetime
x = datetime.datetime.now()
print(type(x).__name__)



                         #REAL-LIFE PROBLEMS:
#1
class Employee:
    def __init__(self, name, emp_id, salary, department):
        self.name = name
        self.id = emp_id
        self.salary = salary
        self.department = department

    def calculate_salary(self, salary, hours_worked):
        overtime = 0
        if hours_worked > 50:
            overtime = hours_worked - 50
        self.salary = self.salary + (overtime * (self.salary / 50))

    def assign_department(self, emp_department):
        self.department = emp_department

    def print_employee_details(self):
        print("\nName: ", self.name)
        print("ID: ", self.id)
        print("Salary: ", self.salary)
        print("Department: ", self.department)
        print("----------------------")


employee1 = Employee("DANIEL", "E7876", 50000, "ACCOUNTING")
employee2 = Employee("JAMES", "E7499", 45000, "RESEARCH")
employee3 = Employee("JOAN", "E7900", 50000, "SALES")
employee4 = Employee("MONA", "E7698", 55000, "OPERATIONS")

print("Original Employee Details:")
employee1.print_employee_details()
employee2.print_employee_details()
employee3.print_employee_details()
employee4.print_employee_details()

employee1.assign_department("OPERATIONS")
employee4.assign_department("SALES")

employee2.calculate_salary(45000, 52)
employee4.calculate_salary(45000, 60)

print("Updated Employee Details:")
employee1.print_employee_details()
employee2.print_employee_details()
employee3.print_employee_details()
employee4.print_employee_details()

#2
class Restaurant:
    def __init__(self):
        self.menu_items = {}
        self.book_table = []
        self.customer_orders = []
    
    def add_item(self,item,price):
        self.menu_items[item]=price
        
    def book_tables(self,table_number):
        self.book_table.append(table_number)
        
    def customer_order(self, table_number,order):
        order_details={'table_number': table_number, 'order':order}
        self.customer_orders.append(order_details)
        
    def display_menu(self):
        for item,price in self.menu_items.items():
            print("{}: {}".format(item,price))
            
    def display_book_table(self):
        for table in self.book_table:
            print(f'Table {table}')
            
    def display_customer_orders(self):
        for order in self.customer_orders:
            print("Table {}: {}".format(order['table_number'], order['order']))
    
restaurant=Restaurant()

restaurant.add_item("Cheeseburger", 9.99)
restaurant.add_item("Caesar Salad", 8)
restaurant.add_item("Grilled Salmon", 19.99)
restaurant.add_item("French Fries", 3.99)
restaurant.add_item("Fish & Chips:", 15)

restaurant.book_tables(1)
restaurant.book_tables(2)
restaurant.book_tables(3)
    
restaurant.customer_order(1, "Cheeseburger")
restaurant.customer_order(1, "Grilled Salmon")
restaurant.customer_order(2, "Fish & Chips")
restaurant.customer_order(2, "Grilled Salmon")

print("\nMenu: ")
restaurant.display_menu()
print("\nReserved Tables: ")
restaurant.display_book_table()
print("\nCustomer Orders: ")
restaurant.display_customer_orders()

#3
class BankAccount:
    def __init__(self, account_number, date_of_opening, balance, customer_name):
        self.account_number = account_number
        self.date_of_opening  = date_of_opening 
        self.balance = balance
        self.customer_name = customer_name
        
    def deposit(self, amount):
        self.balance += amount
        print(f"${amount} has been deposited in your account.")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"${amount} has been withdrawn from your account.")
            
    def check_balance(self):
        print(f"Current balance is ${self.balance}.")
        
    def print_customer_details(self):
        print("Name:", self.customer_name)
        print("Account Number:", self.account_number)
        print("Date of opening:", self.date_of_opening)
        print(f"Balance: ${self.balance}\n")   

ac_no_1 = BankAccount(2345, "01-01-2011", 1000, "Toninho Takeo")
ac_no_2 = BankAccount(2312, "12-01-2009", 3000, "Orli Kerenza")
ac_no_3 = BankAccount(1395, "01-01-2011", 3000, "Luciana Chika")
ac_no_4 = BankAccount(6345, "01-05-2011", 4000, "Toninho Takeo")

print("Customer Details:")
ac_no_1.print_customer_details()
ac_no_2.print_customer_details()
ac_no_3.print_customer_details()
ac_no_4.print_customer_details()

print("=============================")
ac_no_4.print_customer_details()
ac_no_4.deposit(1000)
ac_no_4.check_balance()
ac_no_4.withdraw(5000)
ac_no_4.withdraw(3400)
ac_no_4.check_balance()

#4
class Inventory:
    def __init__(self):
        self.inventory = {}
    def add_item(self, item_id, item_name, stock_count, price):
        self.inventory[item_id] = {"item_name": item_name, 
                                   "stock_count": stock_count, 
                                   "price": price
                                  }
    def update_item(self, item_id, stock_count, price):
        if item_id in self.inventory:
            self.inventory[item_id]["stock_count"] = stock_count
            self.inventory[item_id]["price"] = price
        else:
            print("Item not found in inventory.")

    def check_item_details(self, item_id):
        if item_id in self.inventory:
            item = self.inventory[item_id]
            return f"Product Name: {item['item_name']}, 
                     Stock Count: {item['stock_count']}, 
                     Price: {item['price']}"
        else:
            return "Item not found in inventory."

inventory = Inventory()

inventory.add_item("I001", "Laptop", 100, 500.00)
inventory.add_item("I002", "Mobile", 110, 450.00)
inventory.add_item("I003", "Tablet", 90, 550.00)

print("Item Details:")
print(inventory.check_item_details("I001"))
print(inventory.check_item_details("I002"))
print(inventory.check_item_details("I003"))

print("\nUpdate the price of item code - 'I001':")
inventory.update_item("I001", 100, 505.00)
print(inventory.check_item_details("I001"))
print("\nUpdate the stock of item code - 'I003':")
inventory.update_item("I003", 115, 500.00)
print(inventory.check_item_details("I003"))



