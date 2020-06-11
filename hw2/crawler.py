from bs4 import BeautifulSoup
import requests

with open('olympic_shotpush_data/years', 'r') as y_file:
    urls = y_file.readlines()
    for url in urls:
        with open('./olympic_shotpush_data/'+url.split('/')[3].split('-')[-1]+'.txt', 'w') as out_file:
            r = requests.get(url[:-1])
            soup = BeautifulSoup(r.text, 'html.parser')
            td_tag = soup.find_all('td', class_ = 'col3')
            for tag in td_tag:
                out_file.write(tag.string.strip()+'\n')