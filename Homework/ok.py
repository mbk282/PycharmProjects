#fin = open(r"""C:\Users\Max\PycharmProjects\War_and_Peace.txt""")

def dict_inverter(d):
    newdict = dict()
    for key, value in d.items():
        newdict.setdefault(value, []).append(key)
    return newdict

def indexer(d):
    counter = 0
    index_list = []
    for k in d:
        index_list[counter] = d[k]
        counter += 1
    #Use my sorter algorith to sort the list
    for n in range(0, len(index_list)):
        for i in range(n + 1, len(index_list)):
            if index_list[n] > index_list[i]:
                store = index_list[n]
                index_list[n] = index_list[i]
                index_list[i] = store
            else:
                pass
    return(index_list)

def dicts_inverter(dictio):
    index_list = indexer(dictio)
    keys_list = []
    for number in index_list:
        for key in dictio:
            if dictio[key] == number:
                keys_list[number] = key

def ranker(length):
    length = int(length)
    ranking = []
    n = 0
    while length > 0:
        index = inverted_dict.keys()
        print(index)
        print(type(index))
        indexlist = []
        for i in range(0,len(index)):
            indexlist[1] = index[i]
        index.sort()
        for i in index:
            indexed_list = inverted_dict[i]
            indexed_list.sort()
            for x in indexed_list:
                ranking[n] = x
                n += 1
                length -= 1
    return(ranking)






file_input = input('Which file would you like to inspect? Please provide the full path if it is not in the current directory.')
file = (file_input)
wordstorage = dict()
print(file)
fin = open(file)
for line in fin:
    sentence = fin.readline()
    lowercase_sentence = sentence.lower()
    words = lowercase_sentence.split()
    for word in words:
        if word not in wordstorage:
            wordstorage[word] = 1
        else:
            wordstorage[word] += 1
inverted_dict = dict_inverter(wordstorage)




x = True
while x:
    option = input('In what way would you like to inspect your file? \n Type \'1\' if you would like to know which words are used most frequently in your text. \n Alternativey, you can type \'2\' if you would like to know which words are used the least in your text. \n If you would like to know the word count for a specific word, type \'3\'. \n Finally, if you are done inspecting your text, type \'4\'.')
    if option == str(1):
            length_list = input('Please specify how long you want the list of most frequently used words to be by giving me a positive integer.')
            print(ranker(length_list))
    elif option == str(2):
        pass
    elif option == str(3):
        word = input('Please type the word of which you would like to see the word count.')
        print(wordstorage[word])
    elif option == str(4):
        x = False






