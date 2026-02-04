print(" Welcome to Number Guessing Game! ")
import random
n = random.randint(1,100)
difficulty_level = input("Choose the difficulty level(Hard or Easy): ").strip().lower()
count=0
def func_guessnum(n):
    if(difficulty_level=="hard"):
        count=5
    elif (difficulty_level=="easy"):
        count=10
    else:
        return "Invalid input"
    print(f"You have {count} attempts to guess the number.")
    while(count>0):
        guess=int(input("Make a guess : "))
        if (guess>n):
            print("Too high")
        elif (guess<n):
            print("Too low")
        elif(guess==n):
            print("You win")
            break
        else:
            print("Guess Again")
        count=count-1
func_guessnum(n)
print(n)
