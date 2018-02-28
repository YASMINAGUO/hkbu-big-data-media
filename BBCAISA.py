import requests
import csv
from bs4 import BeautifulSoup

resp = requests.get('http://www.bbc.com/news/world/asia/china')
html_str = resp.text
document = BeautifulSoup(html_str,'html.parser')

headlines = document.find_all('h3',attrs ={'class':'title-link__title'})

lists = [ ]
for title in headlines:
        name = title.find('span',attrs = {'class':'title-link__title-text'})
        lists.append(name.text)

print(lists)

mydates = document.find_all('ul',attrs ={'class':'mini-info-list'})

dates = [ ]
for time in mydates:
        t = time.find('li',attrs = {'class':'mini-info-list__item'})
        dates.append(t.text)

mysection = document.find_all('li',attrs ={'class':'mini-info-list__item mini-info-list__item--section'})

section = [ ]
for sec in mysection:
        s = sec.find('a',attrs = {'class':'mini-info-list__section'})
        section.append(s.text)

print(dates)
print(section)

with open('bbc.csv','w') as f:
         writer = csv.writer(f)
         header = ['headlines', 'date', 'section']
         writer.writerow(header)

         writer.writerows(zip(lists,dates,section))
         




