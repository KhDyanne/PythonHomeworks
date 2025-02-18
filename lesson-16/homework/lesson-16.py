#1
import threading

def print_message(name):
    print(f'My name is {name}')
    
myThreads = []

for i in range(1, 10):
    thread = threading.Thread(target=print_message, args=(f'Thread {i}',))
    myThreads.append(thread)
    thread.start()

for i in myThreads:
    i.join()
    

#2
import threading
import requests

def download_file(url):
    filename = url.split("/")[-1]
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(filename, "wb") as file:
            file.write(response.content)
        print(f"Downloaded: {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {url}: {e}")

file_urls = [
    "https://tcmall.uz/strapi/uploads/2010750800_1_1_1_1_287ddf0b2b.jpg",
    "https://tcmall.uz/strapi/uploads/VS_1_8219_Asilbek_Azamov_1_a43c6b6034.jpg",
    "https://tcmall.uz/strapi/uploads/Artwork_SP_24_Brand_Tier3_CK_Jeans_Option75772x772px_Alexandra_Tarassova_50e0891002.jpg"
]

threads = [threading.Thread(target=download_file, args=(url,)) for url in file_urls]
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print("\nAll downloads completed!")


#3
even=[]
odd=[]

def even_nums(min,max):
    for i in range(min,max+1):
        if i%2==0:
            even.append(i)
    print(f'Even numbers: {even}')

def odd_nums(min,max):
    for i in range(min,max+1):
        if i%2==1:
            odd.append(i)
    print(f'Odd numbers: {odd}')

thread_even=threading.Thread(target=even_nums, args=(30,50))
thread_odd=threading.Thread(target=odd_nums,args=(30,50))

thread_even.start()
thread_even.join()
thread_odd.start()
thread_odd.join()



#4
result_list=[1,1]
def factorial(begin,end,index):
    result=1
    for i in range(begin,end+1):
        result*=i
    result_list[index]=result

def calculate_factorial(num):
    if num==0 or num==1:
        return 1

    mid=num//2
    thread1=threading.Thread(target=factorial, args=(1,mid,0))
    thread2=threading.Thread(target=factorial, args=(mid+1,num,1))

    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    
    return result_list[0]*result_list[1]
    

 
myNum=int(input('Enter a number: '))   
print(f'Factorial of {myNum}: {calculate_factorial(myNum)}')


#5
import threading
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)
def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1
    return merged
def multi_threaded_merge_sort(arr, num_threads):
    if num_threads <= 1:
        return merge_sort(arr)
    size = len(arr) // num_threads
    sublists = [arr[i:i+size] for i in range(0, len(arr), size)]
    threads = []
    sorted_sublists = []
    for sublist in sublists:
        thread = threading.Thread(target=lambda sublist: sorted_sublists.append(merge_sort(sublist)), args=(sublist,))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    merged = sorted_sublists[0]
    for sublist in sorted_sublists[1:]:
        merged = merge(merged, sublist)
    return merged
input_list = [ 12,1,8,3,2,5,3,7,4,3]
num_threads = 2
print("Original List:", input_list )
sorted_list = multi_threaded_merge_sort(input_list, num_threads)
print("Sorted list:", sorted_list)



#6
import threading

def partition(nums, low, high):
    i = low - 1
    pivot = nums[high]
  
    for j in range(low, high):
        if nums[j] <= pivot:
            i = i + 1
            nums[i], nums[j] = nums[j], nums[i]
  
    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    return i + 1


def quick_sort(nums, low, high):
    if low < high:
        pi = partition(nums, low, high)
  
        left_thread = threading.Thread(target=quick_sort, args=(nums, low, pi - 1))
        right_thread = threading.Thread(target=quick_sort, args=(nums, pi + 1, high))
  
        left_thread.start()
        right_thread.start()
        
        left_thread.join()
        right_thread.join()

arr = [40, 5, 18, 3, 0, 52, 32, 9, 5, 3]
print("Original array:", arr)

quick_sort(arr, 0, len(arr) - 1)

print("Sorted array:", arr)


#7
import requests
import threading
def make_request(url):
    response = requests.get(url)
    print(f"Response from {url}: {response.status_code}")
urls = [
    "https://www.wikipedia.org",
    "https://www.example.com",
    "https://www.google.com",
    "https://www.python.org"
]
threads = []
for url in urls:
    thread = threading.Thread(target=make_request, args=(url,))
    thread.start()
    threads.append(thread)
for thread in threads:
    thread.join()
