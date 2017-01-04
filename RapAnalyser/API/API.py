#import section
import requests
import json
import pickle
import html2text


#pkl_file = open('artistIDs.pkl', 'rb')
#artistIDs = pickle.load(pkl_file)


def modestifyer():
    """
    I never used this one
    :return:
    """
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    access_token = 'Bearer qN_1-XYxAf_CrLWMN8oHyWZZKbAKXb53kmvXUgB8wwqIIsiy-tFZCqqeB0WytD1X'
    headers={'User-Agent':user_agent, 'Authorization': access_token }

    begin_marker = '##  ['
    end_marker = ']'

    pdk_file = open('songpaths.pkl', 'rb')
    songpaths = pickle.load(pdk_file)

    modest_dict = {}

    for artist in songpaths:
        print('processing '+artist)
        modest_dict[artist] = {}
        for path in songpaths[artist]:
            response = requests.get(songpaths[artist][path], headers=headers)
            text = response.text
            #text = text.decode('utf-8')
            text = html2text.HTML2Text().handle(text)

            parameter1 = str.find(text, begin_marker)
            parameter2 = str.find(text, end_marker, parameter1)
            primary_artist = text[parameter1+len(begin_marker):parameter2]
            primary_artist = '"'+primary_artist+'"'
            if primary_artist == artist:
                modest_dict[artist][path] = songpaths[artist][path]


    output = open('filepaths_prime_artists', 'wb')
    pickle.dump(modest_dict, output)
    output.close()

    pdk_file.close()


#pdk_file = open('songIDs.pkl', 'rb')
# #songIDs = pickle.load(pdk_file)
# for artist in songIDs.keys():
#     modest_dict[artist] = {}
#     for song in songIDs[artist]:
#         songID = songIDs[artist][song]
#         url = "http://api.genius.com//songs//"+str(songID)+"?text_format=plain"
#         response = requests.get(url, headers=headers)
#         data = json.loads(response.text)
#         if data['meta']['status'] == 403:
#             pass
#         elif data["response"]["primary artist"]["name"] == artist:
#             modest_dict[artist][song] = songID


def modest_dict_getter():
    """
    This is what I used to convert the full songIDs to the modest songIDs. It takes the artistIDs (which I harvested with the chrome extension) and gets
    all the songs of that artist by going to the API of genius ang getting the songs.
    Update: I made this 'modest' by having it check whether the artist I am getting the songs off is also the primary artist of the song.
    Update: I made it more modest by excluding exceptions, such as remixes of old songs.
    :return:
    """
    pkl_file = open('artistIDs.pkl', 'rb')
    artistIDs = pickle.load(pkl_file)

    songIDs = {}
    songpaths = {}
    exceptions = ['remix', 'instrumental', 'radio edit', 'club mix' ' dub', 'tracklist', 'album art']
    n=0
    for artist in artistIDs:
        n+=1
        print('getting songs of '+str(artist)+' ('+str(n)+')')
        songIDs[artist] = {}
        songpaths[artist] = {}
        page = 1
        while True:
            url = "https://api.genius.com/artists/"+artistIDs[artist]+"/songs?sort=popularity&per_page=50&page="+str(page)
            user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
            access_token = 'Bearer g7obord03PfeJ7TwQe-pNKVA0pQltMP6zGa76JKhGRIOOEDuB-IrsxdaHgXfue8c'
            headers={'User-Agent':user_agent, 'Authorization': access_token }
            response = requests.get(url,headers=headers)
            data = json.loads(response.text)

            for song in data['response']['songs']:
                for exception in exceptions:
                    if exception in song.lower(): #disable this conditional if you would also like to include remixes and such
                        pass
                    else:
                        primary_artist = song['primary_artist']['name']
                        quoted_primary_artist = '"'+primary_artist+'"'
                        if quoted_primary_artist == artist: #disable this conditional if you would also like to include features and produced songs
                            songtitle = song['title']
                            songID = song['id']
                            songpath = song['url']
                            songIDs[artist][songtitle] = songID
                            songpaths[artist][songtitle] = songpath
            if data['response']['next_page'] == None:
                break
            page += 1

    output = open('modest_songIDs.pkl', 'wb')
    pickle.dump(songIDs, output)
    output.close()

    output = open('modest_songpaths.pkl', 'wb')
    pickle.dump(songpaths, output)
    output.close()

    pkl_file.close()



