import sys

#C:\Users\Max\Downloads\1000mostFrequentWords.txt , C:\Users\Max\Downloads\user1.txt
def main(args):
    gold_words = set()
    student_words = set()

    try:
        with open('C:\\Users\\Max\\Downloads\\1000MostFrequentWords.txt') as goldFile:
            for line in goldFile:
                elements = line.split()
                if elements:
                    gold_words.add(elements[0])

        with open('C:\\Users\\Max\\Downloads\\user1_least.txt') as studentFile:
            for line in studentFile:
                elements = line.split()
                if elements:
                    student_words.add(elements[0])

    except FileNotFoundError:
        print("One of the files does not exist on your computer.")
        sys.exit(0)

    if len(gold_words) != len(student_words):
        print ('The lists are of different size. Please make sure to only ' +
               'use equally sized lists.')
        sys.exit(0)

    intersection = gold_words.intersection(student_words)
    overlap = float(len(intersection)) / len(gold_words) * 100

    print('The overlap between the gold list and the student ouput is {}%'.format(overlap))


if __name__ == '__main__':
    main(sys.argv[1:])