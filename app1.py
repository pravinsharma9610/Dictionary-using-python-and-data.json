import json                                                                     # json is a standard module used to load data.json in this program
from difflib import get_close_matches as closer                                 #to get the close matches for the entered word

data=json.load(open("data.json"))                                               #Now data becomes a dict type ,beacuse it stores data.json in it.

def meaning(word):                                                              #function block

    word=word.lower()                                                           #Make user input to lower case

    if word in data:                                                            #if else block is used check whether the entered word exist's in the dict or not and give o/p accordingly
        return data[word]
    elif word.title() in data:                                                     #if user entered "texas" this will check for "Texas" as well.
        return data[word.title()]
    elif word.upper() in data:                                                     #in case user enters words like USA or NATO
        return data[word.upper()]

    elif len(closer(word,data.keys())[0])>0:
        yn=input("Do you mean '%s' instead? if yes press 'Y',if no press 'N': " % closer(word,data.keys())[0]) #get_close_matches(input,possibilities,no.=3,cutoff=0.6) #[0] selects 1st element from the pssible list

        if yn=="Y":
            return data[closer(word,data.keys())[0]]
        elif yn=="N":
            return "Word doesn't exist.Please Double check"
        else:
            return "We didn't understand your query"

    else:
        return "Word doesn't exist.Please Double check"

word= input('Enter a word: ')                                                   #to take input from user
array =meaning(word)

if type(array)==list:                                                           #function call
    b=1                                                                             #for indexing list
    for i in array:
        print(b,".",i)
        b=b+1
else:
    print(array)
