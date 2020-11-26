from bs4 import BeautifulSoup
import requests

def extract(page):
    url=f'https://www.monster.com/jobs/search/?q=Python-Developer&where=Atlanta__2C-GA&intcid=skr_navigation_nhpso_searchMain&stpage=1&page={page}'
    r=requests.get(url)
    soup=BeautifulSoup(r.content,'html.parser')
    return soup


def transform(soup):
    global title,company,location,time,x
    divs=soup.find_all('section',class_='card-content')
    # print(len(divs))
    for item in divs:
        try:
            title=item.find('h2',class_='title').text.strip()
            company=item.find('div',class_='company').text.strip()
            location=item.find('div',class_='location').text.strip()
            time=item.find('time',datetime='2017-05-26T12:00').text.strip()
            x=title,company,location,time
            print('Title: '+title)
            print('Company: '+company)
            print('Location: '+location)
            print('Time Posted: '+time+'\n')
        except:
            title='0'
            company='0'
            location='0'
            time='0'
            

with open('Future Jobs.txt','w') as Jobs:            
    for i in range(0,5):
        c=extract(i)
        transform(c) 
        Jobs.write(str(x))