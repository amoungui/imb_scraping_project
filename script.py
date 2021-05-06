#! /usr/bin/env python3
# coding: utf-8
import requests 
from bs4 import BeautifulSoup 
from Movie import Movie as Movie 
from MovieManager import MovieManager as Manager 

## @method getlink
## @param tag: a taget
## @return link of single page
def getlink(tag):
    target = tag.find('h3', attrs={'class':'lister-item-header'})
    a = target.find('a')
    _link = a['href']
    return _link

## @method _setlink
## @param tag: a taget
## @return link of single page
def _link(url):
    return 'https://www.imdb.com/'+ str(url)+'?ref_=adv_li_tt'


def main():
    entity = Movie()
    url = 'https://www.imdb.com/search/title/?at=0&num_votes=5000,&sort=user_rating,desc&start=1&title_type=feature'
    res = requests.get(url)

    if res.ok:
        soup = BeautifulSoup(res.text, 'html.parser')
        tags = soup.find_all('div', attrs={'class':'lister-item-content'})
        for tag in tags:
            r = requests.get(_link(getlink(tag)))
            if r.ok:
                content = BeautifulSoup(r.text, 'html.parser')
                manager = Manager(entity, [content, tag])        
                return entity.__getgross__()

#    for step in range(1,5000,50):
#        print('page: ', step)
#        for i in range(1, 50):
#            print(i)

if __name__ == '__main__':
    print(main())

