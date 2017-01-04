#IMPORT section
import collections

####################################################################################################################################C:\\Users\\Max\\PycharmProjects\\War_and_Peace.txt
#Here I request and open the file to be processed. Then I process it with the counter function, which automatically
# creates a dictionary-like structure that counts the occurrence of each word and has nice built-in functions such as most_common.

file_input = input('Which file would you like to inspect? Please provide the full path (including the filename.filetype!) if it is not in the current directory.') #request the file
#file_input = '[path_to_file]'   ### Note to reviewer: you can specify the pathname to your file here if you get tired of entering it. Just uncomment this line and comment the line directly above this line.
fin = open(file_input) #open the file

wordlist = [] #initiation of list

for line in fin:
    sentence = fin.readline() #this reads full lines
    words = sentence.split() #this converts lines into words
    for word in words:
        wordlist.append(word.lower()) #this adds the words to a list

file_count = collections.Counter(wordlist) #the counter function


########################################################################################################################
#Below is the user-interface. It has four options: (1) find the most used words in the document, (2) find the least used words in the document,
# (3) find the word count for a specific word and (4) exit the interface.

x = True #initiation of true variable for the while loop
while x:
    #below I ask the user what it wants to do
    option = input('\n In what way would you like to inspect your file? \n Type \'1\' if you would like to know which words are used most frequently in your text. \n Alternativey, you can type \'2\' if you would like to know which words are used the least in your text. \n If you would like to know the word count for a specific word, type \'3\'. \n Finally, if you are done inspecting your text, type \'4\'.')
    if option == str(1): #option (1)
        number = int(input("Specify how many of the most used words you would like to see."))
        prelim_list = file_count.most_common(int(number)) #This finds a list of the most used words, but it does not account for alphabet yet (e.g. if the user wants to find the most used word and 'a' and 'b' are both the most used word, this thing does not always give '' back yet.
        b = prelim_list[number-1] #this is thelast item on the list. useful to find the numbr corresponding to this item.
        name_b = b[0] #this is the name of the last item on the list. I do not use it here.
        number_b = b[1] #this is how often the last word in the list is used. This is helpful because this is the number such that other words who have this number of occurrences are also eligeble to be on the list.
        certain = [] #initiate list for the words that are 4sure on the list
        dubious = [] #initiate a list for the words tht have number_b as word count, so all the candidates that may or may not be on the list
        for item in file_count: #This goes through the whole counter and finds all the certain and then the dubious words. This is not very elegant, there should be a way to only go through the relevant items, instead of every item in the counter.
            if file_count[item] > number_b: #every word that is greater than number_b is 4sure on the list
                certain.append(item)
            if file_count[item] == number_b: #words with as wordcount number_b are dubious
                dubious.append(item)
        dubious.sort() #Finally, this sorts the dubious items alphabetically. Note that certain and dubious needed to be seperated up to this point because otherwise the dubious and 4sho words would get juggled together by this sort function.
        certain.extend(dubious) #This is a list of the 4sure items and then the dubious items in alphabetical order.
        print('\n') #white line for readability
        for word in certain[0:number]:
            print(word + '    ' + str(file_count[word])) #This prints the n most used words, together with their word count, with per line a 'word, wordcount' couple.
    elif option == str(2): #This option is very similar to option 1, except that some +'s are changed to -'s.
        number = int(input("Specify how many of the least used words you would like to see."))
        prelim_list = file_count.most_common()[:-(int(number))-1:-1]
        b = prelim_list[number - 1]
        nameb = b[0]
        numberb = b[1]
        certain = []
        dubious = []
        for item in file_count:
            if file_count[item] < numberb:
                certain.append(item)
            if file_count[item] == numberb:
                dubious.append(item)
        dubious.sort()
        certain.extend(dubious)
        print('\n')
        for word in certain[0:number]:
            print(word + '    ' + str(file_count[word]))

    elif option == str(3): #this option is very straight-forward thanks to the built-in function of counter. It returns the word with its wordcount, unless the wordcount is 0, then it apologizes.
        word = input('Please type (in lower cases) the word of which you would like to see the word count.')
        if file_count[word] == 0:
            print('\n Sorry, this word does not occur in the text.')
        else:
            print('\n' + word + ' ' + str(file_count[word]))

    elif option == str(4):
        print('\n Goodbye.') #exit message
        x = False #this makes x not true and thus stops the loop

    else:
        print('\n Sorry, I do not understand this. Please choose again.') #If the input value is invalid, the user returns to the previous menu
