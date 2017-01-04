import pickle

###Use thi to open and print a file
with open('files\wordcount_200.pkl', 'rb') as pick:
    file = pickle.load(pick)
    print(len(file))

# with open('files\modest_songpaths.pkl', 'rb') as pick:
#     file = pickle.load(pick)
#     dict = {}
#     for artist in file.keys():
#         dict[artist]= {}
#         for song in file[artist].keys():
#             while True:
#                 for exception in exceptions:
#                     if exception in song.lower():
#                         break
#                 dict[artist][song] = file[artist][song]
#                 break

#####This is a miscelaneous piece of code that lets you edit the content of a dictionary



# with open('files\modest_songpaths.pkl', 'rb') as pick:
#     file = pickle.load(pick)
#     for artist in file.keys():
#         to_delete = []
#         for song in file[artist].keys():
#             for exception in exceptions:
#                 if exception in song.lower():
#                     to_delete.append(song)
#                     break
#         for i in to_delete:
#             del (file[artist][i])
#
# with open('files\most_modest_songpaths.pkl', 'wb') as newpick:
#     pickle.dump(file, newpick)














# with open('C:\\Users\Max\PycharmProjects\RapAnalyser\\counter_Action Bronson.pkl', 'rb') as pick:
#     file = pickle.load(pick)
#     summ = sum(file['total_counter'].values())
#     lenn = len(file['total_counter'])
#     print(lenn)
#     print(summ)
#     print(lenn/summ)
#
# with open('C:\\Users\Max\PycharmProjects\RapAnalyser\\counter_Logic.pkl', 'rb') as pick:
#     file = pickle.load(pick)
#     print(file['total_counter'])
