#! /usr/bin/env python3
# coding: utf-8
import requests 
from bs4 import BeautifulSoup as Soup

url = 'https://www.imdb.com/search/title/?at=0&num_votes=5000,&sort=user_rating,desc&start=1&title_type=feature'

res = req.get(url)

def main():
    print(res)


if __name__ == '__main__':
    main()
    