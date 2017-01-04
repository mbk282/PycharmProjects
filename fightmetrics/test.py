import pickle
import math
import requests
from bs4 import BeautifulSoup

def prediction(rating_fighter1, rating_fighter2):
    odds_fighter_1 = (1.0 / (1.0 + math.pow(10.0, ((rating_fighter2 - rating_fighter1) / 400.0))))
    return(odds_fighter_1)

url = 'http://www.fightmetric.com/event-details/4b2390cfaceb91d8'

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

pick = open('fighter_elos_full.pkl', 'rb')
file = pickle.load(pick)

fighter1 = file['Amanda Nunes ']
fighter2 = file['Ronda Rousey ']
predict = prediction(fighter1, fighter2)
#print(predict)
odds_fighter_1 = 1.0 / predict
odds_fighter_2 = 1.0 / prediction(fighter2, fighter1)
print('odds '+ 'Amanda Nunes: '+str(odds_fighter_1))
print('odds '+'Ronda Rousey: '+str(odds_fighter_2))

fighter1 = file['Dominick Cruz ']
fighter2 = file['Cody Garbrandt ']
predict = prediction(fighter1, fighter2)
#print(predict)
odds_fighter_1 = 1.0 / predict
odds_fighter_2 = 1.0 / prediction(fighter2, fighter1)
print('odds '+ 'Dominick Cruz: '+str(odds_fighter_1))
print('odds '+'Cody Garbrandt: '+str(odds_fighter_2))

fighter1 = file['TJ Dillashaw ']
fighter2 = file['John Lineker ']
predict = prediction(fighter1, fighter2)
#print(predict)
odds_fighter_1 = 1.0 / predict
odds_fighter_2 = 1.0 / prediction(fighter2, fighter1)
print('odds '+ 'TJ Dillashaw: '+str(odds_fighter_1))
print('odds '+'John Lineker: '+str(odds_fighter_2))

fighter1 = file['Dong Hyun Kim ']
fighter2 = file['Tarec Saffiedine ']
predict = prediction(fighter1, fighter2)
#print(predict)
odds_fighter_1 = 1.0 / predict
odds_fighter_2 = 1.0 / prediction(fighter2, fighter1)
print('odds '+ 'Dong Hyun Kim: '+str(odds_fighter_1))
print('odds '+'Tarec Saffiedine: '+str(odds_fighter_2))

fighter1 = file['Louis Smolka ']
fighter2 = file['Ray Borg ']
predict = prediction(fighter1, fighter2)
#print(predict)
odds_fighter_1 = 1.0 / predict
odds_fighter_2 = 1.0 / prediction(fighter2, fighter1)
print('odds '+ 'Louis Smolka: '+str(odds_fighter_1))
print('odds '+'Ray Borg: '+str(odds_fighter_2))

fighter1 = file['Johny Hendricks ']
fighter2 = file['Neil Magny ']
predict = prediction(fighter1, fighter2)
#print(predict)
odds_fighter_1 = 1.0 / predict
odds_fighter_2 = 1.0 / prediction(fighter2, fighter1)
print('odds '+ 'Johny Hendricks: '+str(odds_fighter_1))
print('odds '+'Neil Magny: '+str(odds_fighter_2))

fighter1 = file['Antonio Carlos Junior ']
fighter2 = file['Marvin Vettori ']
predict = prediction(fighter1, fighter2)
#print(predict)
odds_fighter_1 = 1.0 / predict
odds_fighter_2 = 1.0 / prediction(fighter2, fighter1)
print('odds '+ 'Antonio Carlos Junior: '+str(odds_fighter_1))
print('odds '+'Marvin Vettori: '+str(odds_fighter_2))

fighter1 = file['Mike Pyle ']
fighter2 = file['Alex Garcia ']
predict = prediction(fighter1, fighter2)
#print(predict)
odds_fighter_1 = 1.0 / predict
odds_fighter_2 = 1.0 / prediction(fighter2, fighter1)
print('odds '+ 'Mike Pyle: '+str(odds_fighter_1))
print('odds '+'Alex Garcia: '+str(odds_fighter_2))

fighter1 = file['Brandon Thatch ']
fighter2 = file['Niko Price ']
predict = prediction(fighter1, fighter2)
#print(predict)
odds_fighter_1 = 1.0 / predict
odds_fighter_2 = 1.0 / prediction(fighter2, fighter1)
print('odds '+ 'Brandon Thatch: '+str(odds_fighter_1))
print('odds '+'Niko Price: '+str(odds_fighter_2))

fighter1 = file['Alex Oliveira ']
fighter2 = file['Tim Means ']
predict = prediction(fighter1, fighter2)
#print(predict)
odds_fighter_1 = 1.0 / predict
odds_fighter_2 = 1.0 / prediction(fighter2, fighter1)
print('odds '+ 'Alex Oliveira: '+str(odds_fighter_1))
print('odds '+'Tim Means: '+str(odds_fighter_2))


pick.close()