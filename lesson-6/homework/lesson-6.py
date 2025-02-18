#2
list1=list(input('Enter the first list: '))
list2=list(input('Enter the second list: '))

result=[x for x in list1 if x not in list2]+[y for y in list2 if y not in list1]

print(result)

#3
def underscore(txt):
    vowels = "aeiou"
    result = []
    i = 0

    while i < len(txt):
        part = txt[i:i+3]
        result.append(part)
        i += 3
        
        if i < len(txt):
            if part[-1] in vowels:
                result.append(txt[i])
                i += 1 
            result.append("_")
    return ''.join(result).rstrip("_")


print(underscore("hello"))  
print(underscore("assalom"))    
print(underscore("abcabcdabcdeabcdefabcdefg")) 
