#1
food=["rice", "beans"]
#2
food.append("brocolli")
#3
food.extend(["bread","pizza"])
print(food)
#4
print(food[0:2])
#5
print(food[food.index(food[-1])])
#6
breakfast="eggs fruit orange-juice".split()
print(breakfast)
#7
print(len(breakfast))
#8
lengths=[len(x) for x in breakfast]
print(lengths)