import pickle

pkl_file = open('API\\modest_songpaths.pkl', 'rb')
artistIDs = pickle.load(pkl_file)

song_nrs = []

for key in artistIDs.keys():
    song_nrs.append((key, len(artistIDs[key])))

song_nrs.sort(key=lambda tup: tup[1], reverse=True)
print(song_nrs[:15])







