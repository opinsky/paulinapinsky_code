import requests
from slugify import slugify
import os
import csv
from bs4 import BeautifulSoup

UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.39 Safari/537.36'


URLs = [18, 49, 17, 13, 16, 15, 6, 3, 1]
base_URL = 'https://paulinapinsky.com.br/?cat='

with open('pp.csv', 'w', newline='') as csvfile:
  xfile = csv.writer(csvfile, delimiter=";", quotechar="|", quoting=csv.QUOTE_MINIMAL)
  for cat in URLs:
    URL = base_URL + str(cat)
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    quadros = soup.find(class_='content').findAll(class_='post')

    for quadro in quadros:
        title = quadro.find('h2').text
        filename = slugify(title.lstrip()[(title.rfind('/')+1):])
        categories = (quadro.find(class_='postmetadata').findAll('a', {"rel":"category"}))
        year = (quadro.find(class_='postmetadata').findAll('a', {"rel":"tag"}))
        detail_page = requests.get(quadro.find('a', {"rel":"bookmark"}).get('href'))
        detail_soup = BeautifulSoup(detail_page.content, 'html.parser').find('div', class_='post')
        try:
            image_URL = detail_soup.find('img', class_='alignnone')['src']
        except:
            print("Deu Pau")
        detail_text = [z for z in ','.join([x.get_text() for x in detail_soup.select('p')]).split('\n')
                                                       if z != '' and z != ',' and z[0:10] != 'This entry' and z[0:14] != 'You can follow']

        
        print (title)
        print (filename)
        xcat = []
        for cat in categories:
          xcat.append (cat.text)
        print (image_URL)
        print (detail_text)
        xfile.writerow([filename, title, xcat, detail_text])
        #os.system('wget -O ' + filename + '.jpeg ' + image_URL)
    