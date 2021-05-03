#! /usr/bin/env python3
# coding: utf-8
import requests 
from bs4 import BeautifulSoup 

url = 'https://www.imdb.com/search/title/?at=0&num_votes=5000,&sort=user_rating,desc&start=1&title_type=feature'

res = requests.get(url)

## @method getvote
## @param tag: a taget
## @return vote value
def getvote(tag):
    return tag.find('span', attrs={'name':'nv'}).text

## @method getrating
## @param tag: a taget
## @return rating(note) value
def getrating(tag):
    return tag.find('div', attrs={'class':'ratings-imdb-rating'}).find('strong').text

## @method getruntime
## @param tag: a taget
## @return runtime value
def getruntime(tag):
    return tag.find('span', attrs={'class':'runtime'}).text

## @method getgross
## @param tag: a taget
## @return Gross value
def getgross(tag):
    return tag.find('span', attrs={'data-value':'28,341,469'}).text

## @method getfilmname
## @param tag: a taget
## @return name of film
def getfilmname(tag):
    return tag.find('h3', attrs={'class':'lister-item-header'}).find('a').text

## @method gettype
## @param tag: a taget
## @return type of film
def gettype(tag):
    return tag.find('span', attrs={'class':'genre'}).text

## @method getscore
## @param tag: a taget
## @return film metascore
def getscore(tag):
    return tag.find('span', attrs={'class':'metascore'}).text

def main():
    if res.ok:
        soup = BeautifulSoup(res.text, 'html.parser')
        first_results = soup.find_all('div', attrs={'class':'lister-item-content'}) #lister-item-content
        
        print(getscore(first_results[1]))


if __name__ == '__main__':
    main()

