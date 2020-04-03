import requests
import re
from bs4 import BeautifulSoup

url = 'https://jinyong.fandom.com/zh/wiki/%E7%A5%9E%E9%B5%B0%E4%BF%A0%E4%BE%B6%E8%A7%92%E8%89%B2%E5%88%97%E8%A1%A8'

r = requests.get(url)
soup = BeautifulSoup(r.text, features="html.parser")
text = soup.text

pattern = r'.+——|.+：'
temp = re.findall(pattern, text)

names = []
with open('./CondorHeroes/names_wiki.txt', 'w') as out_file:
    for n in temp:
        out_file.write(re.sub(r'：|——', '', n)+'\n')

