import random

def gtn_comp():
    print('Select a number in your mind in range[1-100]. I will guess a random number and print it.\n You will enter a number for following options:\n 0.Guess lower number\n 1.Guess higher number\n 2.Perfect Guess\n')
    start = 0
    end = 100
    count = 0
    while True:
        guess = random.randint(start, end)
        count += 1
        print(guess)
        hint = int(input('Enter hint: '))
        if hint == 0:
            end = guess - 1
        elif hint == 1:
            start = guess + 1
        else:
            print(f"Bingo!! I took {count} chance to guess the correct Number")
            exit(0)


if __name__ == "__main__":
    gtn_comp()
