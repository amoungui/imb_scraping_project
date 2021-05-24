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
    gdp = Metric()
    rate = Rate()
    debt = Debt()
    capita = Capita()
    inflation = Inflation()
    manufacturing = Manufacturing()
    links = ['gdp-gross-domestic-product', 'gdp-growth-rate', 'gdp-per-capita', 'debt-to-gdp-ratio', 'inflation-rate-cpi', 'manufacturing-output']
    for link in links:     
        if link in 'gdp-gross-domestic-product':
            url = 'https://www.macrotrends.net/countries/ranking/'+link
            res = requests.get(url)
            
            if res.ok:
                soup = BeautifulSoup(res.content.decode('utf-8', 'ignore'), 'html.parser')
                tags = soup.find('tbody').find_all('tr')
                for tag in tags:
                    manager =  MetricManager(gdp, tag.find_all('td'))
                    manager.parse_metric_to_json(gdp)
                    manager.gdp_to_csv()
                    
        if link in 'gdp-growth-rate':
            url = 'https://www.macrotrends.net/countries/ranking/'+link
            res = requests.get(url)
            
            if res.ok:
                soup = BeautifulSoup(res.content.decode('utf-8', 'ignore'), 'html.parser')
                tags = soup.find('tbody').find_all('tr')
                for tag in tags:
                    manager =  RateManager(rate, tag.find_all('td'))
                    manager.to_json(rate)
                    manager.to_csv()     
                    
        if link in 'gdp-per-capita':
            url = 'https://www.macrotrends.net/countries/ranking/'+link
            res = requests.get(url)
            
            if res.ok:
                soup = BeautifulSoup(res.content.decode('utf-8', 'ignore'), 'html.parser')
                tags = soup.find('tbody').find_all('tr')
                for tag in tags:
                    manager =  CapitaManager(capita, tag.find_all('td'))
                    manager.to_json(capita)
                    manager.to_csv()                         
                       
        if link in 'debt-to-gdp-ratio':
            url = 'https://www.macrotrends.net/countries/ranking/'+link
            res = requests.get(url)
            
            if res.ok:
                soup = BeautifulSoup(res.content.decode('utf-8', 'ignore'), 'html.parser')
                tags = soup.find('tbody').find_all('tr')
                for tag in tags:
                    manager =  DebtManager(debt, tag.find_all('td'))
                    manager.to_json(debt)
                    manager.to_csv()      
                    
        if link in 'inflation-rate-cpi':
            url = 'https://www.macrotrends.net/countries/ranking/'+link
            res = requests.get(url)
            
            if res.ok:
                soup = BeautifulSoup(res.content.decode('utf-8', 'ignore'), 'html.parser')
                tags = soup.find('tbody').find_all('tr')
                for tag in tags:
                    manager =  InflationManager(inflation, tag.find_all('td'))
                    manager.to_json(inflation)
                    manager.to_csv()      
                    
        if link in 'manufacturing-output':
            url = 'https://www.macrotrends.net/countries/ranking/'+link
            res = requests.get(url)
            
            if res.ok:
                soup = BeautifulSoup(res.content.decode('utf-8', 'ignore'), 'html.parser')
                tags = soup.find('tbody').find_all('tr')
                for tag in tags:
                    manager =  ManufacturingManager(manufacturing, tag.find_all('td'))
                    manager.to_json(manufacturing)
                    manager.to_csv()                                                                     
                       
if __name__ == '__main__':
    print(metric_launcher())
