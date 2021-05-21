from Managers.EntityManager import EntityManager

class MetricManager(EntityManager):
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
            return self.entity.__setyear_2018__(tag.text)
        except (TypeError, AttributeError, IndexError):
            return self.entity.__setyear_2018__(None)        
        
    def getyear_2017(self, tag):
        """ @method getyear_2017
            @param tag: a taget
            @description hydrate the value of the gross for 2017 entity  
        """                     
        try:
            return self.entity.__setyear_2017__(tag.text)
        except (TypeError, AttributeError, IndexError):
            return self.entity.__setyear_2017__(None)         
        
    def getyear_2016(self, tag):
        """ @method getyear_2016
            @param tag: a taget
            @description hydrate the value of the gross for 2017 entity  
        """                     
        try:
            return self.entity.__setyear_2016__(tag.text)
        except (TypeError, AttributeError, IndexError):
            return self.entity.__setyear_2016__(None)         
                
    def getyear_2015(self, tag):
        """ @method getyear_2015
            @param tag: a taget
            @description hydrate the value of the gross for 2015 entity  
        """                     
        try:
            return self.entity.__setyear_2015__(tag.text)
        except (TypeError, AttributeError, IndexError):
            return self.entity.__setyear_2015__(None)         

    def getyear_2014(self, tag):
        """ @method getyear_2014
            @param tag: a taget
            @description hydrate the value of the gross for 2014 entity  
        """                     
        try:
            return self.entity.__setyear_2014__(tag.text)
        except (TypeError, AttributeError, IndexError):
            return self.entity.__setyear_2014__(None)         
                                
                        