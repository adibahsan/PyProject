items = ["Abby", "Brenda", "Cindy", "Diddy"]

for item in items:
    print(item)

for x in range(1, 10):
    print(x,end=" ")

print()
correctNumber = 5
guess = 0


while guess != correctNumber:
    guess = int(input("Guess the number: "))

    if guess != correctNumber:
        print('False guess')

print('You guessed the correct number')