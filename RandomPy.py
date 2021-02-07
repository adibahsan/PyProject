import random as rnd

ran1 = rnd.randint(1,10)
ran2 = rnd.uniform(1,10)
ran3 = rnd.randint(1,10)

print(ran1,ran2,ran3, sep='\n')

items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rnd.shuffle(items)
print(items)

x = rnd.sample(items, 1)   # Pick a random item from the list
print(x[0])

y = rnd.sample(items, 4)    # Pick 4 random items from the list
print(y)


items = ['Alissa','Alice','Marco','Melissa','Sandra','Steve']

x = rnd.sample(items, 1)   # Pick a random item from the list
print(x[0])

y = rnd.sample(items, 4)    # Pick 4 random items from the list
print(y)