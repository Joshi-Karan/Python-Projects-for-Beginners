import random

def rps():
    score_comp = score_user = 0
    print('Rock = r, Paper = p, Scissor = s, Exit = e')
    while True:
        choice_user = input('Enter Choice: ')
        choice_comp = random.choice(['r', 'p', 's'])
        if choice_user == choice_comp:
            print('Tie')
        elif choice_user == 'e':
            print(f"User score: {score_user}, Comp score: {score_comp}")
            exit(0)
        elif (choice_comp == 'r' and choice_user == 's') or (choice_comp == 'p' and choice_user == 'r') or (choice_comp == 's' and choice_user == 'p'):
            print('Computer won')
            score_comp += 1
        else:
            print('You won')
            score_user += 1

if __name__ == "__main__":
    rps()