from curses.ascii import isalpha
import random
import io
import time
#To use sleep so to beautify the execution
count =0

def start():
    global show
    global word
    global guessed
    global original
    print("\nWelcome to Hangman game\n===================\n")
    time.sleep(1)
    print("Choose the topic: \n1. Literature\n2. Sports\n3. History\n4. Movies")
    n=int(input())
    if (n==1):
        f1=io.open('literature.txt','r', encoding="utf8")
        line1=f1.readline()
        litlist=line1.split()
        word=(random.choice(litlist))
        original=word
        word=word.lower()
        time.sleep(1)
        print("Guess the author")
        print("The word contains ",len(word)," letters")
        show ='_'*(len(word))
        game()
        guessed=[]

    if (n==2):
        f2=io.open('sports.txt','r', encoding="utf8")
        line2=f2.readline()
        litlist=line2.split()
        word=(random.choice(litlist))
        original=word
        word=word.lower()
        time.sleep(1)
        print("Guess the sport/adventure")
        print("The word contains ",len(word)," letters")
        show ='_'*(len(word))
        game()
        guessed=[]

    if (n==3):
        f3=io.open('kpolitics.txt','r', encoding="utf8")
        line3=f3.readline()
        litlist=line3.split()
        word=(random.choice(litlist))
        original=word
        word=word.lower()
        time.sleep(1)
        print("Guess the chief minister in kerala politics")
        print("The word contains ",len(word)," letters")
        show ='_'*(len(word))
        game()
        guessed=[]

    if (n==4):
        f4=io.open('movies.txt','r', encoding="utf8")
        line4=f4.readline()
        litlist=line4.split()
        word=(random.choice(litlist))
        original=word
        word=word.lower()
        time.sleep(1)
        print("Guess the famous english movie")
        print("The word contains ",len(word)," letters")
        show ='_'*(len(word))
        game()
        guessed=[]
    
    else:
        print("Inavlid choice!Please enter a choice from 1-4")
        start()

def call_again():
    global count
    count=0
    print("\nDo you want to play again?(y/n)")
    ch=input()
    if ch=='y':
        start()
        game()
    else:
        print("Thanks for playing.")
        time.sleep(2)
        exit()


def game():
    global word
    global show
    guessed=[]
    global count
    l=[]
    print("\nThe word is "+show)
    letter=input("Enter the letter: ")
    f=0
    
    if letter in word:
        l.extend([letter])
        pos = word.find(letter)
        word = word[:pos] + "_" + word[pos + 1:]
        show=show[:pos] + letter + show[pos+1:]
        f=1

    elif letter in l:
        print("Already guessed! Try another letter")
        f=2

    m=0
    if f==0:
        l.extend([letter])
        if letter.isalpha():
            print("\nSorry!! Wrong guess.")
            m=1

        else:
            print("\nInvalid choice. Please enter an alphabet.")
            game()

    elif f==1:
        print("\nGreat guess!!")
        if word == '_' * len(original):
            print("\nCongrats!!! You guessed the word correctly!")
            call_again()
    
    if m==1:
        count+=1
        if count==1:
            time.sleep(1)
            print("   _____ \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            
            print("You have ",(9-count)," chances")
        elif count ==2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("You have ",(9-count)," chances")

        elif count ==3:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("You have ",(9-count)," chances")
        
        elif count ==4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     O\n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("You have ",(9-count)," chances")

        elif count ==5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     O\n"
                  "  |     |\n"
                  "  |      \n"
                  "__|__\n")
            print("You have ",(9-count)," chances")

        elif count ==6:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     O\n"
                  "  |    /|\n"
                  "  |      \n"
                  "__|__\n")
            print("You have ",(9-count)," chances")

        elif count ==7:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     O\n"
                  "  |    /|\ \n"
                  "  |      \n"
                  "__|__\n")
            print("You have ",(9-count)," chances")

        elif count ==8:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     O\n"
                  "  |    /|\ \n"
                  "  |    / \n"
                  "__|__\n")
            print("You have ",(9-count)," chances")

        elif count ==9:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     O\n"
                  "  |    /|\\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            #print("You have ",(9-count)," chances")
    
    if count==9:
        print("Game Over!!!\nBetter luck next time.\nThe word is "+original)
        call_again()
    else:
        game()

    

start()