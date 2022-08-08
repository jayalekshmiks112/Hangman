# HANGMAN Game in Python
****
### ACKNOWLEDGEMENT<br>
This project is done as a part of Cod(h)er program by Tinkerhub foundation
### EXPLANATION<br>
1. Created different text files with differnt words in it <br>
2. In game.py<br>
>>1. Import random, time, curses
>>2. In start():
>>>>1. Depending on the selection of the option, different files are read and a random word is generated
>>3. In call_again():
>>>>1. Depending on the choice of y/n the loop is executed
>>4. In game():
>>>>1. Letter is taken as an input
>>>>2. In a loop, check if the letter is in the word
>>>>>>1. if so then find the postion of atht letter in the word
>>>>>>2. Replace that postion in the word with "_"
>>>>>>3. Replace show with the position with atht letter 
>>>>3. Check if the letter is already accepted
>>>>4. Check if the entered is a an alphabet using isalpha()
>>>>5. Check if the word is completed or not
>>>>6. If wrong, hangman's different parts are displayed based on the count
### FAQS
1. Can the word generated without using files?<br>Yes, word can be generated from a list

## THANK YOU

