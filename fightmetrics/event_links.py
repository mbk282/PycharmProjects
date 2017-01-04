from bs4 import BeautifulSoup
import requests
import math
import pickle
from fighters import Fighter

from date_conversion import date_conversion

#EVENT SECTION

# file = open('sorted_event_links.txt', 'r')
# for line in file:
#     print(line[2])
# file.close()

#This gets the sorted event list to access urls
# file = open('events_and_dates(numbers).pkl', 'rb')
# pick = pickle.load(file)
# tuple_list = pick.items()
#
# sorted = sorted(tuple_list, key=lambda x: x[1])
# for line in sorted:
#     print(line[0])

# sorted_event_links_file = open('sorted_event_links.txt', 'w')
# for line in sorted:
#     sorted_event_links_file.write(str(line)+'\n')
# sorted_event_links_file.close()
#
# file.close()

# with open('events_and_dates.pkl', 'rb') as file:
#     reader = pickle.load(file)
#     new_dict = {}
#     for line in reader:
#         x = line
#         y = reader[line]
#         new_dict[line] = date_conversion(reader[line])
#     file.close()
#
# pick = open('events_and_dates(numbers).pkl', 'wb')
# output = pickle.dump(new_dict, pick)
# pick.close()

def event_analyses(url):
    """

    :param url: url of an event
    :return:
    """
    fightlinks = fight_links(url)
    for link in fightlinks:
        fight_result = fight_analysis(link)
        if type(fight_result[0]) is None:
            pass
        elif type(fight_result[1]) is None:
            pass
        elif type(fight_result) is None:
            pass
        elif fight_result is None:
            pass
        elif fight_result[0] is None:
            pass
        elif fight_result[1] is None:
            pass
        else:
            winner = fight_result[0].text
            loser = fight_result[1].text
            #this type
            if winner not in fighters_dict:
                fighters_dict[winner] = 1500.0
            if loser not in fighters_dict:
                fighters_dict[loser] = 1500.0
            score_updater(winner, loser)

def prediction(fighter1, fighter2):
    odds_fighter_1 = (1.0 / (1.0 + math.pow(10.0, ((fighters_dict[fighter2] - fighters_dict[fighter1]) / 400.0))))
    return(odds_fighter_1)

def score_updater(winner, loser):
    predict = prediction(loser, winner)
    fighters_dict[winner] += predict * 32.0
    fighters_dict[loser] -= predict * 32.0




#This gets all the links to fights off of an event page
def fight_links(url):
    """
    :param url: pass 1 url of an event
    :return:  get a list of urls to fight pages
    """
    fightlinks = []
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    access_token = 'Bearer g7obord03PfeJ7TwQe-pNKVA0pQltMP6zGa76JKhGRIOOEDuB-IrsxdaHgXfue8c'
    headers = {'User-Agent': user_agent, 'Authorization': access_token}
    response = requests.get(url, headers=headers)
    text = response.text
    soup = BeautifulSoup(text, "html.parser")
    links = soup.find_all('a', href=True)
    for link in links:
        if 'http://www.fightmetric.com/fight-details' in link['href']:
            fightlinks.append(link['href'])
    return(fightlinks)

# #FIGHT SECTION: This gets the loser, winner and eventname of this fight, given an URL of a fight
def fight_analysis(url):
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    access_token = 'Bearer g7obord03PfeJ7TwQe-pNKVA0pQltMP6zGa76JKhGRIOOEDuB-IrsxdaHgXfue8c'
    headers = {'User-Agent': user_agent, 'Authorization': access_token}
    response = requests.get(url, headers=headers)
    text = response.text

    marker0 = 'person-status_style_gray'
    parameter0 = str.find(text, marker0)
    text_fragment0 = text[parameter0:]
    data0 = BeautifulSoup(text_fragment0, "html.parser")
    loser = data0.find('a')

    marker1 = 'person-status_style_green'
    parameter1 = str.find(text, marker1)
    text_fragment1 = text[parameter1:]
    data1 = BeautifulSoup(text_fragment1, "html.parser")
    winner = data1.find('a')

    # marker2 = 'content__title'
    # parameter2 = str.find(text, marker2)
    # text_fragment2 = text[parameter2:]
    # data2 = BeautifulSoup(text_fragment2, "html.parser")
    # event = data2.find('a')

    return(winner, loser)

#This gets the date of an event
def date_getter():
    file = open('C:\\Users\\Max\\PycharmProjects\\fightmetrics\\event_links(no-dups)', 'rb')
    event_links_and_dates = {}
    for url in file:
        begin_marker0 = 'http'
        end_marker0 = '\\'
        url = str(url)
        parameter0 = str.find(url, begin_marker0)
        parameter1 = str.find(url, end_marker0)

        url = url[parameter0:parameter1]

        user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
        access_token = 'Bearer g7obord03PfeJ7TwQe-pNKVA0pQltMP6zGa76JKhGRIOOEDuB-IrsxdaHgXfue8c'
        headers = {'User-Agent': user_agent, 'Authorization': access_token}
        response = requests.get(url, headers=headers)
        text = response.text

        #This gets the date of the event
        begin_marker0 = 'Date:\n'
        end_marker0 = '\n'
        parameter0 = str.find(text, begin_marker0)
        textfragment0 = text[parameter0:]
        data0 = BeautifulSoup(textfragment0, "html.parser")
        pretty_data0 = data0.prettify()

        end_parameter0 = str.find(pretty_data0[len(begin_marker0):], end_marker0)

        date = pretty_data0[len(begin_marker0):len(begin_marker0)+end_parameter0]
        event_links_and_dates[url] = date


fighters_dict = {}

#This gets the sorted event list to access urls
# file = open('events_and_dates(numbers).pkl', 'rb')
# pick = pickle.load(file)
# tuple_list = pick.items()
#
# sorted = sorted(tuple_list, key=lambda x: x[1])
# n = 0
# for line in sorted:
#     n +=1
#     if n > 75:
#         event_analyses(line[0])
#
# pick = open(#'fighter_elos_full.pkl', 'wb')
# pickle.dump(fighters_dict, pick)
# pick.close()