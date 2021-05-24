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
    """[summary: get the link of a page]

    Args:
        tag ([html target objet]): [description]

    Returns:
        [String]: the link of a current page
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
    
    """[summary: construct the link of the single page of one movie]

    Args:
        url (string): the url of the current single movie page

    Returns:
        [string]: the link of a current single page
    """       
    return 'https://www.imdb.com/'+ str(url)+'?ref_=adv_li_tt'

def movie_launcher():
    """[summary: launch the script to scrap all information of imb movie platform]
    """
    entity = Movie() # instantiation of the movie objet
    for step in range(1,13117,50): 
        url = 'https://www.imdb.com/search/title/?at=0&num_votes=5000,&sort=user_rating,desc&start='+str(step)+'&title_type=feature'
        res = requests.get(url)

        if res.ok:
            soup = BeautifulSoup(res.content.decode('utf-8', 'ignore'), 'html.parser')
            tags = soup.find_all('div', attrs={'class':'lister-item-content'})
            for tag in tags:
                r = requests.get(_link(getlink(tag))) # 'https://www.imdb.com/title/tt0111161/?ref_=adv_li_tt'
                if r.ok:
                    print('i')
                    content = BeautifulSoup(r.text, 'html.parser') # we get the soup content 
                    manager = Manager(entity, [content, tag]) # initialization of Manager  of movie 
                    manager.parse_json(entity) # convert the current objet to dictionnary
                    manager.to_csv() # register the current entity of movie into the csv file
                    time.sleep(3)

if __name__ == '__main__':
    print(movie_launcher())
