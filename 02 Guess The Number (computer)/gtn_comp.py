import random

def gtn_comp():
    num = random.randint(1, 100)
    count = 0
    while True:
        userinput = int(input('Enter guess: '))
        count += 1
        if userinput == num:
            print(f"Correct guess. Chance took = {count}")
            exit(0)
        elif userinput < num:
            print("Guess higher number")
        elif userinput > num:
            print("Guess lower number")

if __name__ == "__main__":
    gtn_comp()