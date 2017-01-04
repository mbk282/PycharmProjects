import requests
import pickle
import html2text

artist_IDs = {}

urls = open("""C:\\Users\\Max\\PycharmProjects\\RapAnalyser\\API\\pop_artist_song_links""", 'r')
#
# urls = raw_song = [
# "http://genius.com/Rihanna-love-on-the-brain-lyrics",
# "http://genius.com/Uncle-dane-hey-now-youre-a-keemstar-lyrics",
# "http://genius.com/Flume-never-be-like-you-lyrics",
# "http://genius.com/Justin-bieber-love-yourself-lyrics",
# ]

for url in urls:
    url = url.strip('\n')
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    access_token = 'Bearer g7obord03PfeJ7TwQe-pNKVA0pQltMP6zGa76JKhGRIOOEDuB-IrsxdaHgXfue8c'
    headers = {'User-Agent': user_agent, 'Authorization': access_token}
    response = requests.get(url, headers=headers)

    html_data = response.text
    # get the primary artist and primary artist ID
    begin_marker = '"Primary Artist":'
    end_marker = ","

    parameter1 = str.find(html_data, begin_marker)
    parameter2 = str.find(html_data, end_marker, parameter1)
    primary_artist = html_data[parameter1 + len(begin_marker):parameter2]

    begin_marker = '"Primary Artist ID":'
    end_marker = ","
    parameter3 = str.find(html_data, begin_marker)
    parameter4 = str.find(html_data, end_marker, parameter3)
    primary_artist_id = html_data[parameter3 + len(begin_marker):parameter4]

    artist_IDs[primary_artist] = primary_artist_id



output = open('artistIDs.pkl', 'wb')
pickle.dump(artist_IDs, output)
output.close()

pkl_file = open('artistIDs.pkl', 'rb')
mydict2 = pickle.load(pkl_file)
pkl_file.close()
