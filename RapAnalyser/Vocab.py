import pickle
from bs4 import BeautifulSoup
import requests
from collections import Counter
import datetime

def lyrics_counter(songpath):
    """
    This takes a songpath to the genius website and gives back a counter based on the lyrics found on that webpage.
    This does not yet delete the [verse] boxes and also doesn't account for featuring artists
    :param songpath: url to a song on genius
    :return:
    """

    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    access_token = 'Bearer g7obord03PfeJ7TwQe-pNKVA0pQltMP6zGa76JKhGRIOOEDuB-IrsxdaHgXfue8c'
    headers = {'User-Agent': user_agent, 'Authorization': access_token}
    response = requests.get(songpath, headers=headers)
    text = response.text
    soup = BeautifulSoup(text, "html.parser")
    souptext = soup.get_text()
    souptext = souptext[500:]

    # find parameters lyrics
    begin_marker = 'Lyrics'
    end_marker = 'More on Genius'
    parameter1 = str.find(souptext, begin_marker)
    parameter2 = str.find(souptext, end_marker, parameter1)
    lyrics = souptext[parameter1 + len(begin_marker):parameter2]

    #Delete all the [hook] boxes
    begin_parameters = []
    end_parameters = []
    i = -1
    j = -1
    for letter in lyrics:
        i += 1
        j+=1
        if letter == '[':
            begin_parameters.append(i)
        elif letter == ']':
            end_parameters.append(j)
    begin_parameters.sort(reverse=True)
    end_parameters.sort(reverse=True)
    rangge = min(len(begin_parameters), len(end_parameters))
    for i in range(0,rangge):
        lyrics = lyrics[:begin_parameters[i]]+lyrics[end_parameters[i]:]




    processed_lyrics = lyrics.translate({ord(c): None for c in '!@#$?.,\"(){}<>:;\'%^&*|/\\'}).lower().split()



    wordlist = []  # initiation of list

    for word in processed_lyrics:
        wordlist.append(word)  # this adds the words to a list

    lyrics_count = Counter(wordlist)  # the counter function

    return (lyrics_count)

#This gets counters for artists. It gets a counter for every song and a total counter for the artist. TO DO: make it so that it gets onlt one file for all artists.

print('Begun at '+str(datetime.datetime.time(datetime.datetime.now())))

with open('C:\\Users\Max\PycharmProjects\RapAnalyser\\files\most_modest_songpaths.pkl', 'rb') as pick:
    file = pickle.load(pick)
    wordcount = {}
    u=0
    for key1 in file.keys():
        u+=1
        if u > 500:
            artist = key1.strip('""')
            print('working on artist '+artist+' ('+str(u)+'/'+str(len(file))+')(' +str(len(file[key1]))+')')
            artist_total_counter = Counter()
            wordcount[artist] = {}

            for key2 in file[key1].keys():
                song = key2
                song_counter = lyrics_counter(file[key1][key2])
                artist_total_counter += song_counter
                wordcount[artist][song] = song_counter

            wordcount[artist]['total_counter'] = artist_total_counter

            if u%25.0 == 0.0:
                filename = 'C:\\Users\Max\PycharmProjects\RapAnalyser\\files\wordcount_'+str(u)+'.pkl'
                with open(filename, 'wb') as counter_file:
                    pickle.dump(wordcount, counter_file)

    with open('C:\\Users\Max\PycharmProjects\RapAnalyser\\files\wordcount.pkl', 'wb') as counter_file:
        pickle.dump(wordcount, counter_file)

print('Done at ' + str(datetime.datetime.time(datetime.datetime.now())))



#Below it does calculations on the counters

# with open('C:\\Users\Max\PycharmProjects\RapAnalyser\\counter_Action Bronson.pkl', 'rb') as pick:
#     file = pickle.load(pick)
#     print(sum(file['total_counter'].values()))


