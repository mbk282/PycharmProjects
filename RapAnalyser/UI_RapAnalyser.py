#import section
import urllib.request
import html2text
import re

#this configures the html textgetter
text_maker = html2text.HTML2Text()
text_maker.ignore_links = True #this puts off the annotations
text_maker.bypass_tables = True

#function definitions
def stripper(str):
    return(str.translate({ord(c): None for c in '!@#$?.,\"()[]{}<>:;\'%^&*|/\\'}))

#To do:
#- Give the UI the option to enter a new song
#- Rewrite this code into functions for better readability
#- If the song/artist name is invalid, let the user try again
#- Get the intro/verse/hook/artistnames etc. out somehow
#- Let the user give multi-word phrases as input

#(Hard) theoretical problems:
#- Fix the coroners / coroner's problem
#- We want only the text, so only verses and hooks? Or also intro/outro?

#This is all the internet stuff
root = "http://genius.com/"
glue = '-'
raw_song = input('Name a song you would like to analyse.')
raw_artist = input('Of what artist(s) is this song?')
endnote = "lyrics"

song = raw_song.replace(' ', '-')
artist = raw_artist.replace(' ', '-')

#Get problematic characters that are never in the url out of the song and artist name
song = song.translate({ord(c): None for c in '!@#$?.,\"()[]{}<>:;\'%^&*|/\\'})
artist = artist.translate({ord(c): None for c in '!@#$?.,\"()[]{}<>:;\'%^&*|/\\'})

print(song, artist)

url = root + artist + glue + song + glue + endnote
#url = "http://genius.com/Lil-kleine-and-ronnie-flex-drank-and-drugs-lyrics"
#url = "http://genius.com/Lil-wayne-6-foot-7-foot-lyrics"
#url = "http://genius.com/Fresku-kreeft-lyrics"
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers={'User-Agent':user_agent,}
# try
# except
request = urllib.request.Request(url,None,headers)
response = urllib.request.urlopen(request)

#this gets the text off of the website
data = response.read() #raw code
text_data = data.decode('utf-8') #raw code in text
text = text_maker.handle(text_data) #just text displayed on the website

#get the tile
begin_marker = '# '
end_marker = '\n'
parameter1 = str.find(text, begin_marker)
parameter2 = str.find(text, end_marker, parameter1)
song = text[parameter1+len(begin_marker):parameter2]

#get the artist
begin_marker = '## '
end_marker = '\n'
parameter1 = str.find(text, begin_marker)
parameter2 = str.find(text, end_marker, parameter1)
artist = text[parameter1+len(begin_marker):parameter2]

#get the album
begin_marker = 'Album '
end_marker = '\n'
parameter1 = str.find(text, begin_marker)
parameter2 = str.find(text, end_marker, parameter1)
album = text[parameter1+len(begin_marker):parameter2]



#find parameters lyrics
begin_marker = 'Lyrics'
end_marker = 'More on Genius'
parameter1 = str.find(text, begin_marker)
parameter2 = str.find(text, end_marker, parameter1)
lyrics = text[parameter1+len(begin_marker):parameter2]

def stripper(str):
    return(str.translate({ord(c): None for c in '!@#$?.,\"()[]{}<>:;\'%^&*|/\\'}))

lyrics_stripped = lyrics.translate({ord(c): None for c in '!@#$?.,\"()[]{}<>:;\'%^&*|/\\'})
lyrics_low = lyrics_stripped.lower()
lyrics_words = lyrics_low.split()


response.close()

#IMPORT section
import collections



file_count = collections.Counter(lyrics_words) #the counter function


########################################################################################################################
#Below is the user-interface. It has four options: (1) find the most used words in the document, (2) find the least used words in the document,
# (3) find the word count for a specific word and (4) exit the interface.

x = True #initiation of true variable for the while loop
while x:
    #below I ask the user what it wants to do
    option = input('\n In what way would you like to inspect your file? \n Type \'1\' if you would like to know which words are used most frequently in your text. \n Alternativey, you can type \'2\' if you would like to know which words are used the least in your text. \n If you would like to know the word count for a specific word, type \'3\'.\n If you would like to print the lyrics of your song, type \'4\'.\n Finally, if you are done inspecting your text, type \'X\'.')
    if option == str(1): #option (1)
        number = int(input("Specify how many of the most used words you would like to see."))
        prelim_list = file_count.most_common(int(number)) #This finds a list of the most used words, but it does not account for alphabet yet (e.g. if the user wants to find the most used word and 'a' and 'b' are both the most used word, this thing does not always give '' back yet.
        n = 1
        for item in prelim_list:
            print(str(n) + '. ' + str(item))
            n += 1
        print('\n') #white line for readability
    elif option == str(2): #This option is very similar to option 1, except that some +'s are changed to -'s.
        number = int(input("Specify how many of the least used words you would like to see."))
        prelim_list = file_count.most_common()[:-(int(number))-1:-1]
        n = 1
        for item in prelim_list:
            print(str(n) + '. ' + str(item))
            n += 1
    elif option == str(3): #this option is very straight-forward thanks to the built-in function of counter. It returns the word with its wordcount, unless the wordcount is 0, then it apologizes.
        word = input('Please type the word of which you would like to see the word count.')
        processed_word = stripper(word).lower()
        if file_count[processed_word] == 0:
            print('\n Sorry, this word does not occur in the text.')
        else:
            print('\n' + word + ' ' + str(file_count[processed_word]))
    elif option == str(4):
        print(lyrics)
    elif option == 'X':
        print('\n Goodbye.') #exit message
        x = False #this makes x not true and thus stops the loop

    else:
        print('\n Sorry, I do not understand this. Please choose again.') #If the input value is invalid, the user returns to the previous menu
