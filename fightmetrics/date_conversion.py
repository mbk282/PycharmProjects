#this converts date in a text format to comparable nubers representing their date

def date_conversion(written_date):
    """

    :param written_date: must be in string format
    :return: a number representing the date
    """

    date_number = 0

    months = ['dummy', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

    elements = written_date.split()

    for i in range(0,13):
        if elements[0].lower() == months[i]:
            date_number += (i * 100)

    day = elements[1].strip(',')
    if len(day) == 1:
        day = '0' + day
    date_number += int(day)


    year = int(elements[2])
    date_number += (year*10000)

    return(date_number)



