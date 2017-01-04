#Ask the user for a file to analyze
file = """C:\\Users\\Max\\Desktop\\War_and_Peace.txt"""

#Analyse the file: we first make a list 'data' of all words in this file
fin = open(file)
line = fin.readline()
data=[]
for line in fin:
    line_x = line.strip()
    words = line_x.split()
    for item in words:
        word = item.lower() #All words are lowercased
        data.append(word)

from collections import Counter #We use the Counter function for option 3 only

#We make a dictionary with the words as key, the count as value
def diction(x):
    freq_list = dict()
    for word in x:
        if not word in freq_list:
            freq_list[word] = 1
        else:
            freq_list[word] += 1
    return freq_list

d = diction(data)

#Here, the rest of the program starts
#Ask the user what he/she wants to do
while True:     #while loop in order to return to this question after finishing an option
    print('What do you want to do next?')
    while True:     #Check whether the input of the user is correct
        option = input('Choose (1) to look for the most frequent words, \n'
        'choose (2) to look for the least frequent words, \nchoose (3) to look for the count of'
        ' a specific word or \nchoose (4) to exit the program. ')
        if option.isdigit() and 1 <= int(option) <= 4:
            break;
        else:
            print('Sorry, I do not understand this. Please choose again. ')

#First option: show n most frequent words
    if int(option) == 1:
        n_most = input('How many of the most frequent words would you like to see? ')
        def invert_dict(d): #We define a small 'inverse' dictionary, with the word counts as key, the words as value
            inverse=dict()
            for key in sorted(d, key=d.get, reverse=True)[:int(n_most)]: #The inverse dictionary only contains the n most frequent words
                val=d[key]
                if val not in inverse:
                    inverse[val]=[key]
                else:
                    inverse[val].append(key)
            return inverse

        #This part ensures that words of the same count appear in alphabetical order
        print('The ', n_most, 'most frequent words are:',)
        for i in sorted(invert_dict(d),reverse=True):
            for j in range(0,len(invert_dict(d)[i])):
                print(sorted(invert_dict(d)[i])[j],i)

#Second option: show n least frequent words
    elif int(option) == 2:
        n_least = input('How many of the least frequent words would you like to see? ')
        def invert_dict(d): #We define an 'inverse' dictionary, with the word counts as key, the words as value
            inverse=dict()
            for key in sorted(d, key=d.get, reverse=True)[-1-int(n_least):-1]: #The inverse dictionary only contains the n least frequent words
                val=d[key]
                if val not in inverse:
                    inverse[val]=[key]
                else:
                    inverse[val].append(key)
            return inverse

        #This part ensures that words of the same count appear in alphabetical order
        print('The ', n_least, 'least frequent words are:')
        for i in sorted(invert_dict(d),reverse=True):
            for j in range(0,len(invert_dict(d)[i])):
                print(sorted(invert_dict(d)[i])[j],i)

#Third option: count a specific word
    elif int(option) == 3:
        while True:
            word = input('Which word do you want to count? ')
            if (Counter(data)[word]) == 0:
                print('Sorry, this word does not occur in the text.')
            else:
                break
        print('The word',word,'appears',Counter(data)[word],'times in', file+'.')

#Fourth option: exit the program
    elif int(option) == 4:
        print('Thank you for using this program. Bye!')
        exit()


#
# import sys
#
# #C:\Users\Max\Downloads\1000mostFrequentWords.txt , C:\Users\Max\Downloads\user1.txt
# def main(args):
#     gold_words = set()
#     student_words = set()
#
#     try:
#         with open('C:\\Users\\Max\\Downloads\\1000leastFrequentWords.txt') as goldFile:
#             for line in goldFile:
#                 elements = line.split()
#                 if elements:
#                     gold_words.add(elements[0])
#
#         with open('C:\\Users\\Max\\Downloads\\user1.txt') as studentFile:
#             for line in studentFile:
#                 elements = line.split()
#                 if elements:
#                     student_words.add(elements[0])
#
#     except FileNotFoundError:
#         print("One of the files does not exist on your computer.")
#         sys.exit(0)
#
#     if len(gold_words) != len(student_words):
#         print ('The lists are of different size. Please make sure to only ' +
#                'use equally sized lists.')
#         sys.exit(0)
#
#     intersection = gold_words.intersection(student_words)
#     overlap = float(len(intersection)) / len(gold_words) * 100
#
#     print('The overlap between the gold list and the student ouput is {}%'.format(overlap))
#
#
# if __name__ == '__main__':
#     main(sys.argv[1:])