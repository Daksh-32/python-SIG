import random

def main():
    random.seed()
    level = input("Choose a level : hard, medium or easy\n")
    chances = 0
    
    if level == "hard":
        chances = 1
        print(f"You have {chances} chances")
    elif level == "medium":
        chances = 3
        print(f"You have {chances} chances")
    elif level == "easy":
        chances = 5
        print(f"You have {chances} chances")
    
    secret_num = random.randint(1, 100)
    print("I have chosen a number between 1 and 100, Can you guess it?")
    guess = int(input())
    chances -= 1
    
    while chances > 0:
        if guess > secret_num:
            print("Too high, please try again: ", end="")
            chances -= 1
            guess = int(input())
        elif guess < secret_num:
            print("Too low, please try again: ", end="")
            chances -= 1
            guess = int(input())
        else:
            print("Congratulations, You have guessed the number!")
            break
    
    if chances <= 0:
        print("You have no chances remaining, please restart!")
        print(f"Correct answer is {secret_num}")

if __name__ == "__main__":
    main()