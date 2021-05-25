#! /usr/bin/env python3
# coding: utf-8
import sys

from os.path import dirname, abspath
d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

import requests 
from bs4 import BeautifulSoup 
from Models.metrics.gdp import Metric
from Models.metrics.gdp_rate import Rate
from Models.metrics.debt_to_gdp import Debt
from Models.metrics.gdp_per_capita import Capita
from Models.metrics.inflation import Inflation
from Models.metrics.manufacturing import Manufacturing
from Managers.Metrics.MetricManager import MetricManager
from Managers.Metrics.RateManager import RateManager
from Managers.Metrics.InflationManager import InflationManager
from Managers.Metrics.CapitaManager import CapitaManager
from Managers.Metrics.DebtManager import DebtManager
from Managers.Metrics.ManufacturingManager import ManufacturingManager


def metric_launcher():
    """[the method that run the script]
    """
    gdp = Metric() # instantiation of objet gdp
    rate = Rate() # instantiation of objet rate
    debt = Debt() # instantiation of objet debt
    capita = Capita() # instantiation of objet capita
    inflation = Inflation() # instantiation of objet inflation
    manufacturing = Manufacturing() # instantiation of objet gdp
    links = ['gdp-gross-domestic-product', 
             'gdp-growth-rate', 
             'gdp-per-capita', 
             'debt-to-gdp-ratio', 
             'inflation-rate-cpi', 
             'manufacturing-output'] # liste of the url of the page we want to scraping
    for link in links:     # we iterate in into each url
        if link in 'gdp-gross-domestic-product': # we verify if the current link match to url that we want to
            url = 'https://www.macrotrends.net/countries/ranking/'+link
            res = requests.get(url)
            
            if res.ok:
                soup = BeautifulSoup(res.content.decode('utf-8', 'ignore'), 'html.parser')
                tags = soup.find('tbody').find_all('tr')
                for tag in tags:
                    manager1 =  MetricManager(gdp, tag.find_all('td'))
                    manager1.gdp_to_json(gdp)
                    manager1.gdp_to_csv()
                    
        if link in 'gdp-growth-rate':
            url = 'https://www.macrotrends.net/countries/ranking/'+link
            res = requests.get(url)
            
            if res.ok:
                soup = BeautifulSoup(res.content.decode('utf-8', 'ignore'), 'html.parser')
                tags = soup.find('tbody').find_all('tr')
                for tag in tags:
                    manager2 =  RateManager(rate, tag.find_all('td'))
                    manager2.rate_to_json(rate)
                    manager2.rate_to_csv()     
                    
        if link in 'gdp-per-capita':
            url = 'https://www.macrotrends.net/countries/ranking/'+link
            res = requests.get(url)
            
            if res.ok:
                soup = BeautifulSoup(res.content.decode('utf-8', 'ignore'), 'html.parser')
                tags = soup.find('tbody').find_all('tr')
                for tag in tags:
                    manager3 =  CapitaManager(capita, tag.find_all('td'))
                    manager3.capita_to_json(capita)
                    manager3.capita_to_csv()                         
                       
        if link in 'debt-to-gdp-ratio':
            url = 'https://www.macrotrends.net/countries/ranking/'+link
            res = requests.get(url)
            
            if res.ok:
                soup = BeautifulSoup(res.content.decode('utf-8', 'ignore'), 'html.parser')
                tags = soup.find('tbody').find_all('tr')
                for tag in tags:
                    manager4 =  DebtManager(debt, tag.find_all('td'))
                    manager4.debt_to_json(debt)
                    manager4.debt_to_csv()      
                    
        if link in 'inflation-rate-cpi':
            url = 'https://www.macrotrends.net/countries/ranking/'+link
            res = requests.get(url)
            
            if res.ok:
                soup = BeautifulSoup(res.content.decode('utf-8', 'ignore'), 'html.parser')
                tags = soup.find('tbody').find_all('tr')
                for tag in tags:
                    manager5 =  InflationManager(inflation, tag.find_all('td'))
                    manager5.inflation_to_json(inflation)
                    manager5.inflation_to_csv()      
                    
        if link in 'manufacturing-output':
            url = 'https://www.macrotrends.net/countries/ranking/'+link
            res = requests.get(url)
            
            if res.ok:
                soup = BeautifulSoup(res.content.decode('utf-8', 'ignore'), 'html.parser')
                tags = soup.find('tbody').find_all('tr')
                for tag in tags:
                    manager6 =  ManufacturingManager(manufacturing, tag.find_all('td'))
                    manager6.manufact_to_json(manufacturing)
                    manager6.manufact_to_csv()                                                                     
                       
if __name__ == '__main__':
    print(metric_launcher())
