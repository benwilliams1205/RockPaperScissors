import random
strpcChoice = ""
strplayerChoice = ""
def runGame():
    pcChoice = random.choice([1,2,3])
    playerChoice = 0
    global playerScore
    global computerScore
    playerScore = 0
    computerScore = 0
    print(pcChoice)
    print("1 = Rock, 2 = Paper, 3 = Scissors")
    while 1 > playerChoice or 3 < playerChoice:
        try:
            playerChoice = int(input("Please enter your weapon choice (1-3): "))
        except ValueError:
            print("That was not a valid reponse")
    while not int(playerChoice) in range(1,4):
        try:
            playerChoice = input("Please enter your weapon choice (1-3): ")
        except ValueError:
            print("That wasn't a valid input")
    if playerChoice == 1:
        strplayerChoice = "Rock"
        if pcChoice == 1:
            strpcChoice = "Rock"
            print("You picked " + strplayerChoice)
            print("Computer picked " + strpcChoice)
            print("The game is a tie")
        elif pcChoice == 2:
            strpcChoice = "Paper"
            print("You picked " + strplayerChoice)
            print("Computer picked " + strpcChoice)
            print("You Lose")
            computerScore += 1
        elif pcChoice == 3:
            strpcChoice = "Scissors"
            print("You picked " + strplayerChoice)
            print("Computer picked " + strpcChoice)
            print("You win")
            playerScore+=1
    elif playerChoice == 2:
        strplayerChoice = "Paper"
        if pcChoice == 1:
            strpcChoice = "Rock"
            print("You picked " + strplayerChoice)
            print("Computer picked " + strpcChoice)
            print("You Win")
            playerScore+=1
        elif pcChoice == 2:
            strpcChoice = "Paper"
            print("You picked " + strplayerChoice)
            print("Computer picked " + strpcChoice)
            print("Tie")
        elif pcChoice == 3:
            strpcChoice = "Scissors"
            print("You picked " + strplayerChoice)
            print("Computer picked " + strpcChoice)
            print("You lose")
            computerScore += 1
    elif playerChoice == 3:
        strplayerChoice = "Scissors"
        if pcChoice == 1:
            strpcChoice = "Rock"
            print("You picked " + strplayerChoice)
            print("Computer picked " + strpcChoice)
            print("You lose")
            computerScore += 1
        elif pcChoice == 2:
            strpcChoice = "Paper"
            print("You picked " + strplayerChoice)
            print("Computer picked " + strpcChoice)
            print("You Win")
            playerScore+=1
        elif pcChoice == 3:
            strpcChoice = "Scissors"
            print("You picked " + strplayerChoice)
            print("Computer picked " + strpcChoice)
            print("Tie")
#----
print("Welcome to Rock, Paper, Scissors!")
runGame()

while True:
    playagain = str(input("Do you want to play again? (y/n)"))
    if playagain == 'y':
        runGame()
    elif playagain == 'n':
        print("Thanks for playing")
        print("You scored " + str(playerScore) + " points")
        print("The computer scored " + str(computerScore) + " points")
        if playerScore > computerScore:
            print("You are the winner")
        else:
            print("The computer beat you")
        break
    else:
        print("That was not a valid response")
