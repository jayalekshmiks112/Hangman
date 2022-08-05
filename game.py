import random
import io
import time #To use sleep so to beautify the execution

print("Welcome to Hangman game ")
time.sleep(1)
print("Choose the topic: \n1. Literature\n2. Sports\n3. History\n4. Films")
n=int(input())

def start():
    if (n==1):
        f1=io.open('literature.txt','r', encoding="utf8")
        line1=f1.readline()
        litlist=line1.split()
        word=random.choice(litlist)
        print(word)



start()