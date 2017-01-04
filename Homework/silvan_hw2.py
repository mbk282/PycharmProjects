#Assignment 2, Basic Probability Programming, November 2016
#------------------------------------------------------------

#1. Ask user for path to file and read file into text memory

#take user input concerning the path to the file
print("Hello, welcome to the wonderful world of counting words. Please tell me exactly where I can find the text file you would like to have words counted in.")
path_to_text=input(">>>")

#open the file for reading
initial_text=open(path_to_text, 'r')

#prepare file by making it into list of strings (list of the individual words)
text_natural=[] #empty list in which we write the initial_text

for line in initial_text:   #write each line in text file as element of a list
    zeile = line.strip()
    text_natural.append(zeile)

text_natural=str(text_natural).lower() #convert list to string so it becomes splitable

delimiter = ' ' #define space as delimiter
text_individual_words = text_natural.split(delimiter) #text_individual_words is now a list of strings, ready to count

#2. counting words
#use Counter module to count the words in text_individual_words so the data is ready for interact with the user in point 3
import collections
counter=collections.Counter(text_individual_words)

#the following defines a function that gets the least n elements from counter, it will be used below when interacting with the user
from operator import itemgetter
import heapq
import collections

def least_common(array, to_find=None):
    counter = collections.Counter(array)
    if to_find is None:
        return sorted(counter.items(), key=itemgetter(1), reverse=False)
    return heapq.nsmallest(to_find, counter.items(), key=itemgetter(1))

#3. Ask user what she wants to do. The options are: getting most/least frequent words; get count of specific word; exit.

print("What would you like to know about this text. I have four wonderful options for you:")
print("1. Show the most frequent words.")
print("2. Show the least frequent words.")
print("3. Obtain the number of times a word appears in the text.")
print("4. Exit this little interaction.")
print("Please indicate your preference by writing 1,2,3 or 4:")
initial_decision=input(">>>")
initial_decision=int(initial_decision) #process input to make sure it has the right type

while initial_decision!=4:      #if user's input equals 4 program stops running, otherwise it goes to the corresponding option

    if initial_decision==1:
        print("Up to how many words do you want to know this?")
        decision_one=input('>>>')
        print('Most frequent:')
        for string, count in counter.most_common(int(decision_one)): #this function was already built-in
            print('\'{}\' {:>7}'.format(string, count))

        print("What else would you like to know about this text. The options haven't changed:") #going back to 4 options again
        print("1. Show the most frequent words.")
        print("2. Show the least frequent words.")
        print("3. Obtain the number of times a word appears in the text.")
        print("4. Exit this little interaction.")
        print("Please indicate your preference by writing 1,2,3 or 4:")
        initial_decision=input('>>>')
        initial_decision=int(initial_decision)

    if initial_decision==2:
        print("Up to how many words do you want to know this?")
        decision_two=input('>>>')
        decision_two=int(decision_two)
        print('Least frequent:')
        for letter, count in least_common(counter, decision_two): #for argument1(=database counter) and argument2(=length of list) look for the n elements with the least frequency
            print('\'{}\' {:>7}'.format(letter, count))

        print("What else would you like to know about this text. The options haven't changed:") #going back to 4 options again
        print("1. Show the most frequent words.")
        print("2. Show the least frequent words.")
        print("3. Obtain the number of times a word appears in the text.")
        print("4. Exit this little interaction.")
        print("Please indicate your preference by writing 1,2,3 or 4:")
        initial_decision=input('>>>')
        initial_decision=int(initial_decision)

    if initial_decision==3:
        print("Which word would you like to know about?")
        decision_three=input('>>>')
        keyword=str(decision_three).lower()
        if keyword in text_individual_words:
            print('\'{}\' {}'.format(keyword, counter[keyword]))
        else: print("Sorry, this word does not appear in the text.")

        print("What else would you like to know about this text. The options haven't changed:") #going back to 4 options again
        print("1. Show the most frequent words.")
        print("2. Show the least frequent words.")
        print("3. Obtain the number of times a word appears in the text.")
        print("4. Exit this little interaction.")
        print("Please indicate your preference by writing 1,2,3 or 4:")
        print(">>>")
        initial_decision=input('>>>')
        initial_decision=int(initial_decision)

    if initial_decision!= (1 or 2 or 3 or 4): #handling the case where input is invalid
        print("Scusi, I do not understand this. Please choose again. The options haven't changed:") #going back to 4 options again
        print("1. Show the most frequent words.")
        print("2. Show the least frequent words.")
        print("3. Obtain the number of times a word appears in the text.")
        print("4. Exit this little interaction.")
        print("Please indicate your preference by writing 1,2,3 or 4:")
        print(">>>")
        initial_decision=input('>>>')
        initial_decision=int(initial_decision)

print("It has been delightful to interact with you! Can't wait for you to use this program again soon! Doei!") #output in case user wishes to exit

