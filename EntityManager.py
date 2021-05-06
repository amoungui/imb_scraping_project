import os
import io
import requests
from bs4 import BeautifulSoup
import csv
import json

class EntityManager:
    entity = None
    dataset = []
        
    def getPaginate(n:int):
        return self.entity.paginate(n)
    
    def fetch(self, url):
        print('HTTP GET request to URL: %s' % url, end='')
        res = requests.get(url)
        print(' | Status code: %s' % res.status_code)
        
        return res
    def parse(self, html):
        content = BeautifulSoup(html, 'html.parser')
        
    def to_csv(self):
        directory = os.path.dirname(os.path.dirname(__file__)) # we get the right path.
        path_to_file = os.path.join(directory, "data", 'results.csv') # with this path, we go inside the folder `data` and get the file.
        
        with open(path_to_file, 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.dataset[0].keys())
            writer.writeheader()
            
            for row in self.dataset:
                writer.writerow(row)
        
        print('"results.csv" has been written successfully!')