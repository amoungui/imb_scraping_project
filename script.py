#! /usr/bin/env python3
# coding: utf-8
import requests 
from bs4 import BeautifulSoup 
from Movie import Movie as Movie 
from MovieManager import MovieManager as Manager 

entity = Movie()

url = 'https://www.imdb.com/search/title/?at=0&num_votes=5000,&sort=user_rating,desc&start=1&title_type=feature'

res = requests.get(url)

def main():
    if res.ok:
        soup = BeautifulSoup(res.text, 'html.parser')
        tags = soup.find_all('div', attrs={'class':'lister-item-content'})
        [print(str(tag)+'\n\n') for tag in tags]
        

#    for step in range(1,5000,50):
#        print('page: ', step)
#        for i in range(1, 50):
#            print(i)

if __name__ == '__main__':
    main()

