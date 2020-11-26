from bs4 import BeautifulSoup
import requests
joblist=[]

def extract(page):
    headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'}
    url=f'https://www.indeed.com/jobs?q=Python%20Developer&l=Augusta%2C%20GA&start={page}&vjk=5ab1434abb63a27b'
    r=requests.get(url,headers)
    soup=BeautifulSoup(r.content,'html.parser')
    return soup

def transform(soup):
    divs=soup.find_all('div',class_='jobsearch-SerpJobCard')
    for item in divs:
        # title=item.find('a').text.strip()
        # # print(title)
        # company=item.find('span',class_='company').text.strip()
        # # print(company)
        try:
            title = item.find('a').text.strip()
            print('Title= '+title)
            company = item.find('span', class_='company').text.strip()
            print('Company= '+company)
            salary=item.find('span',class_='salaryText').text.strip()
            print('Salary= '+salary+'\n')
        except:
            title=''
            company=''
            salary=''
            pass

        job={
            'title': title,
            'company': company,
            'salary': salary
        }
        joblist.append(job)
    return joblist


c=extract(0)
transform(c)
# print(joblist)