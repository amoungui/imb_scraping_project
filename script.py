#! /usr/bin/env python3
# coding: utf-8
import sys

from os.path import dirname, abspath
d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

import requests 
from bs4 import BeautifulSoup 
import time
from Models.Movie import Movie as Movie 
from Managers.MovieManager import MovieManager as Manager 


def getlink(tag):
    """ @method getlink
        @param tag: a taget
        @return link of a page
    """    
    target = tag.find('h3', attrs={'class':'lister-item-header'})
    a = target.find('a')
    _link = a['href']
    return _link

def _link(url):
    """ @method _link
        @param tag: a taget
        @return link of single page
    """        
    return 'https://www.imdb.com/'+ str(url)+'?ref_=adv_li_tt'

def main():
    entity = Movie()
    for step in range(1,13117,50):
        url = 'https://www.imdb.com/search/title/?at=0&num_votes=5000,&sort=user_rating,desc&start='+str(step)+'&title_type=feature'
        res = requests.get(url)

        if res.ok:
            soup = BeautifulSoup(res.content.decode('utf-8', 'ignore'), 'html.parser')
            tags = soup.find_all('div', attrs={'class':'lister-item-content'})
            for tag in tags:
                r = requests.get(_link(getlink(tag)))
                if r.ok:
                    print('i')
                    content = BeautifulSoup(r.text, 'html.parser')
                    manager = Manager(entity, [content, tag])
                    manager.parse_json(entity)
                    manager.to_csv()
                    time.sleep(1)

if __name__ == '__main__':
    print(main())

