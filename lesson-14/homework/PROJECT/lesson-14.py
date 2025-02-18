import os

os.mkdir("PROJECT")

import requests
import json

with open('actors.json', 'r') as file:
    actor_data = json.load(file)    
print(actor_data)

names=[]

for i in actor_data:
    names.append(i['name'])
        
print(names)  

for j in names:
    os.makedirs(j, exist_ok=True)

for i in actor_data:
    id=i['id']
    name=i['name']
    birthYear=i['birth_year']
    deathYear=i.get('death_year', 'N/A')
    nationality=i['nationality']
    image=i['image']
    
    path1=f'{name}/{name}.jpeg'
    path2=f'{name}/{name}_data.csv'
    
    with open(path2, 'w') as f:
        f.write("id,name,birth_year,death_year,nationality\n")
        
        f.write(f'{id},{name},{birthYear},{deathYear},{nationality}\n')
     
    with open(path1, 'wb') as f:
        respond=requests.get(image)
        f.write(respond.content)
