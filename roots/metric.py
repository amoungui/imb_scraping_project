#! /usr/bin/env python3
# coding: utf-8
import sys

from os.path import dirname, abspath
d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

from Models.Movie import Movie as Movie 
from Models.Metric import Metric
from Managers.MovieManager import MovieManager as Manager 
from Managers.MetricManager import MetricManager
from roots.movie import *



def metric_launcher():
    """[the method that run the script]
    """
    entity = Metric()
    links = ['gdp-gross-domestic-product', 'gdp-growth-rate', 'gdp-per-capita', 'gni-gross-national-income', 'gni-per-capita', 'debt-to-gdp-ratio', 'gnp-gross-national-product', 'inflation-rate-cpi', 'economic-growth-rate', 'manufacturing-output']
    for link in links:        
        url = 'https://www.macrotrends.net/countries/ranking/'+link
        res = requests.get(url)
        
        if res.ok:
            soup = BeautifulSoup(res.content.decode('utf-8', 'ignore'), 'html.parser')
            tags = soup.find('tbody').find_all('tr')
            for tag in tags:
                manager =  MetricManager(entity, tag.find_all('td'))
                manager.parse_metric_to_json(entity)
                manager.to_csv()
        
if __name__ == '__main__':
    print(metric_launcher())
