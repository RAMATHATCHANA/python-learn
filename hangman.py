import random
wordList=["aardvark","baboon","camel"]
word=random.choice(wordList)
print(word)
placeholder=""
for i in range(len(word)):
    placeholder+="_ "
print(placeholder)
correctLetter=[]
life=6
while life>0:
    guess=input("guess a letter: ").lower()
    if guess not in word:
        life=life-1
        print("Life Remaining -> ",life)
    display=""
    for letter in word:    
        if guess==letter:
            display+=guess
            correctLetter.append(guess)
        elif letter in correctLetter:
            display+=letter
        else:
            display+="_"
    print(display)
    if "_" not in display:
        print(display,"You win")
        break;
