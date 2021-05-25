import os
import csv
from Managers.EntityManager import EntityManager

class DebtManager(EntityManager):
    dataset = []
    def __init__(self, entity, tags:list):
        self.entity = entity
        self.getcountry(tags[0])
        self.getyear_2018(tags[1])
        self.getyear_2017(tags[2])
        self.getyear_2016(tags[3])
        self.getyear_2015(tags[4])
        self.getyear_2014(tags[5])
         
    def getcountry(self, tag):
        """ @method getcountry
            @param tag: a taget
            @description hydrate the value of the country entity  
        """                     
        try:
            return self.entity.__setcountry__(tag.text)
        except (TypeError, AttributeError, IndexError):
            return self.entity.__setcountry__(None)        
                               
    def getyear_2018(self, tag):
        """ @method getyear_2018
            @param tag: a taget
            @description hydrate the value of the gross for 2018 entity  
        """                     
        try:
            return self.entity.__setdebt_2018__(tag.text)
        except (TypeError, AttributeError, IndexError):
            return self.entity.__setdebt_2018__(None)        
        
    def getyear_2017(self, tag):
        """ @method getyear_2017
            @param tag: a taget
            @description hydrate the value of the gross for 2017 entity  
        """                     
        try:
            return self.entity.__setdebt_2017__(tag.text)
        except (TypeError, AttributeError, IndexError):
            return self.entity.__setdebt_2017__(None)         
        
    def getyear_2016(self, tag):
        """ @method getyear_2016
            @param tag: a taget
            @description hydrate the value of the gross for 2017 entity  
        """                     
        try:
            return self.entity.__setdebt_2016__(tag.text)
        except (TypeError, AttributeError, IndexError):
            return self.entity.__setdebt_2016__(None)         
                
    def getyear_2015(self, tag):
        """ @method getyear_2015
            @param tag: a taget
            @description hydrate the value of the gross for 2015 entity  
        """                     
        try:
            return self.entity.__setdebt_2015__(tag.text)
        except (TypeError, AttributeError, IndexError):
            return self.entity.__setdebt_2015__(None)         

    def getyear_2014(self, tag):
        """ @method getyear_2014
            @param tag: a taget
            @description hydrate the value of the gross for 2014 entity  
        """                     
        try:
            return self.entity.__setdebt_2014__(tag.text)
        except (TypeError, AttributeError, IndexError):
            return self.entity.__setdebt_2014__(None)         

    def debt_to_json(self, entity):
        """ @method to_json
            @param Object: entity 
            @return List 
            @description Construct a dictionary from the object pass as a parameter 
                        and add it to the attribute of the class which is a list. 
                        it thus returns a dictionary list 
        """                
        data = {
            'Country Name': entity.__getcountry__(),
            'debt_2018': entity.__debt_2018__(),
            'debt_2017': entity.__debt_2017__(),
            'debt_2016': entity.__debt_2016__(),
            'debt_2015': entity.__debt_2015__(),
            'debt_2014':entity.__debt_2014__()
        }           
        return  self.dataset.append(data)
                                
    def debt_to_csv(self):
        """ @method to_csv
            @param None: 
            @return None
            @description write data into the csv file 
        """        
        directory = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) # we get the right path.
        path_to_file = os.path.join(directory, "data", 'debt.csv') # with this path, we go inside the folder `data` and get the file.
        
        with open(path_to_file, 'w', encoding='utf-8') as csv_file: # we open the file as csv_file in w mode.
            writer = csv.DictWriter(csv_file, fieldnames=self.dataset[0].keys()) # instatiation of Writer objet that get the file and the fieldnames
            writer.writeheader() # we writer the header of the file
            
            for row in self.dataset:
                writer.writerow(row) # iteration into the dataset to write each row into the csv_file
        
        print('debt.csv has been written successfully!')                        
                        