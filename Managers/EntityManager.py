import os
import csv

class EntityManager:
    entity = None
    dataset = []

    def parse_json(self, entity):
        """ @method parse_json
            @param Object: entity 
            @return List of dictionnary
            @description Construct a dictionary from the object pass as a parameter 
                        and add it to the attribute of the class which is a list. 
                        it thus returns a dictionary list 
        """                
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
            'storyline': entity.__getstoryline__(),
            'budget en $': entity.__getbudget__(),
            'Opening weekend USA en $': entity.__getopening_weekend__(),
            'gross en $': entity.__getgross__(),
            'Cumulate Worldwide Gross en $': entity.__getworldwide_gross__(),
            'runtime': entity.__getruntime__(),
            'sound Mix': entity.__getsound_mix__(),
            'Color': entity.__getcolor__(),
            'Aspect Ratio': entity.__getaspect_ratio__()
        }   
        
        return  self.dataset.append(data) #json.dumps(self.dataset, indent=2)  json.dumps(data, indent=2) 
        
    def to_csv(self):
        """ @method to_csv
            @param None: 
            @return None
            @description write data into the csv file 
        """        
        directory = os.path.dirname(os.path.dirname(__file__)) # we get the right path.
        path_to_file = os.path.join(directory, "data", 'dataset.csv') # with this path, we go inside the folder `data` and get the file.
        
        with open(path_to_file, 'w', encoding='utf-8') as csv_file: # we open the file as csv_file in w mode.
            writer = csv.DictWriter(csv_file, fieldnames=self.dataset[0].keys()) # instatiation of Writer objet that get the file and the fieldnames
            writer.writeheader() # we writer the header of the file
            
            for row in self.dataset:
                writer.writerow(row) # iteration into the dataset to write each row into the csv_file
        
        print('dataset.csv has been written successfully!')
        
    def strip_date(self, String: str):
        """ @method strip_date
            @param tag: a taget
            @return data
            @description move to the date the name of the country release   
        """     
        i = String.find('(')                  
        return String[0:i]

    def formate_date(self, data):
        """[summary: format the date of the release date]

        Args:
            data (str): the date that we want formate

        Returns:
            [str]: the new date formated
        """
        d = data.split()
        month = { 
            'January': '01',
            'February': '02',                 
            'March': '03',
            'April': '04',
            'May': '05',
            'June': '06',
            'July': '07',
            'August': '08',       
            'September': '09',
            'October': '10',
            'November': '11',
            'December': '12'
        }        
        new_date = ''
        if len(d) == 2:
            new_date = ''+d[1]+'-'+month[d[0]]+'-'+'01'
        if len(d) == 3:
            new_date = ''+d[2]+'-'+month[d[1]]+'-'+d[0]
        if len(d) == 1:
            new_date = ''+d[0]+'-'+month['January']+'-'+'01'
        if d in 'xxx':
            new_date = ''+'1975'+'-'+month['January']+'-'+'01'            
        return new_date    
        