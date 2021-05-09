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
     
    def parse_json(self, entity):
        data = {
            'title': entity.__gettitle__(),
            'rating': entity.__getrating__(),
            'score': entity.__getscore__(),
            'vote': entity.__getvote__(),
            'type': entity.__gettype__(),
            'director':entity.__getdirector__(),
            'writter': entity.__getwritter__(),
            'duration': entity.__getduration__(),
            'release date': entity.__getrelease_date__(),
            'release country': entity.__getrelease_country__(),
            'location': entity.__getlocation__(),
            'reviews': entity.__getreview__(),
            'writter filmographie': entity.__getwritterfilmographie__(),
            'director filmographie': entity.__getdirectorfilmographie__(),
            'budget': entity.__getbudget__(),
            'Opening weekend USA': entity.__getopening_weekend__(),
            'gross': entity.__getgross__(),
            'Cumulate Worldwide Gross': entity.__getworldwide_gross__(),
            'runtime': entity.__getruntime__(),
            'sound Mix': entity.__getsound_mix__(),
            'Color': entity.__getcolor__(),
            'Aspect Ratio': entity.__getaspect_ratio__()
        }   
        
        return  self.dataset.append(data) #json.dumps(self.dataset, indent=2)  json.dumps(data, indent=2) 
        
        
        
    def to_csv(self):
        directory = os.path.dirname(os.path.dirname(__file__)) # we get the right path.
        path_to_file = os.path.join(directory, "data", 'dataset.csv') # with this path, we go inside the folder `data` and get the file.
        
        with open(path_to_file, 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.dataset[0].keys())
            writer.writeheader()
            
            for row in self.dataset:
                writer.writerow(row)
        
        print('"dataset.csv" has been written successfully!')