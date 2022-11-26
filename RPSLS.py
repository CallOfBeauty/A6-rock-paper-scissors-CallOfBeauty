#################################################################################
# Author(s):    Dimitrios Ntentia
# Username(s):  ntentiad
# Assignment:   A06-rock-paper-scissors-CallOfBeauty
# Purpose:      Create a fun game
#################################################################################
import random
import time
def winner(hh, cc):
    '''The function gets the inputs of the computer and the human'''
    winningpairs=[["rock","scissors"],["rock", "lizzard"],["paper", "rock"],["paper", "spock"],["scissors", "lizard"],["scissors", "paper"],["spock", "scissors"],["spock", "rock"],["lizard", "spock"],["lizard", "paper"]]
    '''This is a list of the dominant pairs, the first one is the winner, this way we can compare against and know the winner'''
    k=""
    l=""
    for i in winningpairs:
        k=str(i[0])+str(i[1])
        l=str(hh)+str(cc)
        if str(k)==str(l):
            return "human"
        else:
            return "computer"
def main():
    list = ["rock", "paper", "scissors", "spock", "lizard"]
    human=0
    computer=0
    playintent = input("do you wanna play?")
    while playintent=="yes":
        print("Hello, this is a game of rock, paper, scissors, spock, lizard!")
        time.sleep(0.5)
        hchoice=input("Please make your choice: ")
        time.sleep(0.5)
        cchoice=list[random.randrange(0,5)]
        if str(hchoice)==str(cchoice):
            computer+= 1
            human+=1
            print("Its a tie, you both chose", cchoice, "and the score is:\n-human: ",human,"\n-computer:", computer)
        else:
            print("You chose: ", hchoice, "\nand the computer chose: ", cchoice, ".")
            time.sleep(0.5)
            if winner(hchoice, cchoice) == "computer":
                computer+=1
            else:
                human+=1
            print("Therefore the winner is: ", winner(hchoice,cchoice), "\nand the score is:\n-human: ",human,"\n-computer:", computer)
        playintent = input("do you wanna play again?")
    print("The final score is ",computer,"for the computer, and ",human, "for the human")
if __name__ == "__main__":
    main()