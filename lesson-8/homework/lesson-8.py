f=open('file.txt', 'r')
d={}

Text=f.read()
chars=['.',',','--','!','*','\n']
for i in chars:
    Text.replace(i,'')

Text=Text.split()

for word in Text:
    if word not in d.keys():
        d[word]=0
    else:
        d[word]+=1
    
print(d)